from fastapi import FastAPI
from setup_db import setup_db
import sqlite3
from pydantic import BaseModel

connection = sqlite3.connect("server_db.db")

cursor = connection.cursor()


setup_db()


class Item(BaseModel):
    id: int
    name: str
    description: str


def convert_query_to_model(query_data):
    items = []
    for item in query_data:
        items.append(Item(id=item[0], name=item[1], description=item[2]))
    return items


app = FastAPI()


@app.get('/items')
async def get_todo():
    data = cursor.execute("select * from items")
    data = data.fetchall()
    data = convert_query_to_model(data)
    return data
