<template>
  <div class="messages-view">
    <div class="left-Messages-container">
      <h3>Mensajes</h3>
      <div class="messages-list-container" id="messages-list-container">
        <MessageList
          v-for="chat in chats"
          :key="chat.id_chat"
          :name="chat.name"
          :image="chat.photo"
          :lastMessage="chat.id_mensaje"
          :id="chat.id_chat"
          @click="openChat"
        />
      </div>
    </div>

    <div class="right-Messages-container">
      <div id="main-Messages-container" class="main-Messages-container">
        <div class="user-Message-box" id="user-Message-box">
          <div
            class="message-bubble"
            :class="message.class"
            v-for="message in mensajes"
            :key="message.id"
          >
            <p>{{ message.contenido }}</p>
          </div>
        </div>
      </div>
      <div class="send-Messages-container">
        <input
          type="text"
          placeholder="Escribe un mensaje"
          id="mensaje_value"
        />
        <button id="send-btn" class="send-btn" @click="sendMessage">
          Enviar
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import MessageList from "@/components/MessageList.vue";

export default {
  components: {
    MessageList,
  },
  mounted() {
    this.loadChats();
  },
  data() {
    return {
      chats: [
        {
          id: 34567890,
          name: "Chica uwu",
          photo: "http://localhost:5000/static/images/algo.png",
          lastMessage: "Último mensaje aquí",
        },
      ],
      mensajes: [
        {
          id: 1,
          contenido: "Aqui irán los chats",
          class: "user-Message",
        },
      ],
    };
  },
  methods: {
    loadChats() {
      //fetch a la ruta /usuarios/chats
      // fetch("http://localhost:5000/usuarios/chats", {
      //   method: "GET",
      //   credentials: "include",
      // })
      //   .then((res) => res.json())
      //   .then((data) => {
      //     console.log(data);
      //     this.chats = data.chats;
      //   });
    },
    openChat() {
      //actualizar mensajes
      this.mensajes = [];
    },
    sendMessage() {
      const inputm = document.getElementById("mensaje_value");
      const mensaje = inputm.value;
      this.mensajes = [
        ...this.mensajes,
        {
          id: this.mensajes.length + 1,
          contenido: mensaje,
          class: "this-Message",
        },
      ];
    },
  },
};
</script>

<style>
#user-Message-image {
  width: 100px;
  height: 100px;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  border-radius: 50%;
  margin-bottom: 15px;
}

#user-Message-image img {
  height: 100%;
}

.messages-view {
  display: flex;
  flex-direction: row;
  justify-content: stretch;
  align-items: stretch;
  max-width: none;
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
}

/*left container ---- CONTACTOS*/
.left-Messages-container {
  display: flex;
  flex-direction: column;
  width: 30%;
  height: 100%;
  margin: 0;
  padding: 0;
  background-color: rgba(0, 0, 0, 0.05);
  border-right: 1px solid rgba(0, 0, 0, 0.1);
}

.left-Messages-container h3 {
  margin: 20px;
}

.Messages-container {
  display: flex;
  flex-direction: row;
  justify-content: stretch;
  align-items: stretch;
  max-width: none;
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
}

.contact-box-immage img {
  height: 100%;
}

/*left container ---- CONTACTOS*/
.left-Messages-container {
  display: flex;
  flex-direction: column;
  width: 30%;
  height: 100%;
  margin: 0;
  padding: 0;
  background-color: rgba(0, 0, 0, 0.05);
  border-right: 1px solid rgba(0, 0, 0, 0.1);
}

.left-Messages-container h3 {
  margin: 20px;
}

.left-Messages-container .contact-box {
  display: flex;
  height: 100px;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
  flex-wrap: nowrap;
  width: 100%;
  height: 100px;
  margin: 0;
  padding: 0;
  transition: all 0.2s ease-in-out;
}

.left-Messages-container .contact-box p {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.contact-box:hover {
  background-color: rgba(0, 0, 0, 0.05);
  cursor: pointer;
}

.contact-box-active {
  border-right: 3px solid #e15a87;
  background-color: rgba(0, 0, 0, 0.035);
  transition: all 0.2s ease-in-out;
}

.left-Messages-container .contact-box .contact-box-immage {
  border-radius: 100%;
  overflow: hidden;
  flex-shrink: 0;
  width: 60px;
  height: 60px;
  margin: 10px;
}

.left-Messages-container .contact-box .contact-box-message {
  height: 100%;
  margin: 10px;
  overflow: hidden;
  padding: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  flex-grow: 1;
}

.left-Messages-container .contact-box .contact-box-message p {
  margin: 0;
}

/*right container - MESSAGES*/

.right-Messages-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 70%;
  height: 100%;
  margin: 0;
  padding: 0;
}

.right-Messages-container .main-Messages-container {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  justify-content: flex-start;
  align-items: center;
  width: 100%;
  overflow-y: scroll;
  height: calc(100% - 100px);
  margin: 0;
  padding: 0;
}

/*SCROLL BAR chats!*/

.right-Messages-container .main-Messages-container::-webkit-scrollbar {
  width: 5px;
  height: 0;
  background-color: rgba(0, 0, 0, 0.05);
}

.right-Messages-container .main-Messages-container::-webkit-scrollbar-thumb {
  background-color: rgba(0, 0, 0, 0.1);
}

.right-Messages-container .main-Messages-container .user-Message-info {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  width: 100%;
  padding: 25px;
  background-color: rgba(0, 0, 0, 0.015);
  border-bottom: 2px solid rgba(0, 0, 0, 0.02);
}

.right-Messages-container .main-Messages-container .user-Message-info:hover {
  background-color: rgba(0, 0, 0, 0.035);
  cursor: pointer;
}

.right-Messages-container .main-Messages-container .user-Message-info img {
  border-radius: 100%;
  overflow: hidden;
  margin-bottom: 25px;
}

.right-Messages-container .main-Messages-container .user-Message-box {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: center;
  width: 100%;
  height: 100%;
  padding: 15px 15px 0 15px;
}

.right-Messages-container
  .main-Messages-container
  .user-Message-box
  .user-Message {
  display: flex;
  flex-direction: row;
}

.user-Message {
  width: 100%;
}

.other-Message {
  /*alinear a la izquierda el div*/
  justify-content: flex-start;
}
.this-Message {
  /*alinear a la derecha el div*/
  justify-content: flex-end;
}

.server-Message {
  width: 100%;
  text-align: center;
  justify-content: center;
  margin-bottom: 16px;
}

.user-Message p {
  display: inline-block;
  padding: 10px;
  font-size: 15px;
  margin: 5px;
  padding: 15px;
  max-width: 84%;
  overflow-wrap: anywhere;
}

.other-Message p {
  /*rosa*/
  background-color: #306ffc;
  color: white;
  border-radius: 15px 15px 15px 0;
}

.this-Message p {
  color: black;
  background-color: rgba(0, 0, 0, 0.05);
  border-radius: 15px 15px 0 15px;
}

.server-Message p {
  background: #f8e5ee;
  color: black;
  width: 100%;
  border-radius: 19px;
}

.right-Messages-container .send-Messages-container {
  display: flex;
  flex-direction: row;
  justify-content: stretch;
  align-items: center;
  width: 100%;
  height: 78px;
  padding: 12px;
  background-color: rgb(31 31 31 / 5%);
}

.emoji-btn,
.file-btn,
.send-btn {
  font-size: 16px;
  padding: 10px;
  border-radius: 100%;
  border: 0;
  background-color: transparent;
}

/*hover*/
.emoji-btn:hover,
.file-btn:hover {
  background-color: rgba(0, 0, 0, 0.1);
}

.send-btn:hover {
  font-weight: bold;
}

/*clicks*/
.emoji-btn:active,
.file-btn:active {
  background-color: rgba(0, 0, 0, 0.2);
}

.send-btn:active {
  font-weight: lighter;
}

.send-Messages-container input {
  margin: 15px;
  padding: 10px;
  border-radius: 10px;
  border: 0;
  background-color: rgba(0, 0, 0, 0.05);
  width: 100%;
  height: 100%;
  font-size: 15px;
  font-family: "Montserrat", sans-serif;
}

/*input active*/
.send-Messages-container input:focus {
  outline: none;
  background-color: rgba(0, 0, 0, 0.1);
}

.left-Messages-container .contact-box {
  display: flex;
  height: 100px;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
  flex-wrap: nowrap;
  width: 100%;
  height: 100px;
  margin: 0;
  padding: 0;
  transition: all 0.2s ease-in-out;
}

.left-Messages-container .contact-box p {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.contact-box:hover {
  background-color: rgba(0, 0, 0, 0.05);
  cursor: pointer;
}

.contact-box-active {
  border-right: 3px solid #e15a87;
  background-color: rgba(0, 0, 0, 0.035);
  transition: all 0.2s ease-in-out;
}

.left-Messages-container .contact-box .contact-box-immage {
  border-radius: 100%;
  overflow: hidden;
  flex-shrink: 0;
  width: 60px;
  height: 60px;
  margin: 10px;
}

.left-Messages-container .contact-box .contact-box-message {
  height: 100%;
  margin: 10px;
  overflow: hidden;
  padding: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  flex-grow: 1;
}

.left-Messages-container .contact-box .contact-box-message p {
  margin: 0;
}

/*right container - MESSAGES*/

.right-Messages-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 70%;
  height: 100%;
  margin: 0;
  padding: 0;
}

