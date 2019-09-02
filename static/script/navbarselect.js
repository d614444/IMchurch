$(function(){
    $(window).on('scroll', function() {
        $('.nav-part').each(function(i) {
            if($(window).scrollTop() >= ($(this).position().top)-100) {
                var id = $(this).attr('id');
            $('#navbarSupportedContent  ul li a').removeClass('active');
            $('a').eq(i).addClass('active');
          
            }  
        });
    });
})