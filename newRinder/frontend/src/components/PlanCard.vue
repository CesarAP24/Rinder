<template>
  <div id="app"></div>
  <div class="Planes" id="basicPlan">
    <div id="placeholder-plan"></div>
    <p class="Planes-abajo">Consta en likes limitados, máximo 20 por día</p>
    <p class="Planes-abajo">____________________________________________</p>
    <div class="Button-Plan">
      <button class="Planess" @click="showPayPal">Plan Básico (Actual)</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "PlanCard",
  methods: {
    showPayPal() {
      this.$emit("showPayPal");
    },
  },
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Montserrat", sans-serif;
}
a h1,
h2,
h3,
h4,
h5,
h6 {
  margin-bottom: 0.5rem;
  font-weight: 500;
  line-height: 1.2;
}

h3 {
  font-size: 1.75rem;
}

p {
  display: block;
  margin-block-start: 1em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  margin-top: 0;
  margin-bottom: 1rem;
}

h5 {
  font-size: 1.25rem;
}

h4 {
  font-size: 1.5em;
}

/* Estilo para el body */
body {
  background-color: #f7f3f7;
  display: flex;
  flex-direction: row;
  justify-content: center;
  overflow: hidden;
  height: 100vh;
  box-sizing: border-box;
  color: #333333;
  font-family: "Montserrat", sans-serif;
  align-items: center;
  margin-bottom: 90px;
}

.main {
  /*extender el main*/
  width: 100%;
  height: 100vh;
}

/* Estilo para la barra lateral */
.sidebar {
  width: 30%;
  max-width: 300px;
  height: 100vh;
  z-index: 1;
  background-image: linear-gradient(to bottom, #ff0054, #ff00a2);
  overflow-x: hidden;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

/* Estilo para el título del sidebar */
.sidebar h1 {
  font-family: "Ysabeau", cursive;
  color: #fff;
}

.rounded-pink-border {
  border-radius: 15px;
  border: 2px solid rgb(235 214 224);
}

/* Estilo para los elementos de la barra lateral */
.sidebar a {
  display: block;
  padding: 10px;
  margin-bottom: 10px;
  text-decoration: none;
  color: #fff;
  transition: all 0.5s ease;
}

.sidebar a:hover {
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 10px;
}

.sidebar a:visited {
  color: #fff;
}

.sidebar .title {
  display: flex;
  padding: 10px;
  flex-direction: row;
  justify-content: left;
  align-items: center;
}

.sidebar .title img {
  height: 62px;
  margin-left: -13px;
}

/* Estilo para los elementos activos de la barra lateral */
.sidebar a.active {
  background-color: rgba(255, 255, 255, 0.3);
  color: white;
  border-radius: 10px;
}

/* Estilo para el contenido de la página */
.container {
  padding: 20px;
  height: 100vh;
}

/* Estilo para los títulos */
h1,
h2,
h3,
h4 {
  color: #ff007f;
}

/* Estilo para la foto de perfil */
.profile-photo {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background-color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 10px;
  overflow: hidden;
}

/*adds section*/
.adds-container {
  width: 25%;
  height: calc(100% - 40px);
  margin: 20px;
  border-radius: 15px;
  padding: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  background: linear-gradient(to bottom, #f5f5f5, #ffffff);
}

/*animacion de entrada para .title img*/
.title img {
  animation: fadeIn 1s;
}

#support {
  margin-left: 20px;
  line-height: 24px;
  font-size: 14px;
}

#placeholder-plan {
  background-color: #ff007f;
  width: 300px;
  height: 130px;
  border-top-right-radius: 20px;
  border-top-left-radius: 20px;
  /* background-image: url("static/images/fondoPlanes1.JPG"); */
  background-size: cover;
  background-repeat: no-repeat;
  margin-bottom: 21px;
  background-position: center;
}

*[data-v-43943ed4] {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  margin-right: 14px;
  font-family: "Montserrat", sans-serif;
}

*[data-v-43943ed4][data-v-43943ed4] {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Montserrat", sans-serif;
  margin-right: 14px;
  margin-top: 8px;
  margin-left: 6px;
}
</style>
