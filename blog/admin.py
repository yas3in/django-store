from django.contrib import admin
from django.contrib.admin import register
from blog.models import User, Post


# Register your models here.


@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "password"]
    search_fields = ("username",)
    

@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["auther", "post", "is_active"]
    list_editable = ("is_active", )
    list_filter = ("is_active", )



# admin.site.register(User, UserAdmin)
# admin.site.register(Post, PostAdmin)