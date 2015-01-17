# coding: utf-8
from django.db import models


class Task(models .Model):
    task_text = models.CharField(max_length=64)
    due_date = models.DateField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    overdue = False

    def __str__(self):
        return self.task_text

    def __unicode__(self):
        return unicode(self.task_text)

    def get_due_date(self):
        return self.due_date