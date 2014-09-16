from flask import Flask
from flask.ext import restful
import os, json

app = Flask(__name__)
api = restful.Api(app)

class PatientRecords(restful.Resource):
    def get(self):
        """
        Get the patient record
        :return:
        """
        data = json.load(open('data.json'))     # load the data
        return data

# API endpoints
api.add_resource(PatientRecords, '/')


if __name__ == '__main__':
    app.run(debug=True)