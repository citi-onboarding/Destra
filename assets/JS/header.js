var $doc = $('html, body');
$('.scrollSuave').click(function() {
    $doc.animate({
        scrollTop: $( $.attr(this, 'href') ).offset().top
    }, 500);
    return false;
});

let mainNav = document.getElementById('js-menu');

var $doc = $('html, body');
$('.js-navbar-toggle').click(function() {
    mainNav.classList.toggle('active');
});