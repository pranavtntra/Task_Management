// ======for seachig in userdetails page======
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
})


// =======pop-up for delete user in userdetails=======
$(document).on('click', '.confirm-delete', function(){
    return confirm('Are you sure you want to delete this?');
})

function sortTable(n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("btable");
    switching = true;
    dir = "asc"; 
    while (switching) {
      switching = false;
      rows = table.rows;
      for (i = 1; i < (rows.length - 1); i++) {
        shouldSwitch = false;
        x = rows[i].getElementsByTagName("TD")[n];
        y = rows[i + 1].getElementsByTagName("TD")[n];
        if (dir == "asc") {
          if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
            shouldSwitch= true;
            break;
          }
        } else if (dir == "desc") {
          if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
            shouldSwitch = true;
            break;
          }
        }
      }
      if (shouldSwitch) {
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
        switchcount ++;      
      } else {
        if (switchcount == 0 && dir == "asc") {
          dir = "desc";
          switching = true;
        }
      }
    }
  }