<template>
  <div
    id="Mensajes-Content"
    class="container slide-in-top Messages-container"
    style="display: none"
  >
    <div class="left-Messages-container">
      <h3>Mensajes</h3>
      <div id="show_chats" style="display: none">
        Aca se van a mostrar tus chats!
      </div>
      <div class="messages-list-container" id="messages-list-container">
        <div class="contact-box" data-id="1" id="template-contact-box">
          <div class="contact-box-immage">
            <img src="https://via.placeholder.com/60" alt="Foto de perfil" />
          </div>
          <div class="contact-box-message">
            <p><strong>Cesar Perales</strong></p>
            <p>Last message here!</p>
            <div id="its_a_match">IT'S A MATCH!</div>
          </div>
        </div>
      </div>
    </div>

    <div class="right-Messages-container">
      <div id="main-Messages-container" class="main-Messages-container">
        <div class="user-Message-info" style="display: none">
          <img
            src="static/profilePhotos/default/defaultProfile.png"
            alt="Foto de perfil"
          />
          <h4>César Perales</h4>
          <p>
            <strong>Descripción: </strong>Con propietaria pero sin dueña siuuu
          </p>
        </div>
        <div class="user-Message-box" id="user-Message-box"></div>
      </div>
      <div class="send-Messages-container">
        <button id="emoji-btn" class="emoji-btn" style="display: none">
          🧐
        </button>
        <input
          type="text"
          placeholder="Escribe un mensaje"
          id="mensaje_value"
        />
        <button id="send-btn" class="send-btn">Enviar</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MessagesChats",
};
</script>

<style scoped>
/* Estilos para el componente Messages.vue */
</style>
