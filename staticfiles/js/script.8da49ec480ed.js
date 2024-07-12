
// Make message disappear after 2 seconds
$(document).ready(function() {
    setTimeout(function() {
        $('#success-message').fadeOut('slow');
    }, 2000); // 2000 milissegundos = 2 seconds
});

// Makes the header appear after 3.2 seconds
$(document).ready(function(){
    $("header").hide();
    $("header").fadeIn(2300);
});

$(document).ready(function(){
    $(".menu-navbar").hide();
    $(".menu-navbar").fadeIn(4000);
});

$(document).ready(function(){
    $(".food-menu").hide();
    $(".food-menu").fadeIn(4500);
});

$(document).ready(function(){
    $(".contact-container").hide();
    $(".contact-container").fadeIn(2500);
});




$(".food-1").show("slide", { direction: "left" }, 2500);