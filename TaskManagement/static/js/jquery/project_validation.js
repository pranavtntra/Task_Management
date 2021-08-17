//     $("#start").datepicker();
//     $("#start").on('change', function () {
//         var date = Date.parse($(this).val());
//         if (date < Date.now()) {
//             alert('Selected date must be greater than today date');
//             $(this).val('');
//         }
//     });
// });

// $('#end').on('change', function(){
//     var startDate = $('#start').val();
//     var endDate = $('#end').val();
//     if (endDate < startDate){
//         alert('End date should be greater than Start date.');
//        $('#end').val('');
//     }
// });


jquery('#start').on('change', function () {
    console.log(">><>><");
    var date = $(this).val();
    jquery('#end').datetimepicker({minDate: date});
});

// jquery('#start').on('change', function () {
//     console.log(">><><>>")
//     var date = $(this).val();
//     ('#end').datetimepicker({minDate: date});
//     });

// ('#start').on('change', function(){
//     var date = $(this).val();
//     ('#start').datetimepicker({minDate: Date.now()});  

// });