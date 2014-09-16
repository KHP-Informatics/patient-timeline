from flask import Flask
from flask.ext import restful
import json

app = Flask(__name__)
api = restful.Api(app)

database = json.load(open('data.json'))

class PatientRecords(restful.Resource):
    def get(self):
        """
        Get the patient record
        :return:
        """
        return database

class PatientID(restful.Resource):
    def get(self, patient_id):
        """
        Given a patient ID, check the records and append records that match the
        patient id
        :param patient_id:
        :return:
        """
        response = []
        for record in database:
            record = dict(record)
            if record['patient_id'] == patient_id:
                response.append(record)

        return json.dumps(response)

# API endpoints
api.add_resource(PatientRecords, '/')
api.add_resource(PatientID, '/patient/<int:patient_id>/')


if __name__ == '__main__':
    app.run(debug=True)