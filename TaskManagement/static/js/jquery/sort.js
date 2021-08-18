$("#sort").change(function () {
    console.log("abcd")
    var sort = $(this).val()
    $.ajax({
        url: $(this).data('url'),
        data: {
            'sort': sort
        },
        datatype: 'json',

        success: function(babu){
            $('#search_result').html(babu)
            $(".delete_content").remove();
        },
        error: function(data) {
            console.log("error")
        }
    })}); 