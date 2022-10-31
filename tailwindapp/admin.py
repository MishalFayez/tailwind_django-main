from django.contrib import admin
from .models import CommentProject, Info, Project,Category, Post, CommentPost
# Register your models here.

admin.site.register(Info)
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(CommentProject)
admin.site.register(CommentPost)