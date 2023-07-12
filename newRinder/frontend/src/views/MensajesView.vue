<template>
  <div class="messages-view">
    <div class="left-messages-container">
      <h3>Mensajes</h3>
      <div id="show_chats" style="display: none">
        Aquí se van a mostrar tus chats!
      </div>
      <div class="messages-list-container" id="messages-list-container">
        <message-list :chats="chats" @selectChat="openChat" />
      </div>
    </div>

    <div class="right-messages-container">
      <div id="main-messages-container" class="main-messages-container">
        <div class="user-message-info" v-if="selectedChat">
          <img :src="selectedChat.profileImage" alt="Foto de perfil" />
          <h4>{{ selectedChat.name }}</h4>
          <p><strong>Descripción: </strong>{{ selectedChat.description }}</p>
        </div>
        <div class="user-message-box" id="user-message-box">
          <message-bubble
            v-for="message in selectedChat ? selectedChat.messages : []"
            :key="message.id"
            :message="message"
          />
        </div>
      </div>
      <message-input v-if="selectedChat" />
    </div>
  </div>
</template>

<script>
import MessageInput from "@/components/MessageInput.vue";
import MessageBubble from "@/components/MessageBubbles.vue";
import MessageList from "@/components/MessageList.vue";

export default {
  components: {
    MessageInput,
    MessageBubble,
    MessageList,
  },
  data() {
    return {
      chats: [
        // Datos de ejemplo de los chats
        {
          id: 1,
          name: "Cesar Perales",
          profileImage: "https://via.placeholder.com/60",
          lastMessage: "Último mensaje aquí",
          isMatch: true,
          description: "Con propietaria pero sin dueña siuuu",
          messages: [
            { id: 1, content: "Hola", time: "10:00", isMe: false },
            { id: 2, content: "Hola, ¿cómo estás?", time: "10:05", isMe: true },
            {
              id: 3,
              content: "Bien, gracias. ¿Y tú?",
              time: "10:10",
              isMe: false,
            },
            // ...
          ],
        },
        // Otros chats...
      ],
      selectedChat: null,
    };
  },
  methods: {
    openChat(chat) {
      this.selectedChat = chat;
    },
  },
};
</script>

<style>
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
</style>
