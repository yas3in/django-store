from django.contrib import admin
from django.contrib.admin import register
from apps.blog.models import Post


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["auther", "post", "is_active"]
    list_editable = ("is_active", )
    list_filter = ("is_active", )



# admin.site.register(User, UserAdmin)
# admin.site.register(Post, PostAdmin)