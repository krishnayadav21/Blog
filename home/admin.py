from django.contrib import admin
from .models import Blogpost
from .models import Usertype


# Register your models here.
class AdminBlogpost(admin.ModelAdmin):
    list_display = ['post_id', 'title', 'subtitle', 'user_type', 'author_name', 'description','post_date']


class AdminUesrtype(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Blogpost, AdminBlogpost)
admin.site.register(Usertype, AdminUesrtype)
