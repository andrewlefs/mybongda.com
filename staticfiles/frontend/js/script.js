// Document ready
$(document).ready(function() {
    $('.close_ads').click(function(event) {
        $(this).parent().hide();
    });
    $('.lable-chatbox').click(function(event) {
        $(this).next().fadeToggle('fast', function() {});
    });

    $('.hightlight_video .content .video').hover(
        function() {
            $(this).find('.post_date').fadeIn('fast');
        },
        function() {
            $(this).find('.post_date').fadeOut('fast');
        }
    );

    $('.videos_template .comment_form > .heading > span').click(function(){
        if($('.videos_template .comment_form > .heading > span').hasClass('active')){
            $('.videos_template .comment_form > .heading > span').removeClass('active');
        }
        $(this).addClass('active');
    });

    $('.news_detail_template .comment_form > .heading > span').click(function(){
        if($('.news_detail_template  .comment_form > .heading > span').hasClass('active')){
            $('.news_detail_template  .comment_form > .heading > span').removeClass('active');
        }
        $(this).addClass('active');
    });

    $('.pagination ul li').click(function(){
        if($('.pagination ul li').hasClass('active')){
            $('.pagination ul li').removeClass('active');
        }
        if(!$(this).hasClass('middle')){
            $(this).stop().addClass('active');
        }
    });

    var ads_top = $('.live_match_template .container-fluid .row .col-md-3 .ads_area').offset().top;
    if($(window).scrollTop() >= ads_top){
        $('.live_match_template .container-fluid .row .col-md-3 .ads_area').css({
            'position' : 'fixed',
            'top': 0,
            'width' : '259px',
            'z-index' : 99999999
        });
    } else {
        $('.live_match_template .container-fluid .row .col-md-3 .ads_area').css({
            'position' : 'static',
            'width' : '100%'
        });
    }
    $(window).scroll(function(event) {
        if($(window).scrollTop() >= ads_top){
            $('.live_match_template .container-fluid .row .col-md-3 .ads_area').css({
                'position' : 'fixed',
                'top': 0,
                'width' : '259px',
                'z-index' : 99999999
            });
        } else {
            $('.live_match_template .container-fluid .row .col-md-3 .ads_area').css({
                'position' : 'static',
                'width' : '100%'
            });
        }
    });
    $(window).resize(function(event) {
        var ads_top = $('.live_match_template .container-fluid .row .col-md-3 .ads_area').offset().top;
        $(window).scroll(function(event) {
            if($(window).scrollTop() >= ads_top){
                $('.live_match_template .container-fluid .row .col-md-3 .ads_area').css({
                    'position' : 'fixed',
                    'top': 0,
                    'width' : '259px',
                    'z-index' : 99999999
                });
            } else {
                $('.live_match_template .container-fluid .row .col-md-3 .ads_area').css({
                    'position' : 'static',
                    'width' : '100%'
                });
            }
        });
    });
});
