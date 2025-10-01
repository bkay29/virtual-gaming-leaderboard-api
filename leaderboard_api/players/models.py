from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import uuid

class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # safer than SERIAL
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  
    username = models.CharField(max_length=150, unique=True)  # unique login name
    display_name = models.CharField(max_length=150, null=True, blank=True)  # optional nickname
    created_at = models.DateTimeField(auto_now_add=True)  # auto set when created
    is_active = models.BooleanField(default=True)  # soft delete flag

    def __str__(self):
        return self.display_name or self.username