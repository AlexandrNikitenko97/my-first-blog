// Background gradient on 360 degrees
$(document).ready(function() {

	var 
		degrees = 0,
		timer = setInterval(function() {

			degrees++;	
			jQuery('.page-header').css('background', 'linear-gradient(' + degrees +'deg, #D74177, #FFE98A)');
			jQuery('.footer').css('background', 'linear-gradient(' + degrees + 'deg, #D74177 , #FFE98A)');
		}, 30000 / 360);

});


// Approve deleting post
$(document).on('click', '.confirm-delete', function(){
    return confirm('Are you sure you want to delete this post?');
})