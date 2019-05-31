$(document).ready(function(){
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
                {
                    breakpoint: 400,
                    settings: {
                        centerPadding: '30px',
                    }
                },
            ]
        });
 });
