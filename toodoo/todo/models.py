from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=150, verbose_name='Задача')
    description = models.TextField(blank=True, verbose_name='Описание задачи')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Задача создана')
    completed_date = models.DateTimeField(null=True, blank=True, verbose_name='Задача завершена')
    completed = models.BooleanField(default=False, verbose_name='Задача выполнена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
