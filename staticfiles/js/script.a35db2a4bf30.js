
// Make message disappear after 2 seconds
$(document).ready(function() {
    setTimeout(function() {
        $('#success-message').fadeOut('slow');
    }, 2000); // 2000 milissegundos = 2 seconds
});

// Makes the header appear after 2.3 seconds
$(document).ready(function(){
    $("header").hide();
    $("header").fadeIn(2300);
});

// Makes the footer appear after 4 seconds
$(document).ready(function(){
    $(".menu-navbar").hide();
    $(".menu-navbar").fadeIn(4000);
});

// Makes the footer appear after 4.5 seconds
$(document).ready(function(){
    $(".food-menu").hide();
    $(".food-menu").fadeIn(4500);
});

// Makes the footer appear after 2.5 seconds
$(document).ready(function(){
    $(".contact-container").hide();
    $(".contact-container").fadeIn(2500);
});