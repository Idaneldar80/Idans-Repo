from flask import Flask,request

app = Flask(__name__)

users = [
    {"id": 1, "username": "hodi", "password": "123", "salary": 5000, "address": "123Main St", "active": True},
    {"id": 2, "username": "josh", "password": "456", "salary": 60000, "address": "456 Oak St","active": True}
    ]


@app.get('/hello')
def greet():
    return {"message":"hello"}

@app.get('/users')
def get_all_users():
    # active_users=[]
    # for user in users:
    #     if user['active']:
    #         active_users.append(user)
    # return active_users
 
    return [user for user in users if user['active']] # return all the active users

@app.get('/users/<int:user_id>') # all the get http requests with id as int will run this function
def get_user_by_id(user_id):
    for user in users: # run over all the users
        if user['id'] == user_id: # if the user id found return the user
            return user
    
    return{"error":"User not found"},404 # if the user_id doesnt exist return 404 status code 

@app.post('/users')
def add_user():
    new_user = request.json # get data from postman or any other client that
    new_user['id'] = users[-1]['id']+1  # assign valid id
    users.append(new_user) # add the new user to the users list
    return {"message":"created"},201

@app.put('/users/<int:user_id>')
def update_user(user_id):
    updated_user= request.json # get the json from the body of the request
    updated_user['id']= user_id # override the user id
    for user in users: 
        if user["id"]==user_id: # if the user id == the user_id
            users.remove(user) # delete the old user
            users.append(updated_user)  # add the updated user
    
    return{"message"}

@app.delete('/users')
def delete_all():
    users.clear()
    return {"message":"Done"}

@app.delete('/users/<int:user_id>')
def delete_by_id(user_id):
    for user in users:
        if user.get('id')== user_id:
            users.remove(user) # replace the users with new list of userts that dont have the same id as the user_id param  TODO: [user for user in users if user['id']!= user_id ] 
    
    return {"message":"Done"}
app.run(use_reloader=True) # port 5000 host = localhost@@@