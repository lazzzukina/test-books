from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True)

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    cover = models.URLField(blank=True, null=True)
    language = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')
        db_table = 'books'

    def __str__(self):
        return self.name
