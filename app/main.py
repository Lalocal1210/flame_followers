from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models.base import Base

# MODELOS que se usarán para crear las tablas si no existen
from app.models import (
    rol, usuario, usuario_rol, servicio, pedido, recarga,
    historial_saldo, notificacion, token_recuperacion, ticket_soporte,
    evento_usuario, configuracion_sistema, bitacora_sesion
)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Inicializar la aplicación FastAPI
app = FastAPI(title="Flame Followers API")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción reemplazar por dominio específico
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Importar routers
from app.routers import (
    auth,
    usuario,
    perfil,
    servicios,
    pedidos,
    recargas,
    historial_saldo,
    tickets_soporte,
    notificaciones,
    eventos_usuario,
    bitacora_sesion,
    configuraciones_sistema,
    reportes_mensuales
)

# Incluir routers en la aplicación
app.include_router(auth.router)
app.include_router(usuario.router)
app.include_router(perfil.router)
app.include_router(servicios.router)
app.include_router(pedidos.router)
app.include_router(recargas.router)
app.include_router(historial_saldo.router)
app.include_router(tickets_soporte.router)
app.include_router(notificaciones.router)
app.include_router(eventos_usuario.router)
app.include_router(bitacora_sesion.router)
app.include_router(configuraciones_sistema.router)
app.include_router(reportes_mensuales.router)

# Ruta raíz
@app.get("/")
def root():
    return {"mensaje": "🚀 Flame Followers API está activa"}
