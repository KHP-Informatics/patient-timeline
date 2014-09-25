from flask import Flask
from flask.ext import restful
import json, datetime
from datetime import timedelta
from functools import update_wrapper

app = Flask(__name__)
api = restful.Api(app)

# config
database = json.load(open('data.json'))
date_fmt = '%Y-%m-%d'


def reindex(data=database, key='patient_id', primary_key=True):
    """
    Given the database index first by id then by data for use by the frontend
    :return:
    """
    if primary_key:
        indexed = {}
    else:
        indexed = []

    for record in data:
        record = dict(record)

        if primary_key:
            if record[key] not in indexed.keys():
                indexed[record[key]] = []

            indexed[record[key]].append({'date': record['date'], "element": [record]}) # hack this should be all records!
        else:
            indexed.append({'date': record['date'], "element": [record]})

    return indexed

class PatientRecords(restful.Resource):
    def get(self):
        """
        Get the patient record
        :return:
        """
        return reindex(database)

class PatientID(restful.Resource):
    def get(self, patient_id, start_date=None, end_date=None):
        """
        Given a patient ID, check the records and append records that match the
        patient id
        :param patient_id:
        :return:
        """
        # start_date = False
        # end_date = False

        response = []
        for record in database:
            record = dict(record)
            if int(record['patient_id']) == patient_id:

                if start_date:
                    # convert start_date and the date in the record to a
                    # python datetime
                    start = datetime.datetime.strptime(start_date, date_fmt)
                    record_date = datetime.datetime.strptime(record['date'], date_fmt)

                    if record_date > start:
                        response.append(record)

                elif start_date and end_date:
                    start = datetime.datetime.strptime(start_date, date_fmt)
                    end = datetime.datetime.strptime(end_date, date_fmt)
                    record_date = datetime.datetime.strptime(record['date'], date_fmt)

                    if start > record_date < end:
                        response.append(record)

                else:
                    response.append(record)

        return sorted(reindex(response, 'date', False), key=lambda x: x['date'])



# API endpoints
api.add_resource(PatientRecords, '/')
api.add_resource(PatientID,
                 '/patient/<int:patient_id>/',
                 '/patient/<int:patient_id>/<string:start_date>/',
                 '/patient/<int:patient_id>/<string:start_date>/<string:end_date>/',
                 )


if __name__ == '__main__':
    app.run(debug=True)
