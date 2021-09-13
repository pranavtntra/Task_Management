// const searchInput = document.getElementById('search_here')
// console.log(searchInput)

// $("#search_here").on("keyup", function (e) {
const searchdata = (search_here) => {
    // e.preventDefault()
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
// });

document.getElementById('search_here').addEventListener('keyup', e=>{
    console.log(e.target.value);

    searchdata(e.target.value); 
})



