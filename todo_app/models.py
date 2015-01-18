# coding: utf-8
from datetime import date
import django
from django.db import models
from django.template import Context
from django.template.loader import get_template


class Task(models .Model):
    task_text = models.CharField(max_length=64)
    due_date = models.DateField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    overdue = False
    text_html = ''

    def __str__(self):
        return self.task_text

    def __unicode__(self):
        return unicode(self.task_text)

    def get_html(self, filename):
        try:
            template = get_template(filename)
            context = Context({'task': self})
            return template.render(context)
        except django.template.TemplateDoesNotExist:
            print "Template " + filename + " does not exists!"
            return ""

    def get_task_text_html(self):
        return self.get_html('task_text.html')

    def get_task_html(self):
        self.check_overdue()
        return self.get_html('task.html')

    def check_overdue(self):
        if self.due_date:
            self.overdue = self.due_date < date.today()

    def change_done_state(self):
        self.is_done = not self.is_done
        self.save()