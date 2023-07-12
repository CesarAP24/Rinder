<template>
  <div class="sidebar">
    <div>
      <div class="title">
        <img
          src="../assets/rinderText.PNG"
          class="logo2"
          @click="redirectToHome"
        />
      </div>
      <a href="\">Rind your love!</a>
      <a href="\messages">Mensajes</a>
      <a href="\profile">Mi Perfil</a>
      <a href="\plans">Planes</a>
      <a href="\support">Soporte</a>
    </div>
    <div>
      <button id="log-out-btn">Log out</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "SideBar",
  data() {
    return {
      currentTab: "matches",
    };
  },
  mounted() {
    document.getElementById("log-out-btn").addEventListener("click", () => {
      this.logout();
    });
  },
  methods: {
    logout() {
      // Eliminar la cookie de acceso
      document.cookie =
        "access_token_cookie=; path=/; expires=Thu, 01 Jan 1970 00:00:01 GMT;";
      window.location.href = "/";
    },
  },
};
</script>

<style>
.sidebar .title {
  display: flex;
  /* padding: 10px; */
  width: 86%;
  height: 15%;
  flex-direction: row;
  justify-content: left;
  align-items: center;
  margin-top: -22px;
}

.sidebar .title img {
  height: 104px;
  margin-left: -13px;
  width: 80%;
  margin-top: 16px;
}

/* Estilo para la barra lateral */
.sidebar {
  width: 100%; /* Asegura que ocupe todo el ancho del contenedor principal */
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

.sidebar > div:first-child {
  flex-grow: 1; /* Hace que ocupe todo el espacio vertical disponible */
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

.sidebar #log-out-btn {
  display: block;
  padding: 10px;
  font-size: 16px;
  margin-bottom: 10px;
  text-decoration: none;
  color: #fff;
  transition: all 0.5s ease;
  width: 100%;
  border: none;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0);
}

.sidebar a:hover,
.sidebar #log-out-btn:hover {
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

/* Estilo para los elementos activos de la barra lateral */
.sidebar a.active {
  background-color: rgba(255, 255, 255, 0.3);
  color: white;
  border-radius: 10px;
}

.logo2 {
  width: 100px;
}
</style>
