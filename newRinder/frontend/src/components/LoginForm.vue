<template>
  <div class="main_container">
    <section id="login-section">
      <form id="login-form" @submit="submitForm">
        <div class="container_register">
          <label for="email_login">Correo electrónico:</label>
          <input
            type="email"
            v-model="email"
            required
            autocomplete="on"
            name="correo"
          />

          <label for="password_login">Contraseña:</label>
          <input
            type="password"
            name="contraseña"
            v-model="password"
            required
            autocomplete="on"
          />
          <div v-if="loginFailed" id="login_fallido" style="display: none">
            Error
          </div>

          <button type="submit" id="login-btn">Iniciar sesión</button>
        </div>
      </form>
      <p href="#" id="show-register">
        ¿No tienes una cuenta?
        <a href="/register" @click="showRegisterForm">Regístrate aquí</a>
      </p>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      password: "",
      loginFailed: false,
    };
  },
  methods: {
    submitForm(event) {
      event.preventDefault();

      let formulario = document.getElementById("login-form");
      // Obtener datos del formulario
      formulario = new FormData(formulario);
      formulario = JSON.stringify(Object.fromEntries(formulario));

      // Fetch a la ruta http://localhost:5000/api/login
      fetch("http://localhost:5000/api/login", {
        method: "POST",
        body: formulario,
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .then((res) => {
          console.log(res.access_token);
          this.setAccessTokenCookie(res.access_token);

          // Redirigir a la página de inicio o a otra ruta deseada
          window.location.href = "/";
        })
        .catch((err) => console.log(err));
    },
    setAccessTokenCookie(access_token_cookie) {
      if (access_token_cookie) {
        // Establecer la cookie con el token de acceso
        document.cookie = `access_token_cookie=${access_token_cookie}; path=/;`;
      }
    },
  },
};
</script>

<style scoped>
.container_register {
  display: flex;
  flex-direction: column;
  /* flex-wrap: wrap; */
  align-content: space-around;
  justify-content: center;
  align-items: center;
  background: white;
  width: 100%;
  padding: 15px;
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

.main_container {
  width: 35%;
  max-width: 375px;
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
  font-size: 13px;
  margin-top: 10px;
}

.container {
  overflow-y: scroll;
  height: 100vh;
}

#register-section {
  display: none;
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
</style>
