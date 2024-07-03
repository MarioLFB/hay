
// Fade out the success message for login after 2 seconds
$(document).ready(function() {
    setTimeout(function() {
        $('#success-message').fadeOut('slow');
    }, 2000); // 2000 milissegundos = 2 seconds
});


