from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


#path operator decorator
@app.get('/')
#path operation function
def index():
   return 'hey himanshu'

@app.get('/blog')
#here limit and published are query parameters
def index(limit:int=20, published : bool =False, sort:Optional[str]=None):
    if published:
        return {'data':f'{limit} published blocks'}
    return {'data':f'{limit} blog from server'}

@app.get('/blog/{id}/comment')
def comments(id:int):
    return {'data':{'1','2'}}
#here id is path parameter
@app.get('/blog/{id}')
def show(id : int):
    return {'data':id}

@app.get('/about')
def about():
    return 'it is about page'


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    

@app.post('/blog')
def create_blog(request: Blog):
    return {'data':f'blog is created with {request.title} \
        and body {request.body}'}


# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1",port=9000)





