<template>
  <div>
    <section id="register-section">
      <form @submit="submitForm">
        <div class="container_register">
          <div id="encap">
            <input
              type="text"
              v-model="nombre"
              required
              placeholder="Ingrese su nombre"
              autocomplete="off"
            />
            <input
              type="text"
              v-model="apellido"
              required
              placeholder="Ingrese su apellido"
              autocomplete="off"
            />
          </div>

          <input
            type="email"
            v-model="email"
            required
            placeholder="Ingrese su correo electrónico"
            autocomplete="on"
          />
          <div id="mensaje-mail" style="display: none">
            Ingrese un email válido.
          </div>

          <label for="fecha_nacimiento">Fecha de nacimiento</label>
          <input
            type="date"
            v-model="fechaNacimiento"
            required
            placeholder="Ingrese su fecha de nacimiento"
            autocomplete="off"
          />
          <div id="mensaje-menor-edad" style="display: none">
            Lo sentimos, debes ser mayor de edad para acceder a este sitio.
          </div>

          <label for="password">Contraseña</label>
          <input
            type="password"
            v-model="password"
            required
            placeholder="Ingrese su contraseña"
            autocomplete="on"
          />

          <!-- genero -->
          <div id="genero-a">
            <label for="genero">Género</label>
            <select name="genero" id="genero">
              <option value="masculino">Masculino</option>
              <option value="femenino">Femenino</option>
              <option value="otro">Otro</option>
            </select>
          </div>

          <button type="submit" id="register-btn">Registrarse</button>

          <p>
            ¿Ya tienes una cuenta?
            <a href="/login" id="show-login">Inicia sesión</a>
          </p>
        </div>
      </form>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      nombre: "",
      apellido: "",
      email: "",
      fechaNacimiento: "",
      password: "",
    };
  },
  methods: {
    submitForm(event) {
      event.preventDefault();
      // Aquí puedes agregar la lógica para enviar los datos del formulario al servidor y realizar el registro
      // Puedes acceder a los valores de los campos usando this.nombre, this.apellido, this.email, etc.
      console.log(document.getElementById("genero").value);

      const userData = {
        nombre: this.nombre,
        apellido: this.apellido,
        correo: this.email,
        nacimiento: this.fechaNacimiento,
        contraseña: this.password,
        genero: document.getElementById("genero").value,
      };

      //fetch a la ruta http://localhost:5000/api/register
      fetch("http://localhost:5000/usuarios", {
        method: "POST",
        body: JSON.stringify(userData),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
          this.login(this.email, this.password);
        })
        .catch((err) => {
          console.log(err);
          alert("Ocurrió un error al registrar el usuario");
        });
    },
    login(correo, contraseña) {
      // fetch a login
      fetch("http://localhost:5000/api/login", {
        method: "POST",
        body: JSON.stringify({
          correo: correo,
          contraseña: contraseña,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .then((data) => {
          window.location.href = "/";
          const access_token_cookie = data.access_token;
          document.cookie = `access_token_cookie=${access_token_cookie}; path=/;`;
          console.log(data);
        })
        .catch((err) => {
          console.log(err);
          alert("Ocurrió un error al iniciar sesión");
        });
    },
  },
};
</script>

<style scoped>
#register-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: #f7f3f7;
  width: 100%;
  height: 100%;
  padding: 15px;
  border-radius: 20px;
}

.container_register[data-v-6626deb7][data-v-6626deb7] {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: white;
  width: 100%;
  height: 100%;
  padding: 15px;
  border-radius: 20px;
}

.container_register button {
  margin: 11px;
  width: 95%;
  padding: 10px;
  border: none;
  font-size: 15px;
  background: #ff00a2;
  color: white;
  border-radius: 6px;
  font-family: "Montserrat";
}

button:hover {
  cursor: pointer;
  background: #ff0089;
}

input[type="text"],
input[type="password"],
input[type="email"],
input[type="date"] {
  width: 95%;
  margin: 7px;
  padding: 11px;
  border-radius: 6px;
  box-sizing: border-box;
  border: 1px solid #d5d5d5;
  font-family: "Montserrat";
}

label {
  margin-bottom: 5px;
  margin-top: 11px;
  margin-left: 22px;
  width: 100%;
  font-size: 13px;
}

h2 {
  display: block;
  font-size: 1.5em;
  margin-block-start: 0.83em;
  margin-block-end: 0.83em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  font-weight: bolder;
  text-align: center;
}

form {
  display: flex;
  border-radius: 16px;
  width: 100%;
  overflow: hidden;
}

p {
  text-align: center;
  font-size: 13px;
  margin-top: 10px;
}

.container {
  overflow-y: scroll;
  height: 100vh;
}

#contraseñas_distintas {
  color: red;
  font-size: 12px;
  font-weight: bold;
  text-align: left;
  width: 100%;
  margin-left: 27px;
}

#login_fallido {
  color: red;
  font-size: 12px;
  font-weight: bold;
  text-align: left;
  width: 100%;
  margin-left: 27px;
}

#mensaje-mail {
  color: red;
  font-size: 12px;
  font-weight: bold;
  text-align: left;
  width: 100%;
  margin-left: 27px;
}

#mensaje-menor-edad {
  color: red;
  font-size: 12px;
  font-weight: bold;
  text-align: left;
  width: 100%;
  margin-left: 27px;
}

#encap {
  display: flex;
  flex-direction: row;
  width: 98%;
  justify-content: space-between;
}

#datos {
  color: #ff00a2;
  font-weight: bolder;
  font-size: 20px;
}

#logoinicio {
  width: 86px;
  margin-bottom: 20px;
}

body {
  background-color: #f7f3f7;
  display: flex;
  flex-direction: column;
  justify-content: center;
  overflow: hidden;
  height: 100vh;
  margin: 0;
  padding: 0;
  align-items: center;
  box-sizing: border-box;
  color: #333333;
  font-family: "Montserrat", sans-serif;
}

#show-register {
  font-size: 13px;
  margin-top: 10px;
}

select {
  width: 95%;
  margin: 7px;
  padding: 11px;
  border-radius: 6px;
  box-sizing: border-box;
  border: 1px solid #d5d5d5;
  font-family: "Montserrat";
}
</style>
