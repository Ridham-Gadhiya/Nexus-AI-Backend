from django.db import models
from owner.models import User, BaseModel

class Developer(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)
    role = models.CharField(choices=[
        ('python Developer', 'Python Developer'),
        ('fullstack developer', 'Fullstack Developer'),
        ('devOps engineer', 'DevOps Engineer'),
        ('data scientist', 'Data Scientist'),
        ('ai/ml engineer', 'AI/ML Engineer'),
    ], max_length=50, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='developer/image/', null=True, blank=True)
    linkedln = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.name
