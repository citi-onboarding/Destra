$(document).ready(function(){
    $('.multipleItems').slick({
      dots: true,
      infinite: true,
      slidesToShow: 5,
      slidesToScroll: 5,
      speed: 200,
      prevArrow: document.querySelector('#playButtonBack'),
      nextArrow: document.querySelector('#playButtonNext'),
      responsive: [
        {
          breakpoint: 1400,
          settings: {
            slidesToShow: 4,
            slidesToScroll: 4,
            infinite: true,
            dots: true
          }
        },
        {
          breakpoint: 1200,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 3,
            infinite: true,
            dots: true
          }
        },
        {
          breakpoint: 800,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2,
            infinite: true,
            dots: true
          }
        },
        {
          breakpoint: 550,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
            infinite: true,
            dots: true,
            arrows: false,
          }
        },
      ]
    });
});
      

      