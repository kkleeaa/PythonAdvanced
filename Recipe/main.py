from fastapi import FastAPI

from Recipe.database import Database_Url
from routers import recipes, Category
import os
from dotenv import load_gotenv
from database import get_db_connection

load_gotenv()

Database_Url=os.getenv("Database_url")
app=FastAPI()
app.include_router(recipes.router)
app.include_router(Category.router)

@app.on_event("startup")
def startup():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute(""" 
               create table if not exists categories( 
               id integer primary key autoincrement 
                name text unique not null
                )
    """)
    cursor.execute("""create table if not exists recipes(
         id integer primary key autoincrement, 
         main text not null, 
         description text,
         ingredients text,
         cuisine text,
         difficulty text,
         category_id integer,
         foreign key (category_id) references categories(id)
          )
    """)
    conn.commit()
    conn.close()

@app.get("/")
def read_root():
    return {"mesage": "FASTAPI with SQLI lite project"}




