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
//     alert(JSON.stringify(data));
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
       },
       error : function() {
         postError("Gamestate could not be saved!")
       }
     })

   } else if(data.messageType == "SCORE") {

     console.log(typeof data);
     console.log(typeof JSON.stringify(data));

     //Sending the ajax post to the server, directing to the "savescore" url => directed to savescore view.
     $.ajax({
       type : "POST",
       url : "savescore",
       data : { 'jsondata' : JSON.stringify(data)},
//       data : { 'score': data.score},
       dataType: 'json',
       success : function(data) {
         $('#score').html(data);
         console.log(data);
         console.log($('#score'))

         console.log("Game score saved succesfully");
       },
       error : function() {
         postError("Score could not be saved!")
       }
     })
   } else if(data.messageType == "LOAD_REQUEST") {
     alert("Load request");
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
