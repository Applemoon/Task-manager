from django.db import models


class Task(models .Model):
    task_text = models.CharField(max_length=64)
    due_date = models.DateField()

    def __str__(self):
        return self.task_text

    def __unicode__(self):
        return unicode(self.task_text)