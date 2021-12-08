from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import request
import json

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

tasks = [
    {
        'id': 1,
        'text': "Doctor appointment",
        'reminder': True,
      },
      {
        'id': 2,
        'text': "Lawyer appointment",
        'reminder': False,
      },
      {
        'id': 3,
        'text': "Interview",
        'reminder': False,
      },
]

@app.route("/gettasks")
def getTasks():
    return jsonify(tasks)

@app.route("/addtask", methods = ['POST'])
def addTask():
    try:
        data = json.loads(request.data)
        tasks.append(data['task'])
        return jsonify(tasks)
    except:
        return jsonify(False)

@app.route("/deletetask", methods = ['POST'])
def deleteTask():
    try:
        data = json.loads(request.data)
        id = data['id']
        deleteIndex = -1
        for i in range(len(tasks)):
            if(tasks[i]['id'] == id):
                deleteIndex = i        
        if(deleteIndex != -1):
            tasks.pop(deleteIndex)
        return jsonify(tasks)
    except:
        return jsonify(False)

@app.route("/togglereminder", methods = ['POST'])
def toggleRemainder():
    try:
        data = json.loads(request.data)
        id = data['id']
        for i in range(len(tasks)):
            if(tasks[i]['id'] == id):
                tasks[i]['reminder'] = not tasks[i]['reminder']        
        return jsonify(tasks)
    except:
        return jsonify(False)


if __name__ == '__main__':
   app.run('0.0.0.0',5000)