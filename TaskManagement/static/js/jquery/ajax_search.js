const searchInput = document.getElementById('search_here')
console.log(searchInput)

const searchdata =(search_here) => {
    $.ajax({
        type: "GET",
        url: 'http://127.0.0.1:8000/project/search-project',

        data: {
            'chuzza': search_here
        },
        success: function(babu){
            $('#search_result').html(babu)
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


// $('#search').onclick(function() {
//     console.log("hhhhetyuu")
//     var search = $('#search1').val()

//     $.ajax({
//         type: 'get',
//         url: 'http://127.0.0.1:8000/project/search-project',

//         data: {
//             'search' : search
            
//         },
//         datatype: 'json',























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