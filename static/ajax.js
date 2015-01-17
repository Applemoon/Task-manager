$('document').ready(function () {
    $('#new-task-form').submit(function() {
        var task_text = $('#new-task-input').val();
        var task_date = ''; // TODO прикрутить выбор даты

        $.get('/add_new_task/', {task_text: task_text, task_date: task_date}, function (data) {
            $('#task-container').prepend(data);
            $('#new-task-input').val('')
        });
        return false
    });

    $('.task-container__btn-check-done').click(function() {
        var task_id = $(this).attr("data-task-id");

        $.get('/check_task_done/', {task_id: task_id}, function (data) {
            $('#task-' + task_id + ' .task-container__task-text').html(data);
        })
    });

    $('.task-container__btn-remove').click(function() {
        var task_id = $(this).attr("data-task-id");

        $.get('/remove_task/', {task_id: task_id}, function (data) {
            $('#task-' + task_id).remove()
        })
    });

});
