<template>
  <div class="profile-top">
    <div class="profile-info-fast">
      <div class="profile-info-immage">
        <img
          id="profile-section-photo-img"
          src="http://localhost:5000/static/images/casurpiemelisante/algo.png"
          alt="Foto de perfil"
        />
        <button id="btn-add-photo" class="btn-add-photo">
          <span class="icon" @click="openEditProfilePhoto">+</span>
        </button>
      </div>
      <!-- Información rápida, número de likes recibidos, seguidores, etc. -->
      <div class="profile-info-fast-box">
        <div class="fast-info-box">
          <h3 id="profile-name">Cesar Perales</h3>
        </div>
      </div>
      <form id="form-photo">
        <div
          id="fullscreen2"
          class="vista-superior"
          @click="closeEditProfilePhoto"
        ></div>
        <div
          id="mensaje-emergente"
          class="mensaje-emergente"
          v-show="showEmergente"
        >
          <label for="file-upload">Subir una foto de perfil</label>
          <input type="file" id="file-upload" name="file-upload" />
          <button type="submit" class="btn-send" id="btn-submit-profile-photo">
            Enviar
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProfileHeader",
  data() {
    return {
      isEditProfilePhotoOpen: false,
    };
  },
  methods: {
    openEditProfilePhoto() {
      const fullscreen = document.getElementById("fullscreen2");
      const mensajeEmergente = document.getElementById("mensaje-emergente");
      this.isEditProfilePhotoOpen = true;
      fullscreen.style.display = "block";
      mensajeEmergente.style.display = "block";
    },
    closeEditProfilePhoto() {
      const fullscreen = document.getElementById("fullscreen2");
      const mensajeEmergente = document.getElementById("mensaje-emergente");
      this.isEditProfilePhotoOpen = false;
      fullscreen.style.display = "none";
      mensajeEmergente.style.display = "none";
    },
  },
};
</script>

<style scoped>
.Perfil-container {
  max-width: none;
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  overflow: scroll;
}

.Perfil-container::-webkit-scrollbar {
  width: 3px;
  height: 0;
  background-color: rgba(0, 0, 0, 0);
}

.Perfil-container::-webkit-scrollbar-thumb {
  background-color: rgba(0, 0, 0, 0.02);
}

