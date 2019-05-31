var $doc = $('html, body');
$('.contate-nos').click(function() {
    $doc.animate({
        scrollTop: $( $.attr(this, 'href') ).offset().top
    }, 500);
    return false;
});
function setAssunto(assunto)
{
    document.getElementsByName('assunto')[0].value = assunto;
}