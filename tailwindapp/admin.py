from django.contrib import admin
from .models import CompanyExp,CommentProject, Info, Project,Category, Experience,Post, CommentPost
# Register your models here.

admin.site.register(Info)
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(CommentProject)
admin.site.register(Experience)
admin.site.register(CompanyExp)
admin.site.register(CommentPost)