$(document).on('click', '.spoiler', function() {
    var element_id = $(this).find('.content');
    var content = $(element_id).toggleClass('hide');
});
