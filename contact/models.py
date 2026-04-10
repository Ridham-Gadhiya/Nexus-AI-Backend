from django.db import models

class ContactSubmission(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
