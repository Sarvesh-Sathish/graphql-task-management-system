from graphene import String, ObjectType

class User(ObjectType):
    email = String()
    password = String()
