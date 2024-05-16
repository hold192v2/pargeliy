from django.contrib import admin
from rating_app.models import Comment

# Register your models here.
@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {}