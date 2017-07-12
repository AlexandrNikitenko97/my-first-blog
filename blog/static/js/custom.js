jQuery(document).ready(function() {

	var 
		degrees = 0,
		timer = setInterval(function() {

			degrees++;	
			jQuery('.page-header').css('background', 'linear-gradient(' + degrees +'deg, #D74177, #FFE98A)');
			jQuery('.footer').css('background', 'linear-gradient(' + degrees + 'deg, #D74177 , #FFE98A)');
		}, 30000 / 360);

});