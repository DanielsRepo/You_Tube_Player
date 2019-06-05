$(document).ready(function () {
    $(".thumb").click(function (event) {
        event.preventDefault();

        $.ajax({
            type: 'POST',
            url: window.page_data.like,
            data: {
                'video_id': $(this).closest('div').parent().find('a').attr('href'),
                'csrfmiddlewaretoken': window.page_data.csrf
            },
            dataType: "json"
        });

        if ($(this).hasClass('like')) {
            $(this).removeClass('like fa-thumbs-up')
                .addClass('dislike fa-thumbs-down');
        } else {
            $(this).removeClass('dislike fa-thumbs-down')
                .addClass('like fa-thumbs-up');
        }
    });
});