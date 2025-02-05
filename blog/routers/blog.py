from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from ..oauth import get_current_user




router = APIRouter(prefix='/blog',tags=['blogs'])
get_db = database.get_db

@router.get('/', response_model= List[schemas.ShowBlog])
def all(db:Session= Depends(database.get_db),current_user:schemas.User = Depends(get_current_user)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db:Session= Depends(get_db)):
    new_blog = models.Blog(title=request.title,body=request.body, user_id=1) #hardcoded
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id, response:Response ,db:Session= Depends(get_db),get_current_user:schemas.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,\
            detail=f"blog with {id} is not available")
        # response.status_code= status.HTTP_404_NOT_FOUND
        # return {'detail':f"blog with {id} is not available"}
    return blog


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destory(id, db:Session= Depends(get_db)):
    # db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first(): 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details=f"blog with {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'
        
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED )
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first(): 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details=f"blog with {id} not found")
    blog.update(request)
    db.commit()
    return 'updated'
