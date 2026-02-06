from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi.responses import StreamingResponse
import io
import openpyxl
from datetime import datetime

from app.database import get_db
from app.models.reportes_mensuales import ReporteMensual
from app.models.pedido import Pedido
from app.models.usuario import Usuario
from app.models.recarga import Recarga
from app.schemas.reporte_mensual import ReporteMensualOut

from app.dependencies.roles import verificar_admin

router = APIRouter(prefix="/reportes", tags=["Reportes"])


@router.get("/", response_model=list[ReporteMensualOut], dependencies=[Depends(verificar_admin)])
def listar_reportes(
    anio: int = Query(None, description="Filtrar por año"),
    mes: int = Query(None, description="Filtrar por mes"),
    db: Session = Depends(get_db)
):
    query = db.query(ReporteMensual)
    if anio:
        query = query.filter(ReporteMensual.anio == anio)
    if mes:
        query = query.filter(ReporteMensual.mes == mes)
    return query.order_by(ReporteMensual.anio.desc(), ReporteMensual.mes.desc()).all()


@router.post("/generar", response_model=ReporteMensualOut, dependencies=[Depends(verificar_admin)])
def generar_reporte(db: Session = Depends(get_db)):
    hoy = datetime.utcnow()
    mes = hoy.month
    anio = hoy.year

    existente = db.query(ReporteMensual).filter(
        ReporteMensual.mes == mes,
        ReporteMensual.anio == anio
    ).first()

    if existente:
        raise HTTPException(status_code=400, detail="Ya existe un reporte para este mes")

    total_usuarios = db.query(Usuario).filter(
        func.extract('month', Usuario.fecha_registro) == mes,
        func.extract('year', Usuario.fecha_registro) == anio
    ).count()

    total_pedidos = db.query(Pedido).filter(
        func.extract('month', Pedido.fecha) == mes,
        func.extract('year', Pedido.fecha) == anio
    ).count()

    total_recargas = db.query(Recarga).filter(
        func.extract('month', Recarga.fecha) == mes,
        func.extract('year', Recarga.fecha) == anio
    ).count()

    ingresos_estimados = db.query(func.coalesce(func.sum(Pedido.costo), 0)).filter(
        func.extract('month', Pedido.fecha) == mes,
        func.extract('year', Pedido.fecha) == anio
    ).scalar()

    reporte = ReporteMensual(
        mes=mes,
        anio=anio,
        total_usuarios=total_usuarios,
        total_pedidos=total_pedidos,
        total_recargas=total_recargas,
        ingresos_estimados=ingresos_estimados,
        fecha_generado=datetime.utcnow()
    )

    db.add(reporte)
    db.commit()
    db.refresh(reporte)
    return reporte


@router.get("/exportar", response_class=StreamingResponse, dependencies=[Depends(verificar_admin)])
def exportar_excel_reportes(
    anio: int = Query(...),
    mes: int = Query(...),
    db: Session = Depends(get_db)
):
    reporte = db.query(ReporteMensual).filter(
        ReporteMensual.anio == anio,
        ReporteMensual.mes == mes
    ).first()

    if not reporte:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "ReporteMensual"

    ws.append([
        "Mes", "Año", "Total Usuarios", "Total Pedidos",
        "Total Recargas", "Ingresos Estimados", "Fecha Generado"
    ])

    ws.append([
        reporte.mes, reporte.anio, reporte.total_usuarios,
        reporte.total_pedidos, reporte.total_recargas,
        reporte.ingresos_estimados, reporte.fecha_generado.strftime("%Y-%m-%d %H:%M:%S")
    ])

    stream = io.BytesIO()
    wb.save(stream)
    stream.seek(0)

    filename = f"reporte_{anio}_{mes}.xlsx"
    return StreamingResponse(stream, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", headers={
        "Content-Disposition": f"attachment; filename={filename}"
    })
