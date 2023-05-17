  // hacer que fullscreen solo aparezca al precionar el boton btn-add-photo
        const miBoton = document.getElementById('btn-add-photo');
        const fullDiv = document.getElementById('fullscreen');
        const mEmergente = document.getElementById('mensaje-emergente');

        mEmergente.style.display = 'none';
        fullDiv.style.display = 'none';
        miBoton.addEventListener('click', () => {
            fullDiv.style.display = 'block';
            mEmergente.style.display = 'block';
        });

        fullDiv.addEventListener('click', () => {
            fullDiv.style.display = 'none';
            mEmergente.style.display = 'none';
        })

        //lo mismo para editar perfil
        const btnEditar = document.getElementById('btn-edit-profile');
        const mEmergente2 = document.getElementById('mensaje-emergente2');

        mEmergente2.style.display = 'none';

        btnEditar.addEventListener('click', () => {
            fullDiv.style.display = 'block';
            mEmergente2.style.display = 'block';
        });

        fullDiv.addEventListener('click', () => {
            fullDiv.style.display = 'none';
            mEmergente2.style.display = 'none';
        })

        //ACTUALIZAR INFORMACION DEL PERFIL
        const btnSend = document.getElementById('btn-send-upload');

        btnSend.addEventListener('click', () => {
            d = document.getElementById('form-upload')
            data = new FormData(d);
            data = Object.fromEntries(data);

            const json = {};

            //fetch edit profile FUNCIONAA
            fetch('\submit-profile', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
                .then(function (response) {
                    return response.json();
                })
                .then(function (data) {
                    if (data.success = true) {
                        document.getElementById('fullscreen').click();
                        document.getElementById('Perfil').click();
                    }
                    else {
                        console.log('error');
                    }
                })
                .catch(function (error) {
                    console.log(error);
                })
        })


        //ACTUALIZAR FOTO DE PERFIL

        const btnSubmit = document.getElementById('btn-submit-profile-photo');
        //el event listener de la foto de perfil
        btnSubmit.addEventListener('click', () => {
            event.preventDefault();
            //fetch add photo
            const photo = document.getElementById('form-photo');
            foto = new FormData(photo);

            fetch('\submit-photo', {
                method: 'POST',
                body: foto
            })
                .then(response => response.json())
                .then(function (foto) {
                    if (foto.success = true) {
                        document.getElementById('fullscreen').click();
                        document.getElementById('Perfil').click();
                    }
                    else {
                        console.log('error');
                    }
                })
                .catch(function (error) {
                    console.log(error);
                })
        })