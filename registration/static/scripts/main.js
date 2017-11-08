$(document).ready(function() {
    
	$('.video-overlay').on('click', function(ev) {
		$("#video")[0].src += "?autoplay=1";
		$(".video-overlay").fadeOut(200);
	});

	$('.cases__item>table').click(function() {
  		$(this).parent().find(".cases__content").slideToggle("slow", function() { if($(this).parent().hasClass("opened")) $(this).parent().removeClass("opened"); else $(this).parent().addClass("opened");});
  	});

  	$('.lang-btn').click(function () {
        $(".lang-list, .lang-btn").toggleClass("opened");
        return false;
    });
    $(document).click(function(event) {
        if ($(event.target).closest(".lang-list").length) return;
        $('.lang-list').removeClass("opened");
        $('.lang-btn').removeClass("opened");
        event.stopPropagation();
    });

    if ($(window).width() <= 767) {
        $('.btn-mob-nav').click(function () {
    		$(".menu").removeClass("slideOutRight animated");
            $(".menu").addClass("opened slideInRight animated");
            $('body').toggleClass( "hidden" );
            return false;
        });
        $('.menu_close').click(function () {
            $(".menu").removeClass("slideInRight animated");
    	    $(".menu").addClass("slideOutRight animated");
            $('body').removeClass("hidden");
        });

        $(document).click(function(event) {
            if ($(event.target).closest(".menu").length) return;
           $(".menu").removeClass("slideInRight animated");
            $(".menu").addClass("slideOutRight animated");
            $('body').removeClass("hidden");
            event.stopPropagation();
        });
    }

    new WOW().init();

    // copy text
    
    var btns = document.querySelectorAll('.btn-copy');
    for (var i = 0; i < btns.length; i++) {
        btns[i].addEventListener('mouseleave', function(e) {
            e.currentTarget.setAttribute('class', 'btn_style');
            e.currentTarget.removeAttribute('aria-label');
        });
    }

    function showTooltip(elem, msg) {
        elem.setAttribute('class', 'btn_style tooltipped tooltipped-s');
        elem.setAttribute('aria-label', msg);
    }
        
    var clipboardDemos = new Clipboard('[data-clipboard-demo]');
    clipboardDemos.on('success', function(e) {
        e.clearSelection();
        console.info('Action:', e.action);
        console.info('Text:', e.text);
        console.info('Trigger:', e.trigger);
        showTooltip(e.trigger, (e.action=='cut' ? 'Скопировано и вырезано!' : 'Скопировано!'));
    });
    clipboardDemos.on('error', function(e) {
        console.error('Action:', e.action);
        console.error('Trigger:', e.trigger);
        showTooltip(e.trigger, fallbackMessage(e.action));
    });

    $('.btn-reg').click(function () {
        $(".from-block_reg").fadeIn(500);
        return false;
    });


    $.datepicker.setDefaults( $.datepicker.regional[ "ru" ] );
    $( "#datepicker" ).datepicker();
    $( "#datepicker2" ).datepicker();
    $( "#datepicker3" ).datepicker();
    $( "#datepicker4" ).datepicker();


    ( function( factory ) {
        if ( typeof define === "function" && define.amd ) {

            // AMD. Register as an anonymous module.
            define( [ "../widgets/datepicker" ], factory );
        } else {

            // Browser globals
            factory( jQuery.datepicker );
        }
    }( function( datepicker ) {

    datepicker.regional.ru = {
        closeText: "Закрыть",
        prevText: "&#x3C;Пред",
        nextText: "След&#x3E;",
        currentText: "Сегодня",
        monthNames: [ "Январь","Февраль","Март","Апрель","Май","Июнь",
        "Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь" ],
        monthNamesShort: [ "Янв","Фев","Мар","Апр","Май","Июн",
        "Июл","Авг","Сен","Окт","Ноя","Дек" ],
        dayNames: [ "воскресенье","понедельник","вторник","среда","четверг","пятница","суббота" ],
        dayNamesShort: [ "вск","пнд","втр","срд","чтв","птн","сбт" ],
        dayNamesMin: [ "Вс","Пн","Вт","Ср","Чт","Пт","Сб" ],
        weekHeader: "Нед",
        dateFormat: "dd.mm.yy",
        firstDay: 1,
        isRTL: false,
        showMonthAfterYear: false,
        yearSuffix: "" };
    datepicker.setDefaults( datepicker.regional.ru );

    return datepicker.regional.ru;

    } ) );


    var slider1 = $("#range_01, #range_03").ionRangeSlider({
        min: 100,
        max: 500000,
        from: 550,
        step: 100,
        grid: true
    });

    var slider1 = $("#range_02, #range_04").ionRangeSlider({
        min: 3,
        max: 24,
        from: 3,
        step: 1,
        grid: true
    });

    $( "select" ).selectmenu();

     $( "#tabs" ).tabs();

     if ($(window).width() <= 767) {
        $('.slider-team_mob').slick({
          arrows: false,
          dots: true,
          infinite: true,
          speed: 300,
          slidesToShow: 1,
          slidesToScroll: 1,
          adaptiveHeight: true
        });
    }


    $("body").prepend("<div class='mask'></div>");
    (function($) {
      $(function() {
          var popwindow = $('.popwindow');
          var popbutton = $('.popbutton');
         
          function preparewindow(windowobject) {
            var winwidth = windowobject.data("width");
            var winheight = windowobject.data("height");
            var winmargin = winwidth / 2;
            var wintitle = windowobject.data("title");

            windowobject.wrap("<div class='box_window'></div>");
            windowobject.addClass("box_window_in");
            windowobject.parent(".box_window");

            windowobject.parent(".box_window").prepend("<div class='box_title'>"+wintitle+"</div>");
            windowobject.parent(".box_window").css({'width':winwidth,'margin-left':'-'+winmargin})
            windowobject.css({'height':winheight})
          }  
          if (popwindow.length) {
            preparewindow(popwindow);
            popbutton.click(function(){
                var idwind = $(this).data("window");
                //Закрытие модалок при открывании новой
                $('.box_window').fadeOut('normal', function(){ $('body').removeClass('onModal'); }).removeClass("windactiv");
                //
                $("#" + idwind).parent(".box_window").fadeIn('normal', function(){ $('body').addClass('onModal'); }).addClass("windactiv");
                $(".mask").fadeIn();
                $("body").css("overflow", "hidden");
                $(".windactiv").css("overflow-y", "scroll");
                $(".to_blur").addClass("blur");
            });
          };
          $(document).mouseup(function(e) {
              if($('body').hasClass("onModal")){
                if($(e.target).is('.popup-style *')){
                    return false;
                }
                $(".windactiv").fadeOut('normal', function(){ $('body').removeClass('onModal'); });
                $(".windactiv").removeClass("windactiv");
                $(".mask").fadeOut();
                $(".popup-lvl2").fadeOut();
                $("body").css("overflow", "visible");
                $(".to_blur").removeClass("blur");
              }
          });


          $(".bw_close").click(function(){
            $(".windactiv").fadeOut('normal', function(){ $('body').removeClass('onModal'); });
            $(".windactiv").removeClass("windactiv");
            $(".mask").fadeOut();
            $(".popup-lvl2").fadeOut();
            $("body").css("overflow", "visible");
            $(".to_blur").removeClass("blur");
          });
      });
    })(jQuery)


});