let numeroCards = document.getElementsByName("publicacoesTitle").length;
$(document).ready(function(){
  if (numeroCards === 1) {
    $('.multipleItems').slick({
      dots: false,
      infinite: true,
      slidesToShow: 5,
      slidesToScroll: 5,
      speed: 200,
      prevArrow: document.querySelector('#playButtonBack'),
      nextArrow: document.querySelector('#playButtonNext'),
      responsive: [
        { breakpoint: 1400,
          settings: {
            slidesToShow: 4,
            slidesToScroll: 4,}},
        { breakpoint: 1200,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 3,}},
        { breakpoint: 800,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2,}},
        { breakpoint: 550,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
            arrows: false,}},
      ]
    })
  } else {
    $('.multipleItems').slick({
      dots: true,
      infinite: true,
      slidesToShow: 5,
      slidesToScroll: 5,
      speed: 200,
      prevArrow: document.querySelector('#playButtonBack'),
      nextArrow: document.querySelector('#playButtonNext'),
      responsive: [
        { breakpoint: 1400,
          settings: {
            slidesToShow: 4,
            slidesToScroll: 4,}},
        { breakpoint: 1200,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 3,}},
        { breakpoint: 800,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2,}},
        { breakpoint: 550,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
            arrows: false,}},
      ]
    })
  }
});
      

      