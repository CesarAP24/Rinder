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
			loadChat(id);
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
			var chats = data.chats;
			var html = '';
			for (var i = 0; i < chats.length; i++) {
				var chat = chats[i];
				html += '<div class="contact-box" data-id="'+chat.id+'">';
				html += '<div class="contact-box-img">';
				html += '<img src="'+chat.img+'" alt="">';
				html += '</div>';
				html += '<div class="contact-box-name">';
				html += '<p>'+chat.name+'</p>';
				html += '</div>';
				html += '</div>';
			}
			$('#chats').html(html);
			assingChatsActions();
		}else{
			//error
			console.log(data);
		}
	})
	.catch(function(error){
		console.log(error);
	});

}