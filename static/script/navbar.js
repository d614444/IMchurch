$(function(){
    $(".navbar").hide();

    $(window).scroll(function () {
        // set distance user needs to scroll before we fadeIn navbar
        var coodrinate = $('#section-1').offset().top
        if ($(this).scrollTop() > (coodrinate-100)) {
            $('.navbar').fadeIn();
        } else {
            $('.navbar').fadeOut();
        }
    });

})