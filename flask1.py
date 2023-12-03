from flask import Flask, jsonify, request 

app = Flask(__name__)
contacts = [
    {
    "Contact":"9987644456",
    "Name":"Raju",
    "done": False,
    "id":1
},
{
    "Contact":"9876543222",
    "Name":"Rahul",
    "done": False,
    "id":2
}]
@app.route("/pizza")
def food():
    return("my favorite food is pizza")


@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data!"
        },400)
    contact = {
        'id': contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact',""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status":"successful",
        "message":"Task added successfully"
    })

@app.route("/piano")
def music():
    return("I like playing Piano.")



app.run(debug=True)