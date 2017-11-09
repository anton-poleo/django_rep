$("#" + form_id).submit(function()) {
    if ($(this).hasClass("sending"))
        return false;

var submit_btn = $(this).find("input[type=submit]");
submit_btn.addClass("sending");
submit_btn.attr("data-value", submit_btn.val());
submit_btn.val( submit_btn.attr('data-sending-title') );
$.ajax({
  url: "registration/index/",
  data: $(this).serialize(),
  dataType: "json",
  cache: false,
  success: function(html){
    $("#results").append(html);
  }
});