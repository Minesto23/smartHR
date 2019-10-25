$(document).ready(function(){

    $('#info_services_1').hide();
    $('#info_services_2').hide();
    $('#info_services_3').hide();
    $('#info_services_4').hide();

    $('#category_1').hover(function () {
        $('#h_1').attr('style', 'color: rgb(145, 50, 59)');
        $('#info_services_1').attr('class', 'animated flipInX');
        $('#info_services_1').show();
    }, function () {
        $('#h_1').attr('style', 'color: white');
        $('#info_services_1').hide();     
    });

    $('#info_services_1').hover(function () {
        $('#info_services_1').show(); 
        $('#h_1').attr('style', 'color: rgb(145, 50, 59)');       
    },function () {
        $('#info_services_1').hide();        
        $('#h_1').attr('style', 'color: white');
    });

    $('#category_2').hover(function () {
        $('#h_2').attr('style', 'color: rgb(145, 50, 59)');
        $('#info_services_2').attr('class', 'animated flipInX');
        $('#info_services_2').show();
    }, function () {
        $('#h_2').attr('style', 'color: white');
        $('#info_services_2').hide();
    });

    $('#info_services_2').hover(function () {
        $('#info_services_2').show(); 
        $('#h_2').attr('style', 'color: rgb(145, 50, 59)');       
    },function () {
        $('#info_services_2').hide();        
        $('#h_2').attr('style', 'color: white');
    });

    $('#category_3').hover(function () {
        $('#h_3').attr('style', 'color: rgb(145, 50, 59)');
        $('#info_services_3').attr('class', 'animated flipInX');
        $('#info_services_3').show();
    }, function () {
        $('#h_3').attr('style', 'color: white');
        $('#info_services_3').hide();
    });

    $('#info_services_3').hover(function () {
        $('#info_services_3').show(); 
        $('#h_3').attr('style', 'color: rgb(145, 50, 59)');       
    },function () {
        $('#info_services_3').hide();        
        $('#h_3').attr('style', 'color: white');
    });

    $('#category_4').hover(function () {
        $('#h_4').attr('style', 'color: rgb(145, 50, 59)');
        $('#info_services_4').attr('class', 'animated flipInX');
        $('#info_services_4').show();
    }, function () {
        $('#h_4').attr('style', 'color: white');
        $('#info_services_4').hide();
    });

    $('#info_services_4').hover(function () {
        $('#info_services_4').show(); 
        $('#h_4').attr('style', 'color: rgb(145, 50, 59)');       
    },function () {
        $('#info_services_4').hide();        
        $('#h_4').attr('style', 'color: white');
    });
});