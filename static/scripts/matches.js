//funcion MOVE IMAGE para los matches
        //RECHAZO (EQUIS)

        function moveMatchesInTop() {
            const centerMatches = document.getElementById("center-matches");
            //remover todas las clases
            centerMatches.classList = "";
            centerMatches.classList.add("center-matches");
            centerMatches.classList.add("slide-in-top");
        }


        function moveMatchesOutBottom() {
            const centerMatches = document.getElementById("center-matches");
            //remover todas las clases
            centerMatches.classList = "";
            centerMatches.classList.add("center-matches");
            centerMatches.classList.add("slide-out-bottom");
        }


        function moveMatchesInBottom() {

            const centerMatches = document.getElementById("center-matches");
            //remover todas las clases
            centerMatches.classList = "";
            centerMatches.classList.add("center-matches");
            centerMatches.classList.add("slide-in-bottom");
        }

        function moveMatchesOutTop() {
            const centerMatches = document.getElementById("center-matches");
            //remover todas las clases
            centerMatches.classList = "";
            centerMatches.classList.add("center-matches");
            centerMatches.classList.add("slide-out-top");
        }

        const btnEquis = document.getElementById("equis");
        btnEquis.addEventListener("click", () => {
            moveMatchesOutBottom();
            setTimeout(function () {
                showNewUser()
            }, 300)
            setTimeout(function () {
                moveMatchesInTop();
            }, 800);
        });

        const btnLike = document.getElementById("like");
        btnLike.addEventListener("click", () => {
            moveMatchesOutTop();
            setTimeout(function () {
                showNewUser()
            }, 300)
            setTimeout(function () {
                moveMatchesInBottom();
            }, 800);

            fetch('/Users/match/check', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    'user_id': document.getElementById("foto_perfil").getAttribute("data-id")
                })

            })
                .then(response => response.json())
                .then(function (data) {
                    if (data.success = true) {
                        if (data.success && data.match) {
                            //mostrar 
                            alert("Es un match!");
                            //ir a mensajes
                            document.getElementById("Mensajes").click();
                        }
                    }
                    else {
                        console.log('error');
                    }
                })
        });

        function showNewUser() {
            fetch('/Users/match', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                },

            })
                .then(response => response.json())
                .then(function (data) {
                    console.log(data);
                    const image = document.getElementById("foto_perfil");
                    const name_age = document.getElementById("profile-photo-footer");
                    const desc = document.getElementById("profile-info-matches");
                    image.setAttribute("data-id", data.data.user_id);

                    if (!data.data.ruta_photo) {
                        image.src = "static/profilePhotos/default/defaultProfile.png";
                    }
                    else {
                        image.src = "static/profilePhotos/" + data.data.user_id + "/" + data.data.ruta_photo;
                    }

                    name_age.innerHTML = "<h4>" + data.data.nombre + "</h4><h4>" + data.data.edad + "</h4>";
                    desc.innerHTML = "<p><strong>Descripción</strong></p><p>" + data.data.descripcion + "</p>";
                })
                .catch(function (error) {
                    console.log(error);
                })
        }