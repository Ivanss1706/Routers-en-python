
from fastapi import FastAPI, HTTPException, status
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class User(BaseModel):
    id: int
    Name: str
    LastName: str
    Age: int


users_list = [User(id=0, Name="Alfredo", LastName="Garcia", Age="30"),
              User(id=1, Name="Juan", LastName="Perez", Age="45"),
              User(id=2, Name="María", LastName="Lopez", Age="22")]


@router.get("/alumnos_G")
async def alumnos_G():
    return (users_list)


@router.post("/alumnos_G", response_model=User, status_code=status.HTTP_201_CREATED)
async def alumnos_G(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="el usuario ya existe")
    else:
        users_list.append(user)
        return user


@router.put("/alumnos_G")
async def alumnos_G(user: User):

    found = False  # Usamos bandera found para verificar si hemos encontrado el usuario

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:  # Si el Id del usuario guardado es igual al Id del usuario nuevo
            # accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}
    else:
        return user


@router.delete("/alumnos_G/{id}")
async def alumnos_G(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
            return "El registro se ha eliminado"

    if not found:
        return {"error": "No se ha eliminado el usuario"}
