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

//NOTE! Doesn't save gamestates if no game state has been created. ==> Has to be created when the game is bought
  $(window).on('message', function(evt) {
    //Note that messages from all origins are accepted
   //Get data from sent message
    var data = evt.originalEvent.data;


   if (data.messageType == "SAVE"){
     $.ajax({
       type : "POST",
       url : "savestate",
       data : { 'jsondata' : JSON.stringify(data)},
//      JSON.stringify(data) = {"messageType":"SAVE","gameState":{"playerItems":[],"score":0}}
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
       data : { 'jsondata' : JSON.stringify(data)},
//       data : { 'score': data.score},
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
       data : { 'jsondata' : JSON.stringify(data) },
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
   } else if(data.messageType == "LOAD") {
     alert("Load");
   } else if(data.messageType == "ERROR") {
     error(data.info);
   } else if(data.messageType == "SETTING") {
     var width = data.options.width;
     var height = data.options.height;

     $('iframe').width(width).height(height);

   }
  });
});
