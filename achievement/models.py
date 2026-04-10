from django.db import models
from owner.models import User, BaseModel

class Achievement(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='achievement/image/', null=True, blank=True)
    img_link = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title