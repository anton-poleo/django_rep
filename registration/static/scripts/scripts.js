function form_form(){
    $("#" + form_id).submit()
}
function form_handler(form_id, success_function)
{
    $("#" + form_id).submit(function() {
        if ($(this).hasClass("sending"))
            return false;

        var submit_btn = $(this).find("input[type=submit]");
        submit_btn.addClass("sending");
        submit_btn.attr("data-value", submit_btn.val());

        submit_btn.val( submit_btn.attr('data-sending-title') );

        $(this).addClass("sending");
        $.ajax({
            type : "post",
            url : $(this).attr("action"),
            data : $(this).serialize(),
            dataType : "json",
            cache : false,
            success : function(data) {
                if (data.status)
                {
                    success_function(data);
                }
                else
                {
                    $("#" + form_id).removeClass("sending");
                    var submit_btn = $("#" + form_id).find("input[type=submit]");
                    submit_btn.removeClass("sending");
                    submit_btn.val(submit_btn.attr("data-value"));
                    submit_btn.attr("data-value", "");
                    $.each(data.message, function(i, error) {
                        if (typeof error == "object")
                        {
                            for(ii in error)
                            {
                                alert(error[ii]);
                                return false;
                            }
                        }
                        alert(error);
                        return false;
                    });
                }
            }
        });
        return false;
    });
}