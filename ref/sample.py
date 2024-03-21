
from graphene import ObjectType, String, Schema

# ---------------------------------------------------------------------------- #
#                               Query type class                               #
# ---------------------------------------------------------------------------- #

class Query(ObjectType):
    hello = String(firstName=String(default_value="stranger"))
    goodbye = String()
    
    def resolve_hello(root, info, firstName):
        return f'Hello {firstName}!'
    
    def resolve_goodbye(root, info):
        return "Goodbye!"
    
schema = Schema(query=Query)
print('This is the schema below \n', schema) # returns the type with the hello and goodbye variable

# ---------------------------------- Query 1 --------------------------------- #
query_1 = '{ hello }' # this query is in the format of a string
result_1 = schema.execute(query_1)
print('This is the result of query1 \n',result_1.data) # returns the result of the query 

# ---------------------------------- Query 2 --------------------------------- #
query_2 = '''
    {
        hello(firstName: "tarunesh")
    }
'''

result_2 = schema.execute(query_2)
print('This is the result of query2 \n', result_2.data)

```