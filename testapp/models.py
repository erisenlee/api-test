from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    """Model definition for Project."""

    # TODO: Define fields here
    id = models.UUIDField('id', default=uuid.uuid4(), primary_key=True)
    name = models.CharField('name', max_length=50)
    summary = models.CharField('summary', max_length=300)
    created = models.DateTimeField('created', auto_now=False, auto_now_add=True)
    project_type = models.CharField('type', max_length=1, choices=(('T', 'Team'), ('P', 'Private')))
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='user')

    class Meta:
        """Meta definition for Project."""

        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering=['created']

    def __str__(self):
        """Unicode representation of Project."""
        return '{}'.format(self.name ) # TODO

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('testapi:project-detail', kwargs={'id': self.id})


class Collection(models.Model):
    """Model definition for Collection."""
    id = models.UUIDField('id', default=uuid.uuid4(), primary_key=True)
    name = models.CharField('name', max_length=50)
    created = models.DateTimeField('created', auto_now=False, auto_now_add=True)
    descrption = models.CharField('description', max_length=300, blank=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name='Project')
    
    

    class Meta:
        """Meta definition for Collection."""

        verbose_name = 'Collection'
        verbose_name_plural = 'Collections'

    def __str__(self):
        """Unicode representation of Collection."""
        return '{}'.format(self.name)

    def save(self):
        """Save method for Collection."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Collection."""
        return ('')

    # TODO: Define custom methods here
