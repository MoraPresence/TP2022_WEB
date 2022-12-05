$(".totalLikes").on('click', function () {
    const request = new Request(
        'http://127.0.0.1:8000/like/',
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
            },
            body:
                'data_id=' + $(this).data('id')
            // 'data_type=' + $(this).data('type')//????
        }
    )

    fetch(request).then(response => response.json().then(
        response_json => $(this).context.innerText = response_json.likes_count
    ))
})

$(".form-check-input").on('click', function () {
    const request = new Request(
        'http://127.0.0.1:8000/correct/',
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
            },
            body:
                'data_id=' + $(this).data('id')
            // 'data_type=' + $(this).data('type')//????
        }
    )

    fetch(request).then(response => response.json().then(

    ))
})
