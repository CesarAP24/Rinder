from .models import Mensaje, Usuario, Perfil, Like, Pertenece, Chat

# Utilities
def create_default_data(app, db):
	with app.app_context():
		default_message = Mensaje(id_mensaje="default", contenido="Chat Eliminado")
		if not Mensaje.query.filter_by(id_mensaje="default").first():
			db.session.add(default_message)
			db.session.commit()

		ids = ['casurpiemelisante', 'giansegg', 'isabellaromero']
		correos = ['cesar.cap20.p@gmail.com', 'giansegg@gmail.com', 'isabellaromero@gmail.com']
		contraseñas = ['74185296', '74185296', '74185296']
		nombres = ['Cesar', 'Gian', 'Isabella']
		apellidos = ['Perales', 'Segovia', 'Romero']
		generos = ['M', 'M', 'F']
		nacimientos = ['1999-07-20', '1999-07-01', '1999-12-25']

		for i in range(len(ids)):
			if not Usuario.query.filter_by(id_usuario=ids[i]).first():
				user = Usuario(correos[i], contraseñas[i], ids[i])
				user.insert()

				perfil = Perfil(id_usuario=ids[i], nombre=nombres[i], apellido=apellidos[i], genero=generos[i], nacimiento=nacimientos[i])
				db.session.add(perfil)
				db.session.commit()