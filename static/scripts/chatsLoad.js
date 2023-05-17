//active chat class: contact-box-active

//active para cada chat
function showChat(id){
	//cargar chat
	console.log(id + " loading")
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

	if(contact.ruta_photo == null){
		clone.getElementsByClassName('contact-box-immage')[0].getElementsByTagName('img')[0].src = 'static/profilePhotos/default/defaultProfile.png';
	}else{
		clone.getElementsByClassName('contact-box-immage')[0].getElementsByTagName('img')[0].src = 'static/profilePhotos/' + contact.id + '/' + contact.ruta_photo;
	}

	clone.getElementsByClassName('contact-box-message')[0].innerHTML = '<p><strong>' + contact.username + '</strong></p><p>' + contact.lastMessageContent + '</p>';
	const img = clone.getElementsByClassName('contact-box-img')[0];
	//set attribute data-id
	const message_container = document.getElementById('messages-list-container');
	clone.setAttribute('data-id', contact.id);
	message_container.appendChild(clone);
	return clone;
}  
 

function loadChats(){
	fetch('/mensajes/list', {
		method: 'POST',
		credentials: 'include'
	})
	.then(function(response){
		return response.json();
	})
	.then(function(data){
		if (data.success) {
		for(var i = 0; i < data.chats.length; i++){
			renderContactBox(contact);
			document.getElementById('show_chats').style.display = 'block';
			document.getElementById('show_chats').innerHTML ='Aca se van a mostrar tus chats!';
		}
		assingChatsActions();
		}else{
			//error
			alert('error');
		}
	})
	.catch(function(error){
		alert('error');
	});

}

const boton_mensajes = document.getElementById('Mensajes');
boton_mensajes.addEventListener('click', loadChats);