from datetime import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        'owner.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_created_by"
    )
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey('owner.User',on_delete=models.SET_NULL,null=True,blank=True,related_name="%(class)s_modified_by"
    )

    class Meta:
        abstract = True
        
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
        
    def create_staffuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)
    contact_no = models.CharField(max_length=15, null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

        
        
