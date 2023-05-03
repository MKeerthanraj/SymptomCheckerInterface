from flask import Flask, request, jsonify, after_this_request
from predict import predictDisease
from predict import getSymptomList

# Run "python app.py" to run flask API

app = Flask(__name__)

@app.route("/",methods=['GET'])
def hello():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    jsonResp = {'msg': "hello"}
    return jsonify(jsonResp)

@app.route("/predict",methods=["GET"])
def predict():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    symptoms = request.args.get('symptoms')
    symptoms=symptoms.replace('_',' ').title()
    prediction = predictDisease(symptoms)
    jsonResp = {'symptoms': prediction}
    return jsonify(jsonResp)

@app.route("/symptoms",methods=["GET"])
def symptoms():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    symptomsList = getSymptomList()
    return jsonify(symptomsList)

if __name__ == '__main__':
    app.run(host='localhost', port=6969)