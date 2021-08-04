const searchInput = document.getElementById('search_here')
console.log(searchInput)

const searchdata =(search_here) => {
    $.ajax({
        type: "GET",
        url: $(this).data('url'),
        data: {
            'qs_json': search_here
        },
        success: function(data){
            $("#btable").empty();           
            var tr=[];
            for (var i = 0; i < data.length; i++) {
                tr.push('<tr>');
                tr.push("<td>" + data[i].username + "</td>");
                tr.push("<td>" + data[i].first_name + "</td>");
                tr.push("<td>" + data[i].last_name + "</td>");
                tr.push("<td>" + data[i].contact + "</td>");
                tr.push("<td>" + data[i].email + "</td>");
                tr.push("<td>" + data[i].designation + "</td>");
                tr.push('</tr>');
            }
            $('btable').append($(tr.join('')));
        },
        error: function(data) {
            console.log("error")
        }

    });
}

searchInput.addEventListener('keyup', e=>{
    console.log(e.target.value)

    searchdata(e.target.value)  
})


// $(document).ready( function(){
//     $('#search_here').keyup(function() {
//         $.ajax({
//             type: "GET",
//             url: "account/userdetails/",
//             data: {
//                 'qs_json' : $('#search_here').val(),
//                  $('#search_result').html(newData)      
//              }
//         });
//     });
// });


// JSON.parse(data["user_list"].for((item) => {
            //     var row ="<tr>" +
            //         "<td>" + item.username + "</td>" +
            //         "<td>" + item.first_name + "</td>" +
            //         "<td>" + item.last_name + "</td>" +
            //         "<td>" + item.contact + "</td>" +
            //         "<td>" + item.email + "</td>" +
            //         "<td>" + item.designation + "</td>" +
            //         "</tr>";
            //     $('#btable').append(row);
            // }));