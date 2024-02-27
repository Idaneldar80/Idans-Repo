from flask import Flask

app = Flask(__name__)

users = [ {"id": 1, "username": "hodi", "password": "123", "salary": 5000, "address": "123Main St", "active": True},
          {"id": 2, "username": "josh", "password": "456", "salary": 60000, "address": "456 Oak St", "active": False}
         ]

@app.get('/hello')
def greet():
    return "Hello"


@app.get('/users')
def get_all_users():
    return users

@app.get('/users/<int:user_id>')
def get_user_by_id(user_id):
    for user in users:
        if user['id'] == user_id:
            return user
    return{"error":"User not found"},400


app.run(use_reloader=True)