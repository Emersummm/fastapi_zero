from enum import Enum
from typing import Dict, List, Optional

from fastapi import BackgroundTasks, FastAPI, HTTPException, Path, Query
from pydantic import BaseModel


class ItemType(str, Enum):
    book = 'book'
    gadget = 'gadget'
    tool = 'tool'


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tags: List[str] = []
    type: ItemType = ItemType.tool
    in_stock: bool = True


app = FastAPI(title='FastAPI Maneiro', version='0.1.0')


db: Dict[int, Item] = {
    1: Item(
        name='Caneca',
        description='Caneca térmica preta',
        price=39.90,
        tags=['quente', 'café'],
        type=ItemType.gadget,
    ),
    2: Item(
        name='Caderno',
        description='Caderno de anotações',
        price=24.50,
        tags=['papelaria'],
        type=ItemType.book,
    ),
}


def notify_new_item(item_id: int, item: Item):
    print(f'Novo item cadastrado: {item_id} - {item.name}')


@app.get('/')
def read_root():
    return {'message': 'Olá! Acesse /items para testar o CRUD'}


@app.get('/items')
def list_items(
    item_type: Optional[ItemType] = Query(None),
    limit: int = Query(10, ge=1, le=50),
):
    items = [
        item.dict()
        for item in db.values()
        if item_type is None or item.type == item_type
    ]
    return {'count': len(items), 'items': items[:limit]}


@app.get('/items/{item_id}')
def read_item(
    item_id: int = Path(..., ge=1),
    q: Optional[str] = Query(None, max_length=50),
):
    item = db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail='Item não encontrado')
    result = item.dict()
    if q:
        result['q'] = q
    return result


@app.post('/items', status_code=201)
def create_item(item: Item, background_tasks: BackgroundTasks):
    item_id = max(db.keys(), default=0) + 1
    db[item_id] = item
    background_tasks.add_task(notify_new_item, item_id, item)
    return {'item_id': item_id, 'item': item}


@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    if item_id not in db:
        raise HTTPException(status_code=404, detail='Item não encontrado')
    db[item_id] = item
    return {'item_id': item_id, 'item': item}
