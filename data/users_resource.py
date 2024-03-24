import flask
from . import db_session
from flask_restful import reqparse, abort, Api, Resource
from data.users import User
from data.jobs import Jobs



def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"user {user_id} not found")


class UserResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return flask.jsonify({'user': user.to_dict(only=('name', 'surname', 'age', 'position', 'speciality', 'address', 'email'))})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return flask.jsonify({'success': 'OK'})

    def put(self, user_id):
        abort_if_user_not_found(user_id)
        args = parser.parse_args()
        if not flask.request.json:
            abort(404, message=f"Empty request")

        required_columns = ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'city_from',
                            'password']
        if not all(key in flask.request.json for key in required_columns):
            abort(400, message=f"Bad request")

        session = db_session.create_session()
        user = session.query(User).get(user_id)

        user.surname=args['surname']
        user.name=args['name']
        user.age=args['age']
        user.position=args['position']
        user.speciality=args['speciality']
        user.address=args['address']
        user.email=args['email']
        user.city_from=args['city_from']

        user.set_password(args['password'])

        session.add(user)
        session.commit()
        return flask.jsonify({'id': user.id})

parser = reqparse.RequestParser()
parser.add_argument('surname', required=True)
parser.add_argument('name', required=True)
parser.add_argument('age', required=True, type=int)
parser.add_argument('position', required=True)
parser.add_argument('speciality', required=True)
parser.add_argument('address', required=True)
parser.add_argument('email', required=True)
parser.add_argument('city_from', required=True)
parser.add_argument('password', required=True)

class UserListResource(Resource):
    def get(self):
        session = db_session.create_session()
        user = session.query(User).all()
        return flask.jsonify({'users': [item.to_dict(only=('name', 'surname', 'age', 'position', 'speciality', 'address', 'email', 'city_from')) for item in user]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()

        if not flask.request.json:
            abort(404, message=f"Empty request")

        required_columns = ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'city_from',
                            'password']
        if not all(key in flask.request.json for key in required_columns):
            abort(400, message=f"Bad request")

        user = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            city_from=args['city_from']
        )

        user.set_password(args['password'])

        session.add(user)
        session.commit()
        return flask.jsonify({'id': user.id})
