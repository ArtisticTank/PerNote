from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from notes import Notes
import json
from user import User

app = Flask(__name__)
#api = Api(app)

dummyUser = User("s;dgfh", "this@lol", "thisisshit", "lol@gmail.com", "Shitty", "Sartaj")
users = {
    "lol@gmail.com" : dummyUser
}

n1 = Notes("12345", "shit", "lol", "this","shit")
notes = {
    "12345" : n1
}

@app.route("/login", methods = ['POST'])
def loginController():
    if request.method == 'POST':
        req_data = request.json
        mailId = req_data.get("mailId")
        password = req_data.get("password")

        if mailId == None :
            return "Mail Id is empty"

        elif users[mailId] == None :
            return "Your account does not exist, maybe you need to create an account first"
        
        else : 
            if users[mailId].password == password:
                return users[mailId].userId
            else :
                return "You've entered wrong password"


@app.route("/user", methods = ['POST', 'GET'])
def userController():
    
    if request.method == 'GET':
        mailId = request.args.get('mailId')
        if mailId in users.keys():
            app_json = json.dumps(users[mailId].__dict__)
            return app_json
        return "User does not exists!"
        
    
    if request.method == 'POST':
        req_data = request.json
        userId = req_data.get("userId")
        userName = req_data.get("userName")
        firstName = req_data.get("firstName")
        lastName = req_data.get("lastName")
        mailId = req_data.get("mailId")
        password = req_data.get("password")

        print(userId)
        user = User(userId, userName, password, mailId, firstName, lastName)
        if mailId in users.keys():
            return "Username already registered"
        elif mailId == None:
            return "Mail Id is empty"
        users[mailId] = user
        return json.dumps(users[mailId].__dict__)
        #print(p1)
        

@app.route("/notes", methods = ['GET','POST'])
def notesController():
    if request.method == 'GET':
        userId = request.args.get('userId')
        app_json = json.dumps(notes[userId].__dict__)
        #temp = [notes[userId]]
        #app_json = json.dumps(temp.__dict__)
        return app_json

    elif request.method == 'POST':
        req_data = request.json
        userId = req_data.get("userId")
        userName = req_data.get("userName")
        createdOn = req_data.get("createdOn")
        title = req_data.get("title")
        note = req_data.get("note")

        print(userId)
        p1 = Notes(userId, userName, createdOn, title, note)
        print(p1)
        notes[userId] = p1
        return json.dumps(notes[userId].__dict__)

#api.add_resource(NotesController, '/notes', '/notes/<userId>')        

if __name__ == '__main__':
    app.run(host='192.168.1.10', debug=True)