from django.db import models
from owner.models import User, BaseModel

class About(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    tagline = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='about/Logo/', null=True, blank=True)
    established_year = models.IntegerField(null=True, blank=True)
    linkedln = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('AI', 'Artificial Intelligence'),
        ('WEB', 'Web Development'),
        ('TOOL', 'Tools & Cloud'),
    ]

    name = models.CharField(max_length=100) # e.g., "Python"
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='AI')
    icon = models.ImageField(upload_to='about/skills/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    