from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData, functionName):
    if(functionName == "add" or functionName == "subtract" or functionName== "multiply" ):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200
    elif(functionName == "divide"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        elif int(postedData["y"])==0:
            return 302
        else:
                return 200

class Add(Resource):
    def post(self):
        #if im here, then the resource add was requested using POST

        #step1: Get posted data
        postedData = request.get_json()
        #step1b; verify the validity of the posted data
        status_code = checkPostedData(postedData, "add")
        if (status_code != 200):
            retJson = {
                "Message": "ERROR!: Missing Parameter(s)",
                "Status Code": status_code
            }
            return jsonify(retJson)
        #if im here, posted data = 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        #step2: add the posted data
        ret = x+y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)



class Subtract(Resource):
    def post(self):

        #if im here, then the resource subtract was requested using POST
        postedData = request.get_json()

        #step1: Get posted data
        status_code = checkPostedData(postedData, "subtract")
        if (status_code != 200):
            retJson = {
                "Message": "ERROR!: Missing Parameter(s)",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        ret = x-y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

class Multiply(Resource):
    def post(self):
    
        postedData = request.get_json()

        status_code = checkPostedData(postedData, "multiply")
        if (status_code != 200):
            retJson = {
                "Message": "ERROR!: Missing Parameter(s)",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        ret = x*y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

class Divide(Resource):
    def post(self):
    
        postedData = request.get_json()

        status_code = checkPostedData(postedData, "divide")
        if (status_code != 200):
            retJson = {
                "Message": "ERROR!: Missing Parameter(s)",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        ret = x/y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)


api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")