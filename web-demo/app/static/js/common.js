
// slide banner
 $('.slider-wrapper').slick({
    dots: true,
    infinite: true,
    speed: 500,
	fade: true,
	arrows: false,
    cssEase: 'linear'
});

$('.slide_parner').slick({
	infinite: true,
	slidesToShow: 6,
	slidesToScroll: 3,
	arrows: false,
	dots:true,
	responsive: [
		{
		  breakpoint: 991,
		  settings: {
			slidesToShow: 4,
			slidesToScroll: 4
		  }
		},
		{
			breakpoint: 767,
			settings: {
			  slidesToShow: 3,
			  slidesToScroll: 3
			}
		},
		{
		  breakpoint: 480,
		  settings: {
			slidesToShow: 1,
			slidesToScroll: 1
		  }
		}
	  ]
  });

//change value shopping cart
var x = $('.qty_val').val();
$('.btn-sub').click(function(){
     x--;
    $(this).next().val(x);    
})
$('.btn-inc').click(function(){
    x++;  
    $(this).prev().val(x);        
})


// count date

function makeTimer() {
	
		var endTime = new Date("29 April 2020 9:56:00 GMT+01:00");			
			endTime = (Date.parse(endTime) / 1000);

			var now = new Date();
			now = (Date.parse(now) / 1000);

			var timeLeft = endTime - now;

			var days = Math.floor(timeLeft / 86400); 
			var hours = Math.floor((timeLeft - (days * 86400)) / 3600);
			var minutes = Math.floor((timeLeft - (days * 86400) - (hours * 3600 )) / 60);
			var seconds = Math.floor((timeLeft - (days * 86400) - (hours * 3600) - (minutes * 60)));
  
			if (hours < "10") { hours = "0" + hours; }
			if (minutes < "10") { minutes = "0" + minutes; }
			if (seconds < "10") { seconds = "0" + seconds; }

			$(".days").html(days + "<span>Days</span>");
			$(".hours").html(hours + "<span>Hours</span>");
			$(".minutes").html(minutes + "<span>Minutes</span>");
			$(".seconds").html(seconds + "<span>Seconds</span>");		

	}

	setInterval(function() { makeTimer(); }, 1000);


// dropdown menu

function toggleDropdown (e) {
	const _d = $(e.target).closest('.dropdown'),
	  _m = $('.dropdown-menu', _d);
	setTimeout(function(){
	  const shouldOpen = e.type !== 'click' && _d.is(':hover');
	  _m.toggleClass('show', shouldOpen);
	  _d.toggleClass('show', shouldOpen);
	  $('[data-toggle="dropdown"]', _d).attr('aria-expanded', shouldOpen);
	}, e.type === 'mouseleave' ? 300 : 0);
  }
  
  $('body')
	.on('mouseenter mouseleave','.dropdown',toggleDropdown)
	.on('click', '.dropdown-menu a', toggleDropdown);