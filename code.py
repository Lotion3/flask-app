from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[
    {
        "Contact":1984393923,
        "Name":"Joe",
        "done":"false",
        "id":1
    },
    {
        "Contact":1874397233,
        "Name":"asd",
        "done":"false",
        "id":2
    }
]
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide data"
        },400)
    task={
        "id":tasks[-1]["id"]+1,
        "Name":request.json["title"],
        "Contact":request.json.get("description",""),
        "done":False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task added succssesfully"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
@app.route("/")
def test():
    return "Test"
app.run()