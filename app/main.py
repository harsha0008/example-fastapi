from fastapi import FastAPI, Response, status, HTTPException, Depends
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from typing import List
from . import models
from .database import engine, get_db
from .routers import post,user,auth,vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://www.google.com",
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


####Created now by alembic
####Umcomment if you want to create here in case of no alembic
#models.Base.metadata.create_all(bind=engine)

########   CODE for connecting to database  for running direct SQL commands

# while True:
#     try:
#         conn=psycopg2.connect(host='localhost', database = 'myfastapi', user='postgres',
#                             password='pabsys-sijFer-7xipju', cursor_factory=RealDictCursor)
#         cursor=conn.cursor()
#         print("Database connection sucessfull!")
#         break
#     except Exception as error:
#         print('Connection to database failed')
#         print("Error: ", error)
#         time.sleep(2)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"Hello": "Welcome to my API!!"}


#####CODDE for using SQL commands

# @app.get("/posts")
# def get_posts():
#     cursor.execute("""SELECT * from post""")
#     posts = cursor.fetchall()
#     return posts

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(post: schemas.PostCreate):
#     cursor.execute("""INSERT INTO post (title, content, published) VALUES (%s, %s, %s) returning * """,(post.title, post.content, post.published))
#     new_post = cursor.fetchone()
#     conn.commit()
#     return new_post

# @app.get("/posts/{id}")
# def get_post(id: int):
#     cursor.execute("""SELECT * from post WHERE id = %s""",(id,))
#     post = cursor.fetchone()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id {id} was not found")
#     return post

# @app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     cursor.execute("""DELETE FROM post WHERE id = %s returning *""",(id,))
#     deleted_post = cursor.fetchone()
#     conn.commit()
#     if deleted_post == None:
#          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                              detail=f"post with id {id} does not exist")
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put("/posts/{id}")
# def update_post(id: int, post: schemas.PostCreate):
#     cursor.execute("""UPDATE post SET title=%s, content=%s, published=%s WHERE id = %s RETURNING *""",(post.title,post.content,post.published,id))
#     updated_post=cursor.fetchone()
#     conn.commit()
#     if updated_post == None:
#          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                              detail=f"post with id {id} does not exist")
#     return updated_post




