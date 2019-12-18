
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

        $(document).ready(function() {
		
    

});
function send_data_ajax(c_btn){
	$(c_btn).click(function(){
		$.ajax({
            data: {
                id_product: $(this).attr('data')
            },
            type: 'POST',
            url: "/admin/delete/"
        })
	})
}
send_data_ajax('.delete_btn');
//style for select option
$('select').each(function () {

    var $this = $(this),
        numberOfOptions = $(this).children('option').length;

    $this.addClass('s-hidden');

    $this.wrap('<div class="select"></div>');

    $this.after('<div class="styledSelect"></div>');
    var $styledSelect = $this.next('div.styledSelect');

    $styledSelect.text($this.children('option').eq(0).text());
    var $list = $('<ul />', {
        'class': 'options'
    }).insertAfter($styledSelect);
    for (var i = 0; i < numberOfOptions; i++) {
        $('<li />', {
            text: $this.children('option').eq(i).text(),
            rel: $this.children('option').eq(i).val()
        }).appendTo($list);
    }

    var $listItems = $list.children('li');

    $styledSelect.click(function (e) {
        e.stopPropagation();
        $('div.styledSelect.active').each(function () {
            $(this).removeClass('active').next('ul.options').hide();
        });
        $(this).toggleClass('active').next('ul.options').toggle();
    });
    $listItems.click(function (e) {
        e.stopPropagation();
        $styledSelect.text($(this).text()).removeClass('active');
        $this.val($(this).attr('rel'));
        $list.hide();
    });

    $(document).click(function () {
        $styledSelect.removeClass('active');
        $list.hide();
    });

});

//style for input file
;(function($) {

	var multipleSupport = typeof $('<input/>')[0].multiple !== 'undefined',
		isIE = /msie/i.test( navigator.userAgent );

	$.fn.customFile = function() {

	  return this.each(function() {

		var $file = $(this).addClass('custom-file-upload-hidden'), 
			$wrap = $('<div class="file-upload-wrapper">'),
			$input = $('<input type="text" class="file-upload-input" name="text_image" />'),
			$button = $('<button type="button" class="file-upload-button">Select a File</button>'),
			$label = $('<label class="file-upload-button" for="'+ $file[0].id +'">Select a File</label>');

		$file.css({
		  position: 'absolute',
		  left: '-9999px'
		});

		$wrap.insertAfter( $file )
		  .append( $file, $input, ( isIE ? $label : $button ) );

	
		$file.attr('tabIndex', -1);
		$button.attr('tabIndex', -1);

		$button.click(function () {
		  $file.focus().click(); 
		});

		$file.change(function() {

		  var files = [], fileArr, filename;

		  if ( multipleSupport ) {
			fileArr = $file[0].files;
			for ( var i = 0, len = fileArr.length; i < len; i++ ) {
			  files.push( fileArr[i].name );
			}
			filename = files.join(', ');
		  } else {
			filename = $file.val().split('\\').pop();
		  }

		  $input.val( filename )
			.attr('title', filename)
			.focus(); 

		});

		$input.on({
		  blur: function() { $file.trigger('blur'); },
		  keydown: function( e ) {
			if ( e.which === 13 ) { 
			  if ( !isIE ) { $file.trigger('click'); }
			} else if ( e.which === 8 || e.which === 46 ) { 
			  $file.replaceWith( $file = $file.clone( true ) );
			  $file.trigger('change');
			  $input.val('');
			} else if ( e.which === 9 ){ 
			  return;
			} else { 
			  return false;
			}
		  }
		});

	  });

	};

	if ( !multipleSupport ) {
	  $( document ).on('change', 'input.customfile', function() {

		var $this = $(this),
			uniqId = 'customfile_'+ (new Date()).getTime(),
			$wrap = $this.parent(),

			$inputs = $wrap.siblings().find('.file-upload-input')
			  .filter(function(){ return !this.value }),

			$file = $('<input type="file" id="'+ uniqId +'" name="'+ $this.attr('name') +'"/>');

		setTimeout(function() {
		  if ( $this.val() ) {
			if ( !$inputs.length ) {
			  $wrap.after( $file );
			  $file.customFile();
			}
		  } else {
			$inputs.parent().remove();
			$wrap.appendTo( $wrap.parent() );
			$wrap.find('input').focus();
		  }
		}, 1);

	  });
	}

}(jQuery));

$('input[type=file]').customFile();


//check valid type image

function checkextension() {
	var file = document.querySelector(".upload_image");
	if ( /\.(jpe?g|png|gif|svg|jpg)$/i.test(file.files[0].name) === false ) { 
		$("#form_product").submit(function(e){
			e.preventDefault();
			return false;
		});
		$('.not-image').show();

	}
  }