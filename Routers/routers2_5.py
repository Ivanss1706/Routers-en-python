from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router = APIRouter()


class User(BaseModel):
    id: int
    Name: str
    LastName: str
    Age: int


# Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)
users_list = [User(id=0, Name="Alfredo", LastName="Garcia", Age="30"),
              User(id=1, Name="Juan", LastName="Perez", Age="45"),
              User(id=2, Name="María", LastName="Lopez", Age="22")]


# ***Get
@router.get("/usersclass/")
async def usersclass():
    return (users_list)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/


# ***Get con Filtro Path
@router.get("/usersclass/{id}")
async def usersclass(id: int):
    # Función de orden superior
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

     # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/1


# ***Get con Filtro Query
@router.get("/usersclass/")
async def usersclass(id: int):
    # Función de orden superior
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/?id=1


# ***Post
@router.post("/usersclass/")
async def usersclass(user: User):

    found = False  # Usamos bandera found para verificar si hemos encontrado el usuario

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:  # Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error": "el usuario ya existe"}
    else:
        users_list.append(user)
        return user

    # http://127.0.0.1:8000/usersclass/

    # ***Put


@router.put("/usersclass/")
async def usersclass(user: User):

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

    # http://127.0.0.1:8000/usersclass/

        # ***Delete


@router.delete("/usersclass/{id}")
async def usersclass(id: int):

    found = False  # Usamos bandera found para verificar si hemos encontrado el usuario

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:  # Si el Id del usuario guardado es igual al Id del usuario nuevo
            # Eliminamos al indice de la lista que hemos encontrado
            del users_list[index]
            found = True
            return "El registro se ha eliminado"

    if not found:
        return {"error": "No se ha eliminado el usuario"}

    # http://127.0.0.1:8000/usersclass/1
