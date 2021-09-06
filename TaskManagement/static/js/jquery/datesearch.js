$(".search_date").change(function () {
    if($('#startdate').val() && $("#enddate").val() != "") {
        console.log("abcdxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        var start = $('#startdate').val()
        var end = $('#enddate').val()
        $.ajax({
            url: $(this).data('url'),
            data: {
                'start': start,
                'end': end
            },
            datatype: 'json',

            success: function(data){
                console.log("abcdesggd")
                $('#search_result').html(data);
                $(".delete_content").remove();
            },
            error: function(data) {
                console.log("error")
            }
        
        })}});