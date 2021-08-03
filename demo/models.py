from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Book(models.Model):

    name = models.CharField(_('Name'),max_length=100)
    author = models.CharField(_('Author'),max_length=100)
    publication= models.CharField(max_length=100)
    is_published = models.BooleanField(_('Is Publishable ?'),default=False)
    published_at = models.DateTimeField(_('Published at '),auto_now_add=True)

    class Meta:
        '''Meta definition for Book.'''

        verbose_name = 'Name'
        verbose_name_plural = 'Names'

    def __str__(self):
        '''Unicode representation of Book.'''
        return self.name   