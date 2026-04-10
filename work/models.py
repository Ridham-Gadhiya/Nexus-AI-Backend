from django.db import models
from owner.models import User, BaseModel


class Work(BaseModel):
    owner = models.ManyToManyField(User, related_name='works')
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    project_type = models.CharField(choices=[
        ('ai', 'AI'),
        ('ml', 'ML'),
        ('dl', 'DL'),
        ('web', 'Web Development'),
        ('data', 'Data'),
        ('other', 'Other')
    ], max_length=50, null=True, blank=True)
    repo_link = models.URLField(null=True, blank=True)
    live_demo = models.URLField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    tech = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.title