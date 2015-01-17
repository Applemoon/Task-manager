$('document').ready(function () {
    $('.btn-check-done').click(function() {
        var taskid = $(this).attr("data-taskid");

        $.get('/check_task_done/', {task_id: taskid}, function (data) {
            $('#task-' + taskid).html(data);
        })
    });

    $('#new-task-form').submit(function() {
        var task_text = $('#new-task-input').val();
        var task_date = ''; // TODO прикрутить выбор даты

        $.get('/add_new_task/', {task_text: task_text, task_date: task_date}, function (data) {
            $('.container').append(data)
        });
        return false
    });
});
