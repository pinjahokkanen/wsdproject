/* global $ */
$(document).ready(function() {
  'use strict';

  /* Posting errormessages */
  function postError(text) {
      var message =  {
        messageType: "ERROR",
        info: text
      };
      document.getElementById('gameframe').contentWindow.postMessage(message, "*");
    }

//Reacting when window receives a message
  $(window).on('message', function(evt) {

   //Get data from sent message.
   var data = evt.originalEvent.data;

/* When receiving a message from iframe with attribute messageType and value SAVE, posting a request to savestate url and savestate view.
View returns a render function with highscores.html and updated highscores, and javascript replaces old highscore.html with new content.
*/
   if (data.messageType == "SAVE"){
     var csrftoken = getCookie('csrftoken');//Get csrf token using cookies.

     $.ajax({
       type : "POST",
       url : "savestate",
       data : { 'jsondata' : JSON.stringify(data), csrfmiddlewaretoken: csrftoken},
       dataType: 'json',
       complete: function(data) {
         $('#score').html(data.responseText);
         alert("Your gamestate and current score were saved.")
       }
     });

/* When receiving a message from iframe with attribute messageType and value SCORE, posting a request to savescore url and savescore view.
View returns a render function with highscores.html and updated highscores, and javascript replaces old highscore.html with new content.
*/
   } else if(data.messageType == "SCORE") {
     var csrftoken = getCookie('csrftoken');//Get csrf token using cookies.
     //Sending the ajax post to the server, directing to the "savescore" url => directed to savescore view.
     $.ajax({
       type : "POST",
       url : "savescore",
       data : { 'jsondata' : JSON.stringify(data), csrfmiddlewaretoken: csrftoken},
       dataType: 'json',
       complete: function(data) {
         $('#score').html(data.responseText);
         alert("Your score was submitted and saved if it was your new record.");
       }
     });

/*When receiving a message from iframe with attribute messageType and value LOAD_REQUEST, sends a load request to loadstate url and loadstate view.
If state has been saved, view returns the state which will be posted as a postMessage to the game iframe. If no state has been saved, returns an error message.
*/
   } else if(data.messageType == "LOAD_REQUEST") {
     var csrftoken = getCookie('csrftoken');//Get csrf token using cookies.
     $.ajax({
       type : "POST",
       url : "loadstate",
       data : { 'jsondata' : JSON.stringify(data), csrfmiddlewaretoken: csrftoken},
       dataType: 'json',
       success : function(data) {
         if(data.messageType == "NO_STATE") {
           alert(data.errorText);
         } else {
           var message =  {
             messageType: "LOAD",
             gameState: data
           };
           document.getElementById('gameframe').contentWindow.postMessage(message, "*");
         }
       },
       error : function() {
         postError("Gamestate could not be loaded!");
       }
     });

//Posts error message
   } else if(data.messageType == "ERROR") {
     error(data.info);

//Adjusts the iframe dimension and resolusions when receives a message with MessageType SETTING.
   } else if(data.messageType == "SETTING") {
     var width = data.options.width;
     var height = data.options.height;

     $('iframe').width(width).height(height);

   }
  });
});

/* Get Cookie - function given in django documentation */
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

//# Game cart functionality #//
  function game_to_cart(gameid) {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
      method: 'POST',
      url: 'cart',
      data: {
        csrfmiddlewaretoken: csrftoken,
                game: gameid,
                action:'add'
      },

      success:function(data) {
        if (data.error){
          alert("An error occurred.");
        } else {
          window.location.href = "games/cart";
        }
      },

      error: function(data) {
        if (data.responseJSON && data.responseJSON.error) {
          alert(data.responseJSON.error);
        }else if (data.status == 403) {
          alert("You are not allowed to purchase this game.");
        }else if (data.status == 400) {
          alert("Game already in the cart.");
        }else{
          alert("Unexpected error occurred. Please refresh page and try again.");
        }
      },
    });
}




//add active class to the navbar item
$( "#navbar-Profile" ).addClass('active');

//initialize the table
$( document ).ready(function() {
    $("#tableId").bootstrapTable();
});

//this function is used to remove a game from the cart.
// It notifies to the server and remove the game from the user interface.
 function removeList(gameid) {
   var csrftoken = getCookie('csrftoken');
    $.ajax({
        method:'POST',
        url: 'cart',
        data: {
            csrfmiddlewaretoken: csrftoken,
            game:gameid,
            action:'remove'
        },
        success:function(data) {
            if (data.error) {
                alert("Error: " + data.error);
            }else{
                $('#game-'+gameid).fadeOut(400,function(){this.remove()});
            }
        },
        error: function (data) {
            if (data.error) {
                alert("There was a problem during the request. Please try again.");
            }
        }
    });
}

/* Function categoriseInventory called onchange in game index selection. Gets the selected category, and changes display value on every game using class, which is the game category*/
function categoriseInventory() {
 var selection = document.getElementById("inventory_selection").value;

//For all elements on a page with a specific class, changes display settings according to act.
 function Display(category, act) {
   [].forEach.call(document.querySelectorAll(category), function (el) {
     el.style.display = act;
   });
 }

 if (selection == 'ALL') {
   Display('.ACTION', 'block');
   Display('.ADVENTURE', 'block');
   Display('.PUZZLE', 'block');
   Display('.SPORTS', 'block');
   Display('.EDUCATIONAL', 'block');
   Display('.UNDEFINED', 'block');
 } else if (selection == 'ACTION'){
   Display('.ACTION', 'block');
   Display('.ADVENTURE', 'none');
   Display('.PUZZLE', 'none');
   Display('.SPORTS', 'none');
   Display('.EDUCATIONAL', 'none');
   Display('.UNDEFINED', 'none');
 } else if (selection == 'ADVENTURE'){
   Display('.ACTION', 'none');
   Display('.ADVENTURE', 'block');
   Display('.PUZZLE', 'none');
   Display('.SPORTS', 'none');
   Display('.EDUCATIONAL', 'none');
   Display('.UNDEFINED', 'none');
 } else if (selection == 'PUZZLE'){
   Display('.ACTION', 'none');
   Display('.ADVENTURE', 'none');
   Display('.PUZZLE', 'block');
   Display('.SPORTS', 'none');
   Display('.EDUCATIONAL', 'none');
   Display('.UNDEFINED', 'none');
 } else if (selection == 'SPORTS'){
   Display('.ACTION', 'none');
   Display('.ADVENTURE', 'none');
   Display('.PUZZLE', 'none');
   Display('.SPORTS', 'block');
   Display('.EDUCATIONAL', 'none');
   Display('.UNDEFINED', 'none');
 } else if (selection == 'EDUCATIONAL'){
   Display('.ACTION', 'none');
   Display('.ADVENTURE', 'none');
   Display('.PUZZLE', 'none');
   Display('.SPORTS', 'none');
   Display('.EDUCATIONAL', 'block');
   Display('.UNDEFINED', 'none');
 } else if (selection == 'UNDEFINED'){
   Display('.ACTION', 'none');
   Display('.ADVENTURE', 'none');
   Display('.PUZZLE', 'none');
   Display('.SPORTS', 'none');
   Display('.EDUCATIONAL', 'none');
   Display('.UNDEFINED', 'block');
 }
}
