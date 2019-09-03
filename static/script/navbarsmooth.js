$(function(){
    $(' .nav-link').click(function() {
        var sectionTo = $(this).attr('href');
        $('html, body').animate({
          scrollTop: ($(sectionTo).offset().top)-100
        }, 1000);
    });
})