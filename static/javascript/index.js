
$('.btt-link').click(function(e) {
    window.scrollTo(0,0)
})


$('#sort-selector').change(function() {
    var selector = $(this);
    var currentUrl = new URL(window.location);

    var selectedVal = selector.val();
    if(selectedVal != "reset"){
        var sort = selectedVal.split("_")[0];
        var sort_direction = selectedVal.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("sort_direction", sort_direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("sort_direction");

        window.location.replace(currentUrl);
    }
})

$('.update-link').click(function(e) {
    var form = $(this).prev('update-form');
    form.submit();
)}

$('.remove-item').click(function(e) {
    var csrfToken = "{{ csrf_token}}";
    var itemId = $(this).attr('id').split('remove_')[1];
    var size = $(this).data('size');
    var url = '/shopping_bag/remove/$(itemId)';
    var data = {'csrfmiddlewaretoken': csrfToken, 'size': size}
    form.submit();

    $.post(url, data)
     .done(function() {
         location.reload();
     });
)}