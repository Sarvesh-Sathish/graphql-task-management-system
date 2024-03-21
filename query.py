from graphene import ObjectType, String, List, Field
from models import User
from database import users

class Query(ObjectType):
    user = Field(User, email=String())
    
    def resolve_user(root, info, email):
        for user in users:
            if user['email'] == email:
                return user
            
        return None
    
    def resolve_users(root, info):
        return users