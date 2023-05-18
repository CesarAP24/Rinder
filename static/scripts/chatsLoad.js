//active chat class: contact-box-active

//active para cada chat
function showChat(id){
	//cargar chat
	const messages_container = document.getElementById('user-Message-box');
	//eliminar hijos del container
	var contactor = messages_container.children;
	var max = contactor.length;
	for (var i = 0; i < max; i++) {
		contactor[i].remove();
		i--;
		max--;
	}

	id_last_message = id;
	//get a la uta /Mensaje mandando el id
	fetch('/Mensajes?id_mensaje=' + id, {
		method: 'GET',
		credentials: 'include'
	})
	.then(function(response){
		return response.json();
	})
	.then(function(data){
		console.log(data);
		if (data.success) {
			for (var i = 0; i < data.data.length; i++) {
				var mensaje = document.createElement('div');
				mensaje.classList.add("user-Message")
				if (data.data[i].propietario == 0){
					mensaje.classList.add('server-Message');
				} else if (data.data[i].propietario == 1){
					mensaje.classList.add('this-Message');
				} else {
					mensaje.classList.add('other-Message');
				}
				mensaje.innerHTML = "<p>" + data.data[i].contenido + "</p>";
				messages_container.appendChild(mensaje);
			}
		}
	})
	.catch(function(error){
		alert(error);
	});

}


function assingChatsActions(){

	$('.contact-box').click(function(){
		//checkear si no está activo
		if (!$(this).hasClass('contact-box-active')) {
			$('.contact-box').removeClass('contact-box-active');
			$(this).addClass('contact-box-active');
			//data-id
			var id = $(this).attr('data-id');
			showChat(id);
		}
	});
}

function renderContactBox(contact) {
	const clone = document.getElementById('template-contact-box').cloneNode(true);
	console.log(contact)

	//eliminar atributo id
	clone.removeAttribute('id');

	if(contact.otherUser.ruta_photo == null){
		clone.getElementsByClassName('contact-box-immage')[0].getElementsByTagName('img')[0].src = 'static/profilePhotos/default/defaultProfile.png';
	}else{
		clone.getElementsByClassName('contact-box-immage')[0].getElementsByTagName('img')[0].src = 'static/profilePhotos/' + contact.otherUser.other_id + '/' + contact.otherUser.ruta_photo;
	}

	clone.getElementsByClassName('contact-box-message')[0].innerHTML = '<p><strong>' + contact.otherUser.username + '</strong></p><p>' + contact.lastMessage.contenido + '</p>';
	const img = clone.getElementsByClassName('contact-box-img')[0];
	//set attribute data-id
	const message_container = document.getElementById('messages-list-container');
	clone.setAttribute('data-id', contact.lastMessage.id_mensaje);
	clone.setAttribute('data-chat-id', contact.id_chat);
	message_container.appendChild(clone);
	return clone;
}  
 

function loadChats(){
	const contacts_Container = document.querySelector('#messages-list-container');
	const messages_container = document.getElementById('user-Message-box');
	//eliminar hijos del container
	var contactor = messages_container.children;
	var max = contactor.length;
	for (var i = 0; i < max; i++) {
		contactor[i].remove();
		i--;
		max--;
	}
	
	//hoijos del container
	var contactor = contacts_Container.children;
	var max = contactor.length;
	for (var i = 1; i < max; i++) {
		contactor[i].remove();
		i--;
		max--;
	}


	fetch('/mensajes/list', {
		method: 'POST',
		credentials: 'include'
	})
	.then(function(response){
		return response.json();
	})
	.then(function(data){
		console.log(data);
		if (data.success) {
			for(var i = 0; i < data.data.length; i++){
				renderContactBox(data.data[i]);
			}
			assingChatsActions();
		}else{
			//error
			alert('error');
		}
	})
	.catch(function(error){
		alert(error);
	});

}

const boton_mensajes = document.getElementById('Mensajes');
boton_mensajes.addEventListener('click', loadChats);