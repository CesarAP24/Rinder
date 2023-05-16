//variables del DOM
const nombre = document.getElementById("profile-name");
const username = document.getElementById("profile-username");

const description = document.getElementById("profile-description");
const nacimiento = document.getElementById("profile-nacimiento");
const edad = document.getElementById("profile-edad");
const genero = document.getElementById("profile-genero");

const photo = document.getElementById("profile-section-photo-img");


//función para cargar datos
function loadProfile(event) {
	event.preventDefault();

	//obtener datos con fetch
	fetch("/perfil", {
		method: "POST",
		credentials: "include"
	}).then(function (response) {
		return response.json();
	}).then(function (data) {
		//cargar datos en el DOM
		const nacimientoShow = new Date(data.nacimiento);
		//cambiar contenido de parrafos
		nombre.innerHTML = data.nombre + " " + data.apellido;
		username.innerHTML = data.username;
		description.innerHTML = "<strong>Description: </strong>" + data.descripcion;
		nacimiento.innerHTML = "<strong>Fecha de Nacimiento: </strong>" + nacimientoShow.toLocaleDateString();
		edad.innerHTML = "<strong>Edad: </strong>" + data.edad;
		genero.innerHTML = "<strong>Genero: </strong>" + data.genero;


		//imagen
		if (data.ruta_photo != null) {
			console.log(data.id_user)
			console.log(data.ruta_photo)
			photo.setAttribute("src", "static/profilePhotos/" + data.id_user + "/" + data.ruta_photo);
		} else {
			photo.setAttribute("src", "static/profilePhotos/default/defaultProfile.png");
		}
	});
}



perfilBtn = document.getElementById("Perfil");
perfilBtn.addEventListener("click", loadProfile);