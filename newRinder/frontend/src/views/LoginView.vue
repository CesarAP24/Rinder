<template>
  <div id="total_percent">
    <div class="login-page">
      <img src="../assets/logoRinder.PNG" class="logo" />
      <LoginForm />
    </div>
  </div>
</template>

<script>
import LoginForm from "@/components/LoginForm.vue";

export default {
  components: {
    LoginForm,
  },
  methods: {
    handleLoginSuccess() {
      this.$router.push({ name: "Login" });
    },
  },
};
</script>

<style>
.login-page {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  align-items: center;
}

#total_percent {
  position: absolute;
  width: 100%;
  height: 100vh;
  background-color: #f7f3f7;
  top: 0;
  left: 0;
  display: flex;
  z-index: 100;
}

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

.logo {
  width: 200px; /* Ajusta el ancho deseado */
  height: auto; /* Mantén la proporción de la imagen */
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
</style>
