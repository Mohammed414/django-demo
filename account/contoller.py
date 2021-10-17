from ninja import Router, Schema

acount_contoller = Router()

users = [
    {
        "Name" : "Mohammed",
        "Age" : 21
    },
    {
        "Name" : "Ali",
        "Age" : 31
    }
]

class UserSchema(Schema):
    name: str
    age: int

# query parameters
@acount_contoller.get('list')
def list_accounts(request, index: int):
    if index:
        return users[index]
    return users
# path parameters
@acount_contoller.get('retrieve/{index}')
def retrieve_accounts(request, index: int):
    return users[index]

@acount_contoller.post('')
def create_account(request, account_in: UserSchema):
    return account_in.dict()