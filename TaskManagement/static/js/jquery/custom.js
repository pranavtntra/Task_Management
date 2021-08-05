const searchInput = document.getElementById('search_here')
console.log(searchInput)

const searchdata =(search_here) => {
    $.ajax({
        type: "GET",
        url: 'http://127.0.0.1:8000/accounts/searchuser/',
        data: {
            'search_here': search_here
        },
        success: function(data){
           $('#search_result').html(data)
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
    return false; 
})

$(document).on('click', '.confirm-delete', function(){
    return confirm('Are you sure you want to delete this?');
})