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
	clone.getElementsByClassName('contact-box-immage')[0].getElementsByTagName('img')[0].src = contact.photo;
	clone.getElementsByClassName('contact-box-message')[0].innerHTML = '<p><strong>' + contact.username + '</strong></p><p>' + contact.lastMessageContent + '</p>';
	const img = clone.getElementsByClassName('contact-box-img')[0];
	//set attribute data-id
	clone.setAttribute('data-id', contact.id);
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
		renderContactBox(contact);
					
			//cargar chats
			/*
			{
				"success": true,
				"chats": [
				{
				"id": 1,
				"username": "test",
				"lastMessageContent": "test",
				"lastMessageDate": "2020-05-26T20:47:41.000Z"
				},
				{},
				{},
				...
				];
			}
			*/
		}else{
			//error
			console.log(data);
		}
	})
	.catch(function(error){
		console.log(error);
	});

}


assingChatsActions();