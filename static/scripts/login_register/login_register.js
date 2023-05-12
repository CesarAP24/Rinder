const showRegisterLink = document.getElementById('show-register');
const showLoginLink = document.getElementById('show-login');
const loginSection = document.getElementById('login-section');
const registerSection = document.getElementById('register-section');
const registerBtn = document.getElementById('register-btn');



// Cuando se hace clic en el enlace para registrarse desde el formulario de inicio de sesión, ocultar el formulario de inicio de sesión y mostrar el de registro, y mostrar el botón de "Registrarse"
showRegisterLink.addEventListener('click', function(event) {
    event.preventDefault();
    loginSection.style.display = 'none';
    registerSection.style.display = 'block';
});

// Cuando se hace clic en el enlace para iniciar sesión desde el formulario de registro, ocultar el formulario de registro y mostrar el de inicio de sesión, y ocultar el botón de "Registrarse"
showLoginLink.addEventListener('click', function(event) {
    event.preventDefault();
    registerSection.style.display = 'none';
    loginSection.style.display = 'block';
});


registerBtn.addEventListener('click', function(evenet) {
    const is_valid = validarTodo(event);

    if (!is_valid) {return}
    //fetch 
    fetch('/register', {
        method: 'POST'
    }).then(function(response) {
        return response;
    }).then(function(data) {
        alert(data);
        window.location.reload();
    }).catch(function(error) {
        console.log(error);
    });
});



// FUNCION PARA VALIDAR EDAD

function validarEdad() {

	// obtener la fecha de nacimiento ingresada
	const fechaNacimiento = new Date(document.getElementById('fecha_nacimiento').value);

	// calcular la edad
	const hoy = new Date();
	let edad = hoy.getFullYear() - fechaNacimiento.getFullYear();
	const m = hoy.getMonth() - fechaNacimiento.getMonth();
    const d = hoy.getDate() - fechaNacimiento.getDate();
    if (m < 0 || (m == 0 && d < 0)) {
		edad--;
	}

	// mostrar el mensaje de error si no es mayor de edad
    if (edad < 18) {
		document.getElementById('mensaje-menor-edad').style.display = 'block';
        document.getElementById('mensaje-menor-edad').innerHTML = "Lo sentimos, debe ser mayor de edad";
        return false;
    } else if (!edad) {
        document.getElementById('mensaje-menor-edad').style.display = 'block';
        document.getElementById('mensaje-menor-edad').innerHTML = "Debe completar el campo";
        return false;
    }

    document.getElementById('mensaje-menor-edad').style.display = 'none';
    return true;
}


//FUNCION PARA VALIDAR CONTRASENA

function validarContrasena(){
    
    const password = document.getElementById('password').value;
    const password_confirmed = document.getElementById('password_confirmed').value;

    if (!password || !password_confirmed) {
        document.getElementById('contraseñas_distintas').style.display = 'block';
        document.getElementById('contraseñas_distintas').innerHTML = "Debe completar ambos campos";
        return false;
    } else if(password != password_confirmed) {
        document.getElementById('contraseñas_distintas').style.display = 'block';
        document.getElementById('contraseñas_distintas').innerHTML = "Las contraseñas no coinciden";
        return false;
    } 

    document.getElementById('contraseñas_distintas').style.display = 'none';
    return true;
}

//FUNCION VALIDAR MAIL

function validarMail(){
    
    const email = document.getElementById('email').value;
    const regex = /\S+@\S+\.\S+/;
    if (!regex.test(email)) {
        document.getElementById('mensaje-mail').style.display = 'block';
        return false;
    } else if (!email) {
        document.getElementById('contraseñas_distintas').style.display = 'block';
        document.getElementById('contraseñas_distintas').innerHTML = "Debe completar ambos campos";
        return false;
    } 
    document.getElementById('mensaje-mail').style.display = 'none';
    return true;
}


function validarTodo(event){
    event.preventDefault();

    
    const edad = validarEdad(event)
    const contra = validarContrasena(event)
    const mail = validarMail(event)

    return edad && contra && mail;
}