<template>
  <div id="total_percent">
    <div id="register-page">
      <RegisterForm />
    </div>
  </div>
</template>

<script>
import RegisterForm from "@/components/RegisterForm.vue";

export default {
  components: {
    RegisterForm,
  },
  methods: {
    handleRegisterSuccess() {
      this.$router.push({ name: "Register" });
    },
  },
};
</script>

<style>
#register-page {
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
  align-items: center;
  justify-content: center;
  background: white;
  width: 100%;
  height: 100%;
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
  height: 500px;
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
