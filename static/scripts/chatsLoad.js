//active para cada chat
function loadChat(id){
	//cargar chat
	console.log(id + " loading")
}


$(document).ready(function(){
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
});