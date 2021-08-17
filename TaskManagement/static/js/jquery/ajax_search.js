const searchInput = document.getElementById('search_here')
console.log(searchInput)

const searchdata =(search_here) => {
    $.ajax({
        type: "GET",
        url: $("#search_here").data('url'),

        data: {
            'search': search_here
        },
        success: function(data){
            $('#search_result').html(data)
            $(".delete_content").remove();
        },
        error: function(data) {
            console.log("error")
        }

    });
    return false
}

searchInput.addEventListener('keyup', e=>{
    console.log(e.target.value);

    searchdata(e.target.value); 
})


























// // $(function(){

// //     $('#search').keyup(function() {
    
// //         $.ajax({
        
// //             url: "//search/",
// //             data: { 
// //                 'search_text' : $('#search').val(),
// //                 'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
// //             },
// //             success: searchSuccess,
// //             dataType: 'html'
// //         });
        
// //     });

// // });

// // function searchSuccess(data, textStatus, jqXHR)
// // {
// //     $('#search-results').html(data);
// // }