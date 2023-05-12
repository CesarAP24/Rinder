
// Genera una sal aleatoria

function encriptarClave(event){
    const bcrypt = require('bcryptjs');
    const salt = bcrypt.genSaltSync(10);
    const clave = new String(document.getElementById('password').value);
    const hash = bcrypt.hashSync(clave, salt);
    document.getElementById('password').value = hash;
}


function validarClave(event){
    event.preventDefault();
    const clave_ingresada = new String(document.getElementById('password_login').value);
    if (bcrypt.compareSync(clave_ingresada, hash)) {
        validarMail(event);
      } else {
        document.getElementById('constrasena_incorrecta').style.display = 'block';
      }
}