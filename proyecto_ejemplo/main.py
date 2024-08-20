from fastapi import FastAPI

from appv1.routers import categories, login, users, roles
from fastapi.middleware.cors import CORSMiddleware
from appv1.schemas.user import UserCreate
from appv1.schemas.role import RoleBase
from db.database import test_db_connection
from core.security import get_hashed_password, verify_password, create_access_token


app = FastAPI()

app.include_router(users.router,prefix="/users", tags=["users"])

app.include_router(roles.router,prefix="/roles", tags=["roles"])

app.include_router(categories.router,prefix="/categories", tags=["category"])

app.include_router(login.router, prefix = "/access", tags=["access"])

# Configuración de CORS para permitir todas las solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Permitir estos métodos HTTP
    allow_headers=["*"],  # Permitir cualquier encabezado en las solicitudes
)

@app.on_event("startup")#esto hace que la función on_startup se ejecute inmmediatamente se inicié la app
def on_startup():
    test_db_connection()#Llama a la función que prueba la conexión a la base de datos


@app.get("/")
def read_root():
    return {"mensaje":"ADSO-26705086",
            "Autor": "Maribel Obando"}
# 
# @app.post("/create-user")
# def insert_user(user_id:str, full_name:str,mail:str,passhash:str, user_role:str):
#     return {"mensaje":"hello word"}

# @app.post("/create-user")
# def insert_user(usuario: UserCreate):
#     passEncriptado = get_hashed_password(usuario.passhash)
#     return {
#         "mensaje":"usando un schema", 
#         "id":usuario.user_id,
#         "contraseña":passEncriptado
#     }