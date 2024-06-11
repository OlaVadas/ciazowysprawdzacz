$(document).ready(function() {
    $('#search').on('input', function() {
        let query = $(this).val();
        if (query.length > 0) {
            $.ajax({
                url: '/suggest',
                method: 'GET',
                data: { q: query },
                success: function(data) {
                    let suggestions = JSON.parse(data);
                    $('#suggestions').empty();
                    suggestions.forEach(function(suggestion) {
                        $('#suggestions').append('<li>' + suggestion + '</li>');
                    });
                }
            });
        } else {
            $('#suggestions').empty();
        }
    });

    $(document).on('click', '#suggestions li', function() {
        $('#search').val($(this).text());
        $('#suggestions').empty();
    });
});