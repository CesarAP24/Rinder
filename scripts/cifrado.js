
// Genera una sal aleatoria

function encriptarClave(event){
    const bcrypt = require('bcryptjs');
    const salt = bcrypt.genSaltSync(10);
    const clave = new String(document.getElementById('password').value);
    const hash = bcrypt.hashSync(clave, salt);
}

//falta editar para comparar que el mail ademas este linkeado a esa clave y de ahi 
//compararla con la encriptada y de ahi poder iniciar sesion correctamente
const form = document.getElementById('formulario');
form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const email = document.getElementById('email').value;
  const password = document.getElementById('password_login').value;
  const hashedPassword = encriptarClave(password);
  const errors = await verificarCredenciales(email, hashedPassword);
  // Si el objeto de errores está vacío, el inicio de sesión fue exitoso
  if (Object.keys(errors).length === 0) {
    window.location.href = "index.html";
  } else {
    onSubmit(event);
  }
});

  async function onSubmit(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const errors = await verificarCredenciales(email, password);
    
    // Verificar si hay errores
    if (Object.keys(errors).length === 0) {
      // Si no hay errores, iniciar sesión o redirigir a otra página
      // ... a index.html
    } else {
      // Si hay errores, mostrarlos en la página
      if (errors.email) {
        document.getElementById('mensaje-mail').style.display = 'block';
      }
      if (errors.password) {
        document.getElementById('mensaje-password').style.display = 'block';
      }
      if (errors.error) {
        // Mostrar mensaje de error genérico
        console.error(errors.error);
      }
    }
  }
  

// function validarClave(event){
//     event.preventDefault();
//     const bcrypt = require('bcryptjs');
//     const mail_ingresado = new String(document.getElementById('email_login').value);
//     const clave_ingresada = new String(document.getElementById('password_login').value);
//     if (bcrypt.compareSync(clave_ingresada, hash)) {
//         validarMail(event);
//       } else {
//         document.getElementById('constrasena_incorrecta').style.display = 'block';
//       }
// }