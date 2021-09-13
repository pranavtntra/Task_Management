// $(".search_date").change(function () {
//     if($('#startdate').val() && $("#enddate").val() != "") {
//         console.log("abcdxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
//         var start = $('#startdate').val()
//         var end = $('#enddate').val()
//         $.ajax({
//             url: $(this).data('url'),
//             data: {
//                 'start': start,
//                 'end': end
//             },
  
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
                console.log("abcdesggd")
                $('#search_result').html(data);
                $(".delete_content").remove();
            },
            error: function(data) {
                console.log("error")
            }
        
        })});