#Se importa el framework APIrouter
from fastapi import APIRouter

#Se crea el APIrouter en lugar de fastApi
router = APIRouter()

#*****Instancia de productos
@router.get("/products")
async def products():
    return ["Producto1", "Producto2", "Producto3", "Producto4", "Producto5"]