.right-Messages-container .main-Messages-container {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  justify-content: flex-start;
  align-items: center;
  width: 100%;
  overflow-y: scroll;
  height: calc(100% - 100px);
  margin: 0;
  padding: 0;
}

/*SCROLL BAR chats!*/

.right-Messages-container .main-Messages-container::-webkit-scrollbar {
  width: 5px;
  height: 0;
  background-color: rgba(0, 0, 0, 0.05);
}

.right-Messages-container .main-Messages-container::-webkit-scrollbar-thumb {
  background-color: rgba(0, 0, 0, 0.1);
}

.right-Messages-container .main-Messages-container .user-Message-info {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  width: 100%;
  padding: 25px;
  background-color: rgba(0, 0, 0, 0.015);
  border-bottom: 2px solid rgba(0, 0, 0, 0.02);
}

.right-Messages-container .main-Messages-container .user-Message-info:hover {
  background-color: rgba(0, 0, 0, 0.035);
  cursor: pointer;
}

.right-Messages-container .main-Messages-container .user-Message-box {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: center;
  width: 100%;
  height: 100%;
  padding: 15px 15px 0 15px;
}

.right-Messages-container
  .main-Messages-container
  .user-Message-box
  .user-Message {
  display: flex;
  flex-direction: row;
}

.user-Message {
  width: 100%;
}

.other-Message {
  /*alinear a la izquierda el div*/
  justify-content: flex-start;
}
.this-Message {
  /*alinear a la derecha el div*/
  justify-content: flex-end;
}

.server-Message {
  width: 100%;
  text-align: center;
  justify-content: center;
  margin-bottom: 16px;
}

.user-Message p {
  display: inline-block;
  padding: 10px;
  font-size: 15px;
  margin: 5px;
  padding: 15px;
  max-width: 84%;
  overflow-wrap: anywhere;
}

.other-Message p {
  /*rosa*/
  background-color: #306ffc;
  color: white;
  border-radius: 15px 15px 15px 0;
}

.this-Message p {
  color: black;
  background-color: rgba(0, 0, 0, 0.05);
  border-radius: 15px 15px 0 15px;
}

.server-Message p {
  background: #f8e5ee;
  color: black;
  width: 100%;
  border-radius: 19px;
}

.right-Messages-container .send-Messages-container {
  display: flex;
  flex-direction: row;
  justify-content: stretch;
  align-items: center;
  width: 100%;
  height: 78px;
  padding: 12px;
  background-color: rgb(31 31 31 / 5%);
}

.emoji-btn,
.file-btn,
.send-btn {
  font-size: 16px;
  padding: 10px;
  border-radius: 100%;
  border: 0;
  background-color: transparent;
}

/*hover*/
.emoji-btn:hover,
.file-btn:hover {
  background-color: rgba(0, 0, 0, 0.1);
}

.send-btn:hover {
  font-weight: bold;
}

/*clicks*/
.emoji-btn:active,
.file-btn:active {
  background-color: rgba(0, 0, 0, 0.2);
}

.send-btn:active {
  font-weight: lighter;
}

.send-Messages-container input {
  margin: 15px;
  padding: 10px;
  border-radius: 10px;
  border: 0;
  background-color: rgba(0, 0, 0, 0.05);
  width: 100%;
  height: 100%;
  font-size: 15px;
  font-family: "Montserrat", sans-serif;
}

/*input active*/
.send-Messages-container input:focus {
  outline: none;
  background-color: rgba(0, 0, 0, 0.1);
}

.other-Message {
  display: flex;
  width: 100%;
  justify-content: flex-start;
}

.this-Message p {
  color: black;
  background-color: rgba(0, 0, 0, 0.05);
  border-radius: 15px 15px 0 15px;
  padding: 14px;
}

.this-Message {
  display: flex;
  width: 100%;
  justify-content: flex-end;
  padding-bottom: 13px;
}

.right-Messages-container
  .main-Messages-container
  .user-Message-box
  .user-Message {
  display: flex;
  flex-direction: row;
  width: 100%;
  justify-content: center;
}

.other-Message p {
  background-color: #306ffc;
  color: white;
  padding: 10px;
  border-radius: 15px 15px 15px 0;
}
</style>
