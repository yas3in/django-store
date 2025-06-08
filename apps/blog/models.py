from django.db import models
from django.conf import settings

       
class Post(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32, blank=True)
    auther = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="auther_post")
    post = models.TextField(blank=False, )
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
        
        
    def __str__(self) -> str:
        return f"auther: {self.first_name} {self.last_name}"    
        