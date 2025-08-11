from fastapi import (FastAPI,WebSocket,Cookie,Query,WebSocketException,Depends,status)   
from enum import Enum
from typing import Annotated


class ModelName(str,Enum):
    batman='batman123'
    superman='superman'
    spiderman='spiderman'


app= FastAPI()

@app.get('/')
async def root():
    return {"message":"Hello world"}


@app.get('/items/{item_id}')
async  def read_item(item_id:int):
    return {"item_id":item_id}


@app.get('/users/{user_id}')
async def read_user(user_id:str):
    return {'user_id':user_id}

@app.get('/users/me')
async def read_user_me():
    return {'user_id':"the current user is me"}


@app.get('/hero/{hero_name}')
async def get_hero_name(hero_name:ModelName):
    if hero_name is ModelName.batman:
        return {"hero_dialogue":f'I am batman {hero_name}'}
    elif hero_name is ModelName.superman:
        return {'hero_dialogue':"I'm human"}
    elif hero_name is ModelName.spiderman:
        return {"hero_dialogue":"I'm spiderman"}
    

class Sex(str,Enum):
    male='male'
    female='female'

@app.get("/heros/{name}")
async def get_hero(name:str,sex:Sex=Sex.male,age:int=18):
    if sex in [Sex.male,Sex.female]:
        return {"name":name,"age":age,"sex":sex}
    else:
        return {"name":name,"age":age,"sex":"unknown"}
    



@app.websocket('/ws')
async def websocket_endpoint(websocket:WebSocket):
    await websocket.accept()
    while True:
        data=await websocket.receive_text()
        await websocket.send_text(f"Message received: {data} from {websocket.client}")



async def get_cookie_or_token(websocket:WebSocket,session:Annotated[str|None,Cookie()]=None,token: Annotated[str | None, Query()]= None,):
    if session is None and token is None:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    return session or token 

