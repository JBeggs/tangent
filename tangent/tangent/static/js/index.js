function createCookie(name, value, days) {
    var expires;

    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toGMTString();
    } else {
        expires = "";
    }
    document.cookie = encodeURIComponent(name) + "=" + encodeURIComponent(value) + expires + "; path=/";
}

function readCookie(name) {
    var nameEQ = encodeURIComponent(name) + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) === ' ')
            c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0)
            return decodeURIComponent(c.substring(nameEQ.length, c.length));
    }
    return null;
}

function eraseCookie(name) {
    createCookie(name, "", -1);
}


function me(){
    $('#personal_data').append(readCookie('user'));
    $('.data').hide();
}

function profile(){
    $('#one').slideToggle();
    $('.data').hide();
}

function toggle_employees(){
    $('.data').slideToggle();
    $('#one').hide();
}

function your_worth(worth){
        if (worth>=4){
            me();
            employed();
        else if (worth==3){
            me();
            employed();
        } else if (worth<3){
            window.location = "/logout/";
        }
}

function employed(){

    $.ajax({
        url: 'http://staging.tangent.tngnt.co/api/employee/',
        type: 'GET',

        dataType: 'json',
        contentType: 'application/json',
        headers: {
            'Authorization': "Token " + readCookie('risk_cookie'),
            //'Content-Type':'application/json'
        },

        success: function(data) { 

            records = 1;
            $table = $('<table class="tablesorter">');
            $user_body = $('<tbody>');
            $position_body = $('<tbody>');
            $detail_body = $('<tbody>');

            $.each( data, function( id, json_object ) {
                
                $user_row = $("<tr>");
                $position_row = $("<tr>");
                $detail_row = $("<tr>");


                $.each( json_object, function( json_id, json ) {
                    if (json_id=="user"){
                        
                        $.each( json, function( key, val ) {          
                            $user_row.append($("<td>"+val+"</td>"));
                        });
                        
                        $user_body.append($user_row);
                        

                    } else if (json_id=="position"){
                        $.each( json, function( key, val ) {          
                            $position_row.append($("<td>"+val+"</td>"));
                        });
                        $position_body.append($position_row);
                        
                    } else{
                        $detail_row.append($("<td>"+json+"</td>"));
                    }
                $user_row = $("<tr>");
                $position_row = $("<tr>");
                });
                    $detail_body.append($detail_row);
                    $detail_row = $("<tr>");
            });

            $(".user").append($("<table class='tablesorter'>").append($user_body));
            $(".position").append($("<table class='tablesorter'>").append($position_body));
            $(".detail").append($("<table class='tablesorter'>").append($detail_body));

        },
        error : function(){
            window.location = "/logout/";
        }
    });

};


if(readCookie('risk')!=null){
    your_worth(readCookie('risk'));
} else {
    window.location = "/login/";
}
