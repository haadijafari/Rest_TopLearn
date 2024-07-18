from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Todo(models.Model):
    title = models.CharField(_('Title'), max_length=128)
    description = models.TextField(_('Description'))
    priority = models.IntegerField(_('Priority'), default=1)
    is_done = models.BooleanField(_('is Done?'), default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_set')

    class Meta:
        db_table = 'todos'
        ordering = ['priority', 'title']

        verbose_name = _('Todo')
        verbose_name_plural = _('Todos')

    def __str__(self):
        status = '✓' if self.is_done else 'x'
        return f'{self.title} | {status}'
