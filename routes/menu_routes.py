from fastapi import APIRouter, status, HTTPException

from models.item_models import ItemModel
from utils.menu_querys import *

menu_router = APIRouter()

@menu_router.get("/menu",   status_code=status.HTTP_200_OK,
                            description= "Retorna os itens cadastrados no cardápio") #Consultar itens do cardápio
async def menu_items():
    try:
        menu_data = get_menu_items()
        return {"menu": formatted_list(menu_data)}
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"{error}"
        )
    
@menu_router.post("/menu", status_code=status.HTTP_201_CREATED) #Criar itens no cardápio
async def create_menu_item(item_data: ItemModel):
    try:
        item = get_item_by_name(item_data.item_name)
        if not item:
            create_item(
                item_data.item_name, 
                item_data.item_description, 
                item_data.item_price, 
                item_data.category_name
            )
            return {"success": f"Item: '{item_data.item_name}' foi adicionado no seu menu!"}
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"{error}"
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail=f"Já existe um produto com o nome: '{item_data.item_name}'"
        )

@menu_router.get("/menu/{item_id}", status_code=status.HTTP_200_OK) #Consultar item específico no cardápio
async def item_by_id(item_id: str):
    try:
        item = get_item_by_id(item_id)
        if item:
            return {"item": formatted_list(item)}
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"{error}"
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"O item com o id: '{item_id}' não foi encontrado."
        )

@menu_router.put("/menu/{item_id}", status_code=status.HTTP_200_OK) #Atualizar item do cardápio
async def update_item(item_id: str, item_data: ItemModel):
    try:
        item = get_item_by_id(item_id)
        if item:
            data = dict(item_data)
            new_item = update_item_by_id(item_id, data)
            return {"item": formatted_list(new_item)}
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"{error}"
        )
    else:
        create_item(
            item_data.item_name, 
            item_data.item_description, 
            item_data.item_price, 
            item_data.category_name
        )
        return {"success": f"Item: '{item_data.item_name}' foi adicionado no seu menu!"}

@menu_router.delete("/menu/{item_id}", status_code=status.HTTP_200_OK) #Deletar um item específico no cardápio
async def delete_item(item_id: str):
    try:
        item = get_item_by_id(item_id)
        if item:
            delete_item_by_id(item_id)
            return {"success": f"O item com o id: '{item_id}' foi deletado do seu menu."}
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"{error}"
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"O item com o id: '{item_id}' não foi encontrado."
        )

@menu_router.get("/categories", status_code=status.HTTP_200_OK) #Consultar categorias do cardápio
async def menu_categories():
    try:
        categories_list = get_menu_categories()
        return {"categorias": categories_list}
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"{error}"
        )
    
@menu_router.get("/categories/{category_name}/items", status_code=status.HTTP_200_OK) #Consultar itens de uma catagoria específica no cardápio
async def item_by_category(category_name: str):
    try:
        items_list = get_item_by_category(category_name)
        if items_list:
            return {f"Items de '{category_name}'": formatted_list(items_list)}
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"{error}"
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"A categoria: '{category_name}' não foi encontrada no seu menu."
        )

def formatted_list(data): # Formatação do retorno das pesquisas no banco de dados
    items_list = []
    for item in data:
        item_data = {
            "item_id": item[0],
            "item_name": item[1],
            "item_description": item[2],
            "item_price": item[3],
            "category_name": item[4]
        }
        items_list.append(item_data)
    return items_list