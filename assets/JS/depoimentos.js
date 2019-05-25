$(document).ready(function(){
    $('.carrossel-depoimentos').slick({
        dots: true,
        nextArrow: '.btn-next-carrossel-depoimentos',
        prevArrow: '.btn-prev-carrossel-depoimentos',
        customPaging: function(slider, i){
            return (`<div class="ponto-carrossel-depoimentos">
            </div>`)
        }
    });
 });
