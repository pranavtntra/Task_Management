$('.technologies > li').each( function() {
    $(this).after('<input type="text" name="topic" required id="id_topic" disabled="disabled" >');
});
$('input[type="checkbox"]').click( function() {
    $(this).closest('li').next('input').attr("disabled", !$(this).is(':checked'));
});