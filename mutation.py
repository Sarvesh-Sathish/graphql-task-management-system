from graphene import ObjectType, Mutation, String, Field
from models import User
from database import users

class CreateUser(Mutation):
    class Arguments:
        email = String()
        password = String()
        
    user = Field(lambda: User)
       
    def mutate(self, info, email, password):
        user = {'email': email, 'password': password}
        users.append(user)
        return CreateUser(user=user)
    

class Mutation(ObjectType):
    create_user = CreateUser.Field() #? Mutation probably has a .field() parameter