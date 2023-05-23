from django.db import models

# Create your models here.

from django.db import models

class Task(models.Model):
    task = models.IntegerField(null=True) # parental task
    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    status = models.CharField(max_length=4, choices=[('todo', 'ToDo'), ('done', 'Done')])
    created_at = models.DateTimeField(auto_now_add=True)

    def can_be_completed(self): # can be completed if don't have any uncompleted child
        if self.status == 'todo':
            subtasks = Task.objects.filter(task=self)
            return subtasks.filter(status='todo').count() == 0
        return False

    def __str__(self):
        return self.title