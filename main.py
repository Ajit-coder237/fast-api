from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get('/')
def firstFunction():
     obj = {'message': 'Hello World',
            'number': 1,
            'valid': True,
            'value': None
            }
     return obj['message']

class Blog(BaseModel):
     title: str = "Hello this is Madhu Ajit Pandey, CEO of the TechVedic"
     body: str
     published: Optional[bool]=None

@app.post('/blog')
async def create_blog(blog: Blog):
     return {'data': f"Blog is created with title as {blog.title}"}
 # @app.get('/blog?limit=10&published=true')
@app.get('/blog')

async def index(limit=10, published: bool = True, sort: Optional[str] = None):
    #only get 10 published blogs
    # return published
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
async def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')

async def show(id: int):
    #fetch blog with id = id
        return {'data' : id}    


@app.get('/blog/{id}/comments')
async def comments(id):
      #fetch comments of blog id = id
      return {'data': {'1', '2'}}