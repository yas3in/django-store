from django.db import models
from django.contrib.auth.models import User
# Create your models here.
       
class Post(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32, blank=True)
    auther = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auther_post")
    post = models.TextField(blank=False, )
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
        
        
    def __str__(self) -> str:
        return f"ahter: {self.first_name} {self.last_name}"    
        