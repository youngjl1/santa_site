$(function() {
  console.log( "ready!" );
  var photos_raw = $('meta[name=photos]').attr("content");
  var giver = $('meta[name=giver]').attr("content");
  console.log(photos_raw)
  var photos = photos_raw.split(",")

  pause = 1100
  i = Math.floor(Math.random() * 1000) % photos.length;
  $("#mystery_photo").html('<img src="' + photos[i % photos.length] + '">')

  ;(function animate_photos() {
    setTimeout(function() {
      i += 1
      $("#mystery_photo").html('<img src="' + photos[i % photos.length] + '">')
      if (pause > 100) {
        pause -= 100
      }
      if (i < 30) {
        animate_photos();
      }else{
        reveal_final();
      }
    }, pause);
  })();

  function reveal_final(){
    $("#mystery_box").css("display", "none")
    $("#reveal_box").css("display", "block")
  }
  //<img src="/photos/{{ info["photo"] }}">



});
