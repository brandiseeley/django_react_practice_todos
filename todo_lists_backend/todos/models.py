from django.db import models


class TodoList(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title


class Todo(models.Model):
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        complete = f'[{'X' if self.is_complete else ' '}]: '
        return complete + self.description