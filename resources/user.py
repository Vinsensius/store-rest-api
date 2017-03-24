import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class User:
	def __init__(self, _id, username, password):
		self.id = _id
		self.username = username
		self.password = password

class UserRegister(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument("username",
		type = str,
		required = True,
		help = "This field can't be blank."
	)
	parser.add_argument("password",
		type = str,
		required = True,
		help = "This field can't be blank."			
	)

	def post(self):
		data = UserRegister.parser.parse_args()

		if UserModel.find_by_username(data['username']):
			return {"message" : "A user with that username already exists"}, 400

		user = UserModel(**data)
		user.save_to_db()

		return {"message" : "User created successfully."}, 201 

