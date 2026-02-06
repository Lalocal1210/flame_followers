from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.configuracion_sistema import ConfiguracionSistema
from app.schemas.configuracion_sistema import ConfiguracionSistemaCreate, ConfiguracionSistemaOut
from typing import List
from datetime import datetime

router = APIRouter(prefix="/config", tags=["Configuración del sistema"])

@router.get("/", response_model=List[ConfiguracionSistemaOut])
def listar_configuraciones(db: Session = Depends(get_db)):
    return db.query(ConfiguracionSistema).order_by(ConfiguracionSistema.actualizacion.desc()).all()

@router.get("/{clave}", response_model=ConfiguracionSistemaOut)
def obtener_config(clave: str, db: Session = Depends(get_db)):
    config = db.query(ConfiguracionSistema).filter(ConfiguracionSistema.clave == clave).first()
    if not config:
        raise HTTPException(status_code=404, detail="Configuración no encontrada")
    return config

@router.post("/", response_model=ConfiguracionSistemaOut)
def crear_config(config: ConfiguracionSistemaCreate, db: Session = Depends(get_db)):
    existente = db.query(ConfiguracionSistema).filter(ConfiguracionSistema.clave == config.clave).first()
    if existente:
        raise HTTPException(status_code=400, detail="La clave ya existe")

    nueva = ConfiguracionSistema(
        clave=config.clave,
        valor=config.valor,
        descripcion=config.descripcion,
        actualizacion=datetime.utcnow()
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.put("/{clave}", response_model=ConfiguracionSistemaOut)
def actualizar_config(clave: str, config: ConfiguracionSistemaCreate, db: Session = Depends(get_db)):
    existente = db.query(ConfiguracionSistema).filter(ConfiguracionSistema.clave == clave).first()
    if not existente:
        raise HTTPException(status_code=404, detail="Configuración no encontrada")

    existente.valor = config.valor
    existente.descripcion = config.descripcion
    existente.actualizacion = datetime.utcnow()
    db.commit()
    db.refresh(existente)
    return existente
