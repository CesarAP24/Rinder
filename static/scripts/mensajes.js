//ENVIAR MENSAJES
        const btnEnviarMensajes = document.getElementById("send-btn");
        const inputMensajes = document.getElementById("mensaje_value");
        btnEnviarMensajes.addEventListener("click", enviar_mensaje);
        inputMensajes.addEventListener("keydown", function (event) {
            if (event.keyCode === 13) {
                event.preventDefault();
                enviar_mensaje();
            }
        })



        function enviar_mensaje(event) {
            const enterMensaje = document.getElementById("mensaje_value");
            const chatActivo = document.querySelector(".contact-box-active");
            console.log(chatActivo)
            if (chatActivo){
                const data = {
                    mensaje: enterMensaje.value,
                    chat_id: chatActivo.getAttribute("data-chat-id")
                }

                if (inputMensajes.value) {
                    fetch('\Mensajes', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(data)
                    })
                        .then(response => response.json())
                        .then(function (mensaje) {
                            if (mensaje.success = true) {
                                //enviar mensaje
                                const mensaje = document.createElement("div");
                                mensaje.classList.add("user-Message");
                                mensaje.classList.add("this-Message")
                                mensaje.innerHTML = "<p>" + enterMensaje.value + "</p>";
                                const userMessageBox = document.querySelector(".user-Message-box");
                                userMessageBox.appendChild(mensaje);

                                const container = document.getElementById("main-Messages-container");
                                container.scrollTop = container.scrollHeight;
                                inputMensajes.value = "";
                            }
                            else {
                                console.log('error');
                            }
                        })
                        .catch(function (error) {
                            console.log(error);
                        })
                }
            }
        };