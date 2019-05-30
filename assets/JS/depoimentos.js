var numeroCards = document.getElementsByName("descricaoDepoimento").length;
$(document).ready(function(){
    if (numeroCards === 1) {
        $('.carrossel-depoimentos').slick({
            dots: false,
            nextArrow: '.btn-next-carrossel-depoimentos',
            prevArrow: '.btn-prev-carrossel-depoimentos',
            customPaging: function(slider, i){
                return (`<div class="ponto-carrossel-depoimentos">
                </div>`)
            },
            arrow: false,
            infinite: true,
            speed: 1000,
            slidesToShow: 1,
            adaptiveHeight: true,
            centerMode: true,
            centerPadding: '100px',
            responsive: [
                {
                    breakpoint: 750,
                    settings: {
                        centerPadding: '40px',
                    }
                },
            ]
        });   
    } else {
        $('.carrossel-depoimentos').slick({
            dots: true,
            nextArrow: '.btn-next-carrossel-depoimentos',
            prevArrow: '.btn-prev-carrossel-depoimentos',
            customPaging: function(slider, i){
                return (`<div class="ponto-carrossel-depoimentos">
                </div>`)
            },
            infinite: true,
            speed: 1000,
            slidesToShow: 1,
            adaptiveHeight: true,
            centerMode: true,
            centerPadding: '100px',
            responsive: [
                {
                    breakpoint: 750,
                    settings: {
                        centerPadding: '40px',
                    }
                },
            ]
        });
    }
 });
