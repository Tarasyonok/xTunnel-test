import flask
from . import db_session
from flask_restful import reqparse, abort, Api, Resource
from data.jobs import Jobs
from data.users import User



def abort_if_job_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"job {job_id} not found")


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        return flask.jsonify({'job': job.to_dict(only=('team_leader', 'job', 'work_size', 'collaborators', 'is_finished'))})

    def delete(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return flask.jsonify({'success': 'OK'})

    def put(self, job_id):
        abort_if_job_not_found(job_id)
        args = parser.parse_args()
        if not flask.request.json:
            abort(404, message=f"Empty request")

        required_columns = ['team_leader', 'job', 'work_size', 'collaborators', 'is_finished']
        if not all(key in flask.request.json for key in required_columns):
            abort(400, message=f"Bad request")

        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)

        job.team_leader=args['team_leader']
        job.job=args['job']
        job.work_size=args['work_size']
        job.collaborators=args['collaborators']
        job.is_finished=int(args['is_finished'])
        job.user=session.query(User).get(args['team_leader'])

        session.add(job)
        session.commit()
        return flask.jsonify({'id': job.id})

parser = reqparse.RequestParser()
parser.add_argument('team_leader', required=True, type=int)
parser.add_argument('job', required=True)
parser.add_argument('work_size', required=True, type=int)
parser.add_argument('collaborators', required=True)
parser.add_argument('is_finished', required=True, type=bool)


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        job = session.query(Jobs).all()
        return flask.jsonify({'jobs': [item.to_dict(only=('team_leader', 'job', 'work_size', 'collaborators', 'is_finished')) for item in job]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()

        if not flask.request.json:
            abort(404, message=f"Empty request")

        required_columns = ['team_leader', 'job', 'work_size', 'collaborators', 'is_finished']
        if not all(key in flask.request.json for key in required_columns):
            abort(400, message=f"Bad request")

        job = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_finished=args['is_finished'],
            user=session.query(User).get(args['team_leader'])
        )

        session.add(job)
        session.commit()
        return flask.jsonify({'id': job.id})
