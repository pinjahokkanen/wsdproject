/* global $ */
$(document).ready(function() {
  'use strict';

  function postError(text) {
      var message =  {
        messageType: "ERROR",
        info: text
      };
      //send message to iframe
      document.getElementById('gameframe').contentWindow.postMessage(message, "*");
    }

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
              // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }

//NOTE! Doesn't save gamestates if no game state has been created. ==> Has to be created when the game is bought
  $(window).on('message', function(evt) {
    //Note that messages from all origins are accepted
   //Get data from sent message
    var data = evt.originalEvent.data;
    var csrftoken = getCookie('csrftoken');

   if (data.messageType == "SAVE"){
     $.ajax({
       type : "POST",
       url : "savestate",
       data : { 'jsondata' : JSON.stringify(data), csrfmiddlewaretoken: csrftoken},
       dataType: 'json',
       success : function(data) {
         if (data.score) {
           $('#score').html(data.score);
         }
         alert("Gamestate saved succesfully!")
       },
       error : function() {
         postError("Gamestate could not be saved!")
       }
     })

   } else if(data.messageType == "SCORE") {

     //Sending the ajax post to the server, directing to the "savescore" url => directed to savescore view.
     $.ajax({
       type : "POST",
       url : "savescore",
       data : { 'jsondata' : JSON.stringify(data), csrfmiddlewaretoken: csrftoken},
       dataType: 'json',
       success : function(data) {
         $('#score').html(data);
         alert("New highscore saved succesfully!");
       },
       error : function() {
         postError("Highscore could not be saved!")
       }
     })

   } else if(data.messageType == "LOAD_REQUEST") {
     $.ajax({
       type : "POST",
       url : "loadstate",
       data : { 'jsondata' : JSON.stringify(data), csrfmiddlewaretoken: csrftoken},
       dataType: 'json',
       success : function(data) {
         if(data.messageType == "NO_STATE") {
           alert(data.errorText)
         } else {
           var message =  {
             messageType: "LOAD",
             gameState: data
           };
           document.getElementById('gameframe').contentWindow.postMessage(message, "*");
         }
       },
       error : function() {
         postError("Gamestate could not be loaded!")
       }
     })
   } else if(data.messageType == "ERROR") {
     error(data.info);
   } else if(data.messageType == "SETTING") {
     var width = data.options.width;
     var height = data.options.height;

     $('iframe').width(width).height(height);

   }
  });
});

//# Game cart functionality #//

  function game_to_cart(gameid) {
    $.ajax({
      method: 'POST',
      url: "{% url 'games:cart' %}",
      data: {
        csrfmiddlewaretoken: "{{ csrf_token  }}",
                game: gameid,
                action:'add'
      },

      success:function(data) {
        if (data.error){
          alert("An error occurred.");
        } else {
          window.location.href = "{% url 'games:cart' %}"
        //  alert("The game was added to the cart.");
        }
      },

      error: function(data) {
        if (data.responseJSON && data.responseJSON.error) {
          alert(data.responseJSON.error);
        }else if (data.status = 403) {
          alert("You are not allowed to purchase this game.");
        }else if (data.status == 400) {
          alert("Game already in the cart.");
        }else{
          alert("Unexpected error occurred. Please refresh page and try again.");
        }
      },
    })
}


//# Remove game from cart #//

//add active class to the navbar item
$( "#navbar-Profile" ).addClass('active');

//initialize the table
$( document ).ready(function() {
    $("#tableId").bootstrapTable();
});

//this function is used to remove a game from the cart.
// It notifies to the server and remove the game from the user interface.
 function removeList(gameid) {
    $.ajax({
        method:'POST',
        url: "{% url 'games:cart' %}",
        data: {
            csrfmiddlewaretoken: "{{ csrf_token  }}",
            game:gameid,
            action:'remove'
        },
        success:function(data) {
            if (data.error) {
                alert("Error: " + data.error);
            }
            else{
                $('#game-'+gameid).fadeOut(400,function(){this.remove()});
            }
        },
        error: function (data) {
            if (data.error) {
                alert("There was a problem during the request. Please try again.");
            }
        }
    })
}

<<<<<<< HEAD







=======
>>>>>>> 7cbb8e072afc647e894738c78da2469976c76a59
