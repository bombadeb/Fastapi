from turtle import title
import types
from urllib import response
import uvicorn
from fastapi import Depends, FastAPI, Response, status
from pydantic import BaseModel
import models, schemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()
models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/liveeo')
def create(request: schemas.Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(types=request.types,grid_file=request.grid_file,pole_file=request.pole_file,critical_distances=request.critical_distances)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog.id

@app.get('/liveeo')
def all(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/liveeo/{id}', status_code=200)
def show(id, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
    return blog

@app.delete('/liveeo/{id}', status_code=200)
def destroy(id, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {'data': id,'execution': 'SUCCESS'}


if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)