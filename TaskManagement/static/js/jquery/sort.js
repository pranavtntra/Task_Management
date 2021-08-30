$("#sort").change(function () {
    console.log("abcd")
    var sort = $(this).val()
    $.ajax({
        url: $(this).data('url'),
        data: {
            'sort': sort
        },
        datatype: 'json',

        success: function(data){
            $('#search_result').html(data)
            $(".delete_content").remove();
        },
        error: function(data) {
            console.log("error")
        }
    })}); 