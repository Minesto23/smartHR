$(document).ready(function(){

    $('#back_1').hide();
    $('#back_2').hide();
    $('#back_3').hide();
    $('#back_4').hide();
    $('#back_5').hide();

    $('#front_1').hover(function () {
        $('#front_1').hide();
        $('#back_1').attr('class', 'animated flipInY p-2');
        $('#back_1').show();
    }, function () {
    });

    $('#back_1').hover(function () {    
    },function () {
        $('#front_1').attr('class', 'animated flipInY text-center');
        $('#front_1').show();
        $('#back_1').hide();
    });

    $('#front_2').hover(function () {
        $('#front_2').hide();
        $('#back_2').attr('class', 'animated flipInY p-2');
        $('#back_2').show();
    }, function () {
    });

    $('#back_2').hover(function () {    
    },function () {
        $('#front_2').attr('class', 'animated flipInY text-center');
        $('#front_2').show();
        $('#back_2').hide();
    });

    $('#front_3').hover(function () {
        $('#front_3').hide();
        $('#back_3').attr('class', 'animated flipInY p-2');
        $('#back_3').show();
    }, function () {
    });

    $('#back_3').hover(function () {    
    },function () {
        $('#front_3').attr('class', 'animated flipInY text-center');
        $('#front_3').show();
        $('#back_3').hide();
    });

    $('#front_4').hover(function () {
        $('#front_4').hide();
        $('#back_4').attr('class', 'animated flipInY p-2');
        $('#back_4').show();
    }, function () {
    });

    $('#back_4').hover(function () {    
    },function () {
        $('#front_4').attr('class', 'animated flipInY text-center');
        $('#front_4').show();
        $('#back_4').hide();
    });

    $('#front_5').hover(function () {
        $('#front_5').hide();
        $('#back_5').attr('class', 'animated flipInY p-2');
        $('#back_5').show();
    }, function () {
    });

    $('#back_5').hover(function () {    
    },function () {
        $('#front_5').attr('class', 'animated flipInY text-center');
        $('#front_5').show();
        $('#back_5').hide();
    });
});