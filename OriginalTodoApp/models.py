from django.db import models

# Create your models here.
PRIORITY = (('warning', 'high'), ('success', 'normal'), ('primary', 'low'))
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(null=True)
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY
    )
    duedate = models.DateField()
    def __str__(self):
        return self.title

