from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Info, Post, Project, CommentProject
from .forms import CommentForm
# Create your views here.
def index(request):
    info = Info.objects.all()
    posts = Post.objects.all()
    projects = Project.objects.all()
    context = {'info': info, 'posts':posts, 'projects': projects}
    return render(request, 'tailwindapp/index.html', context)

# def getPosts(request):
#     posts = Post.objects.all()
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
        
#         if form.is_valid():
#             comment = form.save(commit = False)
#             comment.posts = posts
#             comment.save()

#             return redirect('getPosts', slug=posts.slug)
#     else:
#         form = CommentForm()
#     context = {'posts':posts}
#     return render(request, 'tailwindapp/posts.html', context)

def getProjects(request, slug):
    projects = Project.objects.get(slug=slug)
    all_comments = CommentProject.objects.filter(
        post=projects.pk,
    )
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit = False)
            comment.projects = projects
            comment.save()

            return redirect('getProjects', slug=projects.slug)
    context = {'projects':projects,'all_comments': all_comments}
    return render(request, 'tailwindapp/projects.html', context)