.profile-container {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.profile-top {
  margin-top: 100px;
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.profile-banner-image {
  width: 100%;
  height: auto;
}

.profile-banner-image img {
  width: 100%;
  height: auto;
}

.profile-info-fast[data-v-0fabfe96] {
  width: 100%;
  border-bottom: 2px solid rgba(0, 0, 0, 0.1);
  height: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: stretch;
  flex-wrap: wrap;
}

.profile-info-fast-box {
  display: flex;
  flex-direction: row;
  justify-content: flex-end; /* Cambia "right" por "flex-end" para alinear el texto a la derecha */
  align-items: center;
  padding-left: 15px;
}

.fast-info-box {
  height: auto;
  display: flex;
  padding: 15px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.profile-info-immage {
  display: flex;
  border-radius: 15px;
  width: 150px;
  height: 150px;
  overflow: hidden;
  margin: 25px;
  margin-top: -80px;
  border: 4px solid white;
  align-items: center;
  justify-content: flex-end;
  text-align: right; /* Alineación del texto */
}

.profile-top {
  margin-top: 100px;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-end;
}

.profile-info-immage img {
  width: 100%;
  height: 100%;
  object-fit: cover; /* Ajuste de la imagen para cubrir el contenedor sin distorsión */
}

.profile-down {
  padding: 15px;
  width: 100%;
  display: flex;
  justify-content: space-around;
  flex-direction: row;
}

.profile-info-main,
.profile-post-box {
  margin-bottom: 20px;
}

.profile-down .profile-info-main {
  width: 30%;
  padding: 20px;
  height: fit-content;
}

.profile-posts {
  width: 65%;
}

.profile-post-header {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: left;
  margin-bottom: 15px;
}

.profile-post-user-image {
  border-radius: 100%;
  overflow: hidden;
  margin-right: 15px;
}

.profile-post-footer {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.profile-post-footer-right button {
  border: none;
  background-color: rgba(0, 0, 0, 0);
  border-radius: 100%;
  font-size: 20px;
  cursor: pointer;
}

.profile-post-footer-right button:hover {
  color: #ff0000;
  background-color: rgba(0, 0, 0, 0.05);
}

.profile-post-footer-right button:active {
  background-color: rgba(0, 0, 0, 0.1);
}

.liked {
  color: #ff0000;
  background-color: rgba(0, 0, 0, 0.05);
}

.profile-post-content {
  margin: 27px 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  flex-wrap: wrap;
  align-items: center;
}

.profile-post-content img {
  max-width: 100%;
}

.btn-add-photo[data-v-0fabfe96] {
  background-color: #007bff;
  border-width: thick;
  border-radius: 124%;
  padding: 2px 2px;
  font-size: 8px;
  font-weight: bold;
  transition: background-color 0.2s ease-in-out;
  width: 32px;
  text-align: center;
  border: 2px solid white;
  margin-bottom: -110px;
  margin-right: -7px;
}

.btn-add-photo:hover {
  background-color: #0062cc;
}

.icon {
  font-family: Impact;
  display: inline-block;
  width: 24px;
  height: 25px;
  background-color: transparent;
  color: white;
  border-radius: 50%;
  text-align: center;
  font-size: 18px;
  font-weight: bolder;
}

.btn-edit-profile {
  background-color: #e4e0e0;
  color: #343434;
  border: none;
  border-radius: 11px;
  padding: 5px 10px;
  font-size: 16px;
  font-weight: bolder;
  cursor: pointer;
  transition: background-color 0.2s ease-in-out;
  width: 100%;
}

.btn-edit-profile:hover {
  background-color: #f1eded;
  color: #343434;
}

.btn-edit-profile:active {
  background-color: #e4e0e0;
}

p2 {
  font-size: 13px;
  font-weight: bolder;
}

button.profile-post-like-btn {
  font-family: "Ysabeau";
}

#fullscreen {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  z-index: 1000; /* asegúrate de que tenga un índice z alto para estar por encima de todo lo demás */
  background-color: rgba(0, 0, 0, 0.5); /* un fondo negro transparente */
}

.mensaje-emergente {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  border: white;
  border-radius: 9px;
  width: 420px;
  padding: 20px;
  z-index: 2000;
}

#description {
  max-width: 100%;
  min-width: 100%;
  max-height: 200px;
  min-height: 200px;
  overflow-y: scroll;
  margin-top: 13px;
  border-color: #e9e7ea;
  border-width: 2px;
}

input[type="file"]::-webkit-file-upload-button {
  background-color: #f8f8f8;
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 8px 12px;
  cursor: pointer;
  font-weight: bold;
  color: #444;
}

input[type="file"]::-moz-file-upload-button {
  background-color: #f8f8f8;
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 8px 12px;
  cursor: pointer;
  font-weight: bold;
  color: #444;
}

input[type="file"]::-ms-browse {
  background-color: #f8f8f8;
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 8px 12px;
  cursor: pointer;
  font-weight: bold;
  color: #444;
}

input[type="file"]:focus::-webkit-file-upload-button {
  outline: none;
  border-color: #68a9ef;
}

input[type="file"]:focus::-moz-file-upload-button {
  outline: none;
  border-color: #68a9ef;
}

input[type="file"]:focus::-ms-browse {
  outline: none;
  border-color: #68a9ef;
}

#file-upload {
  margin-top: 40px;
  margin-bottom: 40px;
}

.btn-send {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 8px 19px;
  border-radius: 5px;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: block;
}

.btn-send:hover {
  background-color: rgb(4, 4, 179);
}

#center-matches {
  position: relative;
  transition: all 1s ease;
  left: 0;
}

#profile-name {
  font-size: 18px;
  color: #333;
  text-align: right; /* Agrega esta línea para alinear el texto a la derecha */
}

.move-right {
  transform: translateX(100%);
}

/* ----------------------------------------------
 * Generated by Animista on 2023-5-15 19:57:49
 * Licensed under FreeBSD License.
 * See http://animista.net/license for more info. 
 * w: http://animista.net, t: @cssanimista
 * ---------------------------------------------- */

/**
 * ----------------------------------------
 * animation slide-out-right
 * ----------------------------------------
 */
@-webkit-keyframes slide-out-right {
  0% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
    opacity: 1;
  }
  100% {
    -webkit-transform: translateX(1000px);
    transform: translateX(1000px);
    opacity: 0;
  }
}
@keyframes slide-out-right {
  0% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
    opacity: 1;
  }
  100% {
    -webkit-transform: translateX(1000px);
    transform: translateX(1000px);
    opacity: 0;
  }
}

