######################################### Primera Parte################################################
# Instalación del framwork fastApi, código:
# -pip install fastapi-

# Instalación del Servidor Uvicorn, código:
# -pip install "uvicorn[standard]"-

# Instalación del framwork fastApi, código:
# -pip install fastapi[all]-

# Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI

from Routers import Grupo_A, Grupo_B, Grupo_C, Grupo_D, Grupo_E, Grupo_F, Grupo_G, Grupo_H, Grupo_I, Grupo_J

# Creamos un objeto a partir de la clase FastAPI
app = FastAPI()

# Utilizamos la (instancia) función get del framework FastAPI

app.include_router(Grupo_A.router)
app.include_router(Grupo_B.router)
app.include_router(Grupo_C.router)
app.include_router(Grupo_D.router)
app.include_router(Grupo_E.router)
app.include_router(Grupo_F.router)
app.include_router(Grupo_G.router)
app.include_router(Grupo_H.router)
app.include_router(Grupo_I.router)
app.include_router(Grupo_J.router)



@app.get("/")
async def imprimir():
    return {"ESTAS EN EL MAIN"}

# En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/Git
