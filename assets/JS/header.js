var $doc = $('html, body');
$('.scrollSuave').click(function() {
    $doc.animate({
        scrollTop: $( $.attr(this, 'href') ).offset().top
    }, 500);
    return false;
});

let mainNav = document.getElementById('jsMenu');
let buttonNav = document.getElementById('jsHamburguer');
let buttonNavClose = document.getElementById('jsClose');

var $doc = $('html, body');
$('.jsNavbarSwitch').click(function() {
    mainNav.classList.toggle('active');
    buttonNav.classList.toggle('activeHamburguer');
    buttonNavClose.classList.toggle('activeClose');
});