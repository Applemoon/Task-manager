$(document).ready(function () {
    $('#datetimepicker1').datepicker();
});

function add_task() {
    var text_input = $('#new-task-input');
    if (text_input.val() == '') {
        text_input.focus();
        return false
    }

    var date_input = $('#datetimepicker1');

    $.get('/add_new_task/', {task_text: text_input.val(), task_date: date_input.val()}, function (data) {
        $('#task-container').prepend(data);
        $('#label-empty').hide();

        $.bootstrapGrowl("Добавлено задание '" + text_input.val() + "'", {
            type: 'success',
            align: 'right',
            offset: {from: 'bottom', amount: 20},
            width: 'auto'
        });

        text_input.val('');
        date_input.val('');
    });
    return false
}

function check_task_done(button) {
    var task_id = $(button).attr("data-task-id");

    $.get('/check_task_done/', {task_id: task_id}, function (data) {
        $('#task-' + task_id).replaceWith(data);
    });
}

function remove_task(button) {
    var task_id = $(button).attr("data-task-id");

    $.get('/remove_task/', {task_id: task_id}, function (data) {
        $('#task-' + task_id).remove();
        var label = $('#label-empty');
        if (data == 'True') {
            label.show()
        } else {
            label.hide()
        }

        $.bootstrapGrowl("Задание удалено", {
            type: 'danger',
            align: 'right',
            offset: {from: 'bottom', amount: 20},
            width: 'auto'
        });
    })
}

function mouse_over_remove_btn(button) {
    $(button).removeClass('btn-default');
    $(button).addClass('btn-danger');
}

function mouse_out_remove_btn(button) {
    $(button).removeClass('btn-danger');
    $(button).addClass('btn-default');
}