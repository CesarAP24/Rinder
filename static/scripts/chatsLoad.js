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