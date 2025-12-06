from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('InterviewTable')

@app.route("/")
def home():
    return "API Working from Private Subnet!"

@app.route("/item", methods=["POST"])
def put_item():
    data = request.get_json()
    table.put_item(Item=data)
    return {"id": data["id"], "status": "ok"}

@app.route("/item/<id>")
def get_item(id):
    res = table.get_item(Key={"id": id})
    return res.get("Item", {"error": "not found"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
