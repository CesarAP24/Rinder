import unittest  # libreria de python para realizar test
from app.models import db, Usuario, Mensaje, Chat, Perfil, Pertenece
from app import create_app
from flask_sqlalchemy import SQLAlchemy
import json
import random
from config.qa import config

def random_mail():
	random_number = random.randint(0, 100000)
	return "test" + str(random_number) + "@test.com"

class RinderTests(unittest.TestCase):
	def setUp(self):
		print(self)
		database_path = config["DATABASE_URI"]
		self.app = create_app({'database_path': database_path})
		self.client = self.app.test_client()

		self.copy_user = {
			"contraseña": "copy",
			"correo": "copy@test.com"
			}

		self.not_found_user = {
			"contraseña": "not_found",
			"correo": "not_found@not_fount.com"
			}
	

	# POSTS TESTS =====================================================================================================

	# user ------------------------------------------------------------------------------------------------------------

	def test_create_user_no_data(self):
		response = self.client.post('/usuarios', json={})
		data = json.loads(response.data)

		self.assertEqual(response.status_code, 400)
		self.assertEqual(data['success'], False)
	
	def test_create_user_incomplete_data(self):
		response = self.client.post('/usuarios', json={"username": "test"})
		data = json.loads(response.data)

		self.assertEqual(response.status_code, 400)
		self.assertEqual(data['success'], False)

	def test_create_user_already_exists(self):
		#crear un usuario q no existe
		response_1 = self.client.post('/usuarios', json=self.copy_user)
		data_1 = json.loads(response_1.data)

		#crear un usuario q ya existe
		response_2 = self.client.post('/usuarios', json=self.copy_user)
		data_2 = json.loads(response_2.data)

		self.assertEqual(response_2.status_code, 400)
		self.assertEqual(data_2['success'], False)

	# mensaje ---------------------------------------------------------------------------------------------------------



	# API ROUTES ======================================================================================================

	# api/login test ------------------------------------------------------------------------------------------------------


	def test_login_no_data(self):
		response = self.client.post('/api/login', json={})
		data = json.loads(response.data)

		self.assertEqual(response.status_code, 400)
		self.assertEqual(data['success'], False)

	def test_login_incomplete_data(self):
		response = self.client.post('/api/login', json={"correo": "test"})
		data = json.loads(response.data)

		self.assertEqual(response.status_code, 400)
		self.assertEqual(data['success'], False)
		self.assertTrue(data['errors'])

	def test_login_wrong_password(self):
		usuario = {
			'correo': random_mail(),
			'contraseña': 'test'
		}

		new_user = self.client.post('/usuarios', json=usuario)

		login_user = {
			"correo": usuario['correo'],
			"contraseña": "wrong_password"
		}

		response = self.client.post('/api/login', json=login_user)
		data = json.loads(response.data)

		self.assertEqual(response.status_code, 401)
		self.assertEqual(data['success'], False)


	def test_login_user_not_exists(self):
		response = self.client.post('/api/login', json=self.not_found_user)
		data = json.loads(response.data)
		self.assertEqual(response.status_code, 401)
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


