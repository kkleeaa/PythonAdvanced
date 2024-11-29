import sqlite3

from typing import List

from streamlit import status

from ..models.category import CategoryBase, Category

from database import get_db_connection

from fastapi import APIRouter, HTTPException





router = APIRouter()





@router.get("/categories/", response_model=List[Category])

def get_categories():

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute("Select if, name from categories")

    categories = cursor.fetchall()

    conn.close()

    category_list = [{"id": cat[0], "name": cat[1]} for cat in categories]

    return category_list
@router.post("/categories", response_model=category)
def create_category(category:CategoryCreate):
    conn= get_db_connection()
    cursor= conn.cursor()
    try:
        cursor.execute("inset into categories (name) values (?)",(category.name))
        conn.commit()
        category_id= cursor.lastrowid
        return category(id=category_id, name= category.name)
    
