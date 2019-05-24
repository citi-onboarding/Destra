var $doc = $('html, body');
$('.scrollSuave').click(function() {
    $doc.animate({
        scrollTop: $( $.attr(this, 'href') ).offset().top
    }, 500);
    return false;
});

let mainNav = document.getElementById('jsMenu');

var $doc = $('html, body');
$('.jsNavbarToggle').click(function() {
    mainNav.classList.toggle('active');
});