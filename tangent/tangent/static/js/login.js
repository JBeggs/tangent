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


$(".user").focusin(function(){$(".inputUserIcon").css("color", "#e74c3c");}).focusout(function(){$(".inputUserIcon").css("color", "white");});
$(".pass").focusin(function(){$(".inputPassIcon").css("color", "#e74c3c");}).focusout(function(){ $(".inputPassIcon").css("color", "white");});


function security(){
    
    $.ajax({
        url: 'http://staging.tangent.tngnt.co/api/user/me/',
        type: 'GET',

        dataType: 'json',
        contentType: 'application/json',
        headers: {
            'Authorization': "Token " + readCookie('token'),
        },

        success: function(data) { 

            records = 1;
            html = "<table><tbody>"
            $.each( data, function( key, val ) {

                security_level = 0;
                if (key =="is_active"){security_level += 1;} else if(key =="is_staff"){security_level += 2;} else if(key =="is_superuser"){security_level += 3;}                
                html += "</tr><td>"+ key +"</td><td>"+ val +"</td></tr>"
            });

            html += "</tbody></table>"
            eraseCookie('risk');
            createCookie('risk',security_level,1);
            createCookie('risk_cookie',readCookie('token'),1);
            createCookie('user',html,1);
            your_worth(security_level);
        },
        error : function(){
            $("#login_error").html("Please Try me again...");

        }
    });

};


function your_worth(worth){
        if (worth>=3){
            // Worth it
            window.location = "/index/";
        } else if (worth<3){
            $('#login_form h2').html("Back again loser");
            $('#login_error').html("Sheep don't belong here");
        }
}


if (readCookie('token')==null || readCookie('token')=='empty'){
    if(readCookie('risk')!=null){
        your_worth(readCookie('risk'));
        createCookie('token','empty',1);
    } else {
        createCookie('token','empty',1);
        $( "#login_form" ).show();
    };
} else {
    if(readCookie('risk')!=null){
        your_worth(readCookie('risk'));           
    } else {
        security();
    };
};


$("#login_form" ).submit(function( event ) {
    $("#login_error").html("Please Wait...  ");
    $.ajax({
        url: 'http://staging.tangent.tngnt.co/api-token-auth/',
        type: 'POST',
        data: $('#login_form').serialize(), 
        success: function(data) { 
            eraseCookie('token');
            createCookie('token',data.token,1);
            
            if(readCookie('risk')!=null){
                your_worth(readCookie('risk'));          
            } else {
                security();
            };

        },
        error : function(){
            $("#login_error").html("Invalid username or password");
            createCookie('token','empty',1);
            eraseCookie('risk');
        }
    });
  event.preventDefault();
});
