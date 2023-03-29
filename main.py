from fastapi import FastAPI
from typing import List,Optional
from uuid import uuid4
from enum import Enum
from models import User, Gender, Role

app = FastAPI()

db: List[User]= [User(
    id= uuid4(), 
    first_name='Keziah',
    last_name= 'Njeri',
    gender = Gender.female,
    roles = Role.admin),
User(
    id = uuid4(),
    first_name= 'Shelly',
    last_name= 'Anne',
    middle_name = 'Gilberts',
    gender = Gender.female,
    roles  = Role.user
    )]            
  
@app.get('/')
async def index():
    return {'Hello':'World'}


@app.get('/api/v1/users')
async def fetch_users():
    return db;
@app.post('/api/v1/users')
async def new_user(user :User):
    db.append(user)
    return {'id': user.id}