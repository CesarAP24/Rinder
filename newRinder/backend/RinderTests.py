import unittest  # libreria de python para realizar test
from config.qa import config
from app.models import *
from app import create_app
from flask_sqlalchemy import SQLAlchemy
import json
import random

def random_mail():
	random_number = random.randint(0, 100000)
	return "test" + str(random_number) + "@test.com"

class RinderTests(unittest.TestCase):
	def setUp(self):
		database_path = config["DATABASE_URI"]
		self.app = create_app({'database_path': database_path})
		self.client = self.app.test_client()

		self.copy_user = {
			"password": "copy",
			"email": "copy@test.com"
			}

		self.not_found_user = {
			"password": "not_found",
			"email": "not_found@not_fount.com"
			}
	

	# POSTS TESTS =====================================================================================================

	# user ------------------------------------------------------------------------------------------------------------

	def test_create_user(self):
		new_user = {
			"password": "test",
			"email": lambda: random_mail()
		}
		response = self.client.post('/users', json=new_user)
		data = json.loads(response.data)

		self.assertEqual(response.status_code, 201)
		self.assertEqual(data['success'], True)
		self.assertTrue(data['user'])
		self.assertTrue(data['access_token'])

	def test_create_user_no_data(self):
		response = self.client.post('/users', json={})
		data = json.loads(response.data)

		self.assertEqual(response.status_code, 400)
		self.assertEqual(data['success'], False)
	
	def test_create_user_incomplete_data(self):
		response = self.client.post('/users', json={"username": "test"})
		data = json.loads(response.data)

		self.assertEqual(response.status_code, 400)
		self.assertEqual(data['success'], False)

	def test_create_user_already_exists(self):
		#crear un usuario q no existe
		response_1 = self.client.post('/users', json=self.copy_user)
		data_1 = json.loads(response_1.data)

		#crear un usuario q ya existe
		response_2 = self.client.post('/users', json=self.copy_user)
		data_2 = json.loads(response_2.data)

		self.assertEqual(response_2.status_code, 409)
		self.assertEqual(data_1['success'], True)
		self.assertEqual(data_2['success'], False)

	# mensaje ---------------------------------------------------------------------------------------------------------



	# API ROUTES ======================================================================================================

	# api/login test ------------------------------------------------------------------------------------------------------

	def test_login_success(self):
		new_user = {
			'email': random_mail(),
			'password': 'test'
		}
		response = self.client.post('/users', json=new_user)

		login_user = {
			"email": new_user['email'],
			"password": new_user['password']
		}

		response = self.client.post('/api/login', json=login_user)
		data = json.loads(response.data)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(data['success'], True)
		self.assertTrue(data['access_token']) #el token es con jwt

	def test_login_no_data(self):
		response = self.client.post('/api/login', json={})
		data = json.loads(response.data)

		self.assertEqual(response.status_code, 400)
		self.assertEqual(data['success'], False)

	def test_login_incomplete_data(self):
		response = self.client.post('/api/login', json={"email": "test"})
		data = json.loads(response.data)

		self.assertEqual(response.status_code, 400)
		self.assertEqual(data['success'], False)
		self.assertTrue(data['errors'])

	def test_login_wrong_password(self):
		usuario = {
			'email': random_mail(),
			'password': 'test'
		}

		new_user = self.client.post('/users', json=usuario)

		login_user = {
			"email": usuario['email'],
			"password": "wrong_password"
		}

		response = self.client.post('/api/login', json=login_user)
		data = json.loads(response.data)

		self.assertEqual(response.status_code, 401)
		self.assertEqual(data['success'], False)


	def test_login_user_not_exists(self):
		response = self.client.post('/api/login', json=self.not_found_user)
		data = json.loads(response.data)

		self.assertEqual(response.status_code, 404)
		self.assertEqual(data['success'], False)
		self.assertTrue(data['errors'])



# post:
# - Usuario
# - Mensaje
# - suscripciones
# - chat
# - compra
# - likeaPerfil

# get:
# - mensajes
# - chats
# - perfil
# - sucrpciones
# - compra

# patch:
# - perfil
# - usuario
# - compra

# delete:
# - usuario
# - suscripciones

