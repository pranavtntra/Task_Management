  
$('#search').click(function() {

    var start_date = $("#startdate").val();
    var end_date = $("#enddate").val();
    $.ajax({

        url: $("#search").data('url'),
        method: 'get',
        data: {
            'start_date': start_date,
            'end_date': end_date,
        },
            datatype: 'json',

            success: function(data){
                $('#search_result').html(data);
                $(".delete_content").remove();
            },
            error: function(data) {
                console.log("error")
            }
        
        })});