/* ----------------------------------------------
 * Generated by Animista on 2023-5-15 20:6:32
 * Licensed under FreeBSD License.
 * See http://animista.net/license for more info. 
 * w: http://animista.net, t: @cssanimista
 * ---------------------------------------------- */

/**
 * ----------------------------------------
 * animation slide-out-left
 * ----------------------------------------
 */
@-webkit-keyframes slide-out-left {
  0% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
    opacity: 1;
  }
  100% {
    -webkit-transform: translateX(-1000px);
    transform: translateX(-1000px);
    opacity: 0;
  }
}
@keyframes slide-out-left {
  0% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
    opacity: 1;
  }
  100% {
    -webkit-transform: translateX(-1000px);
    transform: translateX(-1000px);
    opacity: 0;
  }
}

.slide-out-right {
  -webkit-animation: slide-out-right 0.5s cubic-bezier(0.55, 0.085, 0.68, 0.53)
    both;
  animation: slide-out-right 0.5s cubic-bezier(0.55, 0.085, 0.68, 0.53) both;
}

.slide-out-left {
  -webkit-animation: slide-out-left 0.5s cubic-bezier(0.55, 0.085, 0.68, 0.53)
    both;
  animation: slide-out-left 0.5s cubic-bezier(0.55, 0.085, 0.68, 0.53) both;
}

/* ----------------------------------------------
 * Generated by Animista on 2023-5-15 21:43:46
 * Licensed under FreeBSD License.
 * See http://animista.net/license for more info. 
 * w: http://animista.net, t: @cssanimista
 * ---------------------------------------------- */

/**
 * ----------------------------------------
 * animation slide-in-left
 * ----------------------------------------
 */
@-webkit-keyframes slide-in-left {
  0% {
    -webkit-transform: translateX(-1000px);
    transform: translateX(-1000px);
    opacity: 0;
  }
  100% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
    opacity: 1;
  }
}
@keyframes slide-in-left {
  0% {
    -webkit-transform: translateX(-1000px);
    transform: translateX(-1000px);
    opacity: 0;
  }
  100% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
    opacity: 1;
  }
}

.slide-in-left {
  -webkit-animation: slide-in-left 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94)
    both;
  animation: slide-in-left 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
}

/* ----------------------------------------------
 * Generated by Animista on 2023-5-15 21:58:48
 * Licensed under FreeBSD License.
 * See http://animista.net/license for more info. 
 * w: http://animista.net, t: @cssanimista
 * ---------------------------------------------- */

/**
 * ----------------------------------------
 * animation slide-in-right
 * ----------------------------------------
 */
@-webkit-keyframes slide-in-right {
  0% {
    -webkit-transform: translateX(1000px);
    transform: translateX(1000px);
    opacity: 0;
  }
  100% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
    opacity: 1;
  }
}
@keyframes slide-in-right {
  0% {
    -webkit-transform: translateX(1000px);
    transform: translateX(1000px);
    opacity: 0;
  }
  100% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
    opacity: 1;
  }
}

.slide-in-right {
  -webkit-animation: slide-in-right 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94)
    both;
  animation: slide-in-right 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
}

/* PLANES */
.Planes {
  float: left;
  width: 300px;
  height: 250px;
  background-color: white;
  margin-right: 10px;
  border-radius: 20px;
  margin-left: 20px;
  margin-top: 60px;
}

#placeholder-plan {
  background-color: #ff007f;
  width: 300px;
  height: 130px;
  border-top-right-radius: 20px;
  border-top-left-radius: 20px;
  /* background-image: url("static/images/fondoPlanes1.JPG"); */
  background-size: cover; /* Ajusta el tamaño de la imagen al contenedor */
  background-repeat: no-repeat; /* Evita la repetición de la imagen */
  background-position: center; /* Posiciona la imagen en el centro del contenedor */
}

.Planes-abajo {
  font-family: "Montserrat";
  margin-left: 10px;
  color: GREY;
  font-size: 12px;
  margin-top: 19px;
  line-height: 3px;
}

.Button-Plan {
  height: 33px;
  border: 2px solid black;
  border-radius: 28px;
  padding: 8px;
  width: 176px;
  margin-left: 108px;
  margin-top: 30px;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
}

.Planess {
  font-size: 12px;
  font-family: Arial, Helvetica, sans-serif;
  font-weight: bolder;
  text-align: center;
}

.vista-superior {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1000;
  background-color: rgba(0, 0, 0, 0.5);
  display: none;
}

.vista-superior.active {
  display: block;
}
</style>
