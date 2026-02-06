from fastapi import FastAPI
from app.database import engine
from app.models.base import Base

app = FastAPI()

# IMPORTA TODOS LOS MODELOS
from app.models import (
    rol, usuario, usuario_rol, servicio, pedido, recarga,
    historial_saldo, notificacion, token_recuperacion, ticket_soporte,
    evento_usuario, configuracion_sistema, reporte_mensual, bitacora_sesion
)

# CREA LAS TABLAS
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"mensaje": "API Flame Followers inicializada correctamente"}
