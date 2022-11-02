from cgitb import html
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Info, Post, Project, CommentProject
from .forms import CommentPForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
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

def getProjects(request, pk):
    project = Project.objects.get(id=pk)
    all_comments = CommentProject.objects.filter(
        post=project.pk,
    )

    if request.method == 'POST':
        form = CommentPForm(request.POST)
        if form.is_valid():
            html = render_to_string('tailwindapp/emails/emailtemplate.html',
            {'name': form.cleaned_data['name'],
            'email': form.cleaned_data['email'],
            'message': form.cleaned_data['body']
            })
            form = form.save(commit = False)
            form.post = project
            form.save()
            send_mail('Subject',
            'message',
            'no-reply@mishalalfawaz.com',
            [form.email, 'mishalalfawaz@gmail.com'],
            html_message=html)


            return redirect('getProjects', pk = project.id)
    else:
        form = CommentPForm()
    context = {'project':project,'all_comments': all_comments,
    'form': form}
    return render(request, 'tailwindapp/projects.html', context)