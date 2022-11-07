from cgitb import html
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import CommentPost, CompanyExp, Experience, Info, Post, Project, CommentProject
from .forms import CommentPForm, ContactForm, CommentPostForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
# Create your views here.
def contact_send(form):
    html = render_to_string('tailwindapp/emails/ContactTemplate.html',
    {'subject': form.cleaned_data['subject'],
    'email': form.cleaned_data['email'],
    'message': form.cleaned_data['body']
    })
    send_mail('Thanks for your Interest !',
    'message',
    'no-reply@mishalalfawaz.com',
    [form.cleaned_data['email'], 'mishalalfawaz@gmail.com'],
    html_message=html)

def index(request):
    info = Info.objects.all()
    posts = Post.objects.all()
    projects = Project.objects.all()
    company = CompanyExp.objects.all()
    experience = Experience.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_send(form)
            form = form.save(commit = False)
            form.save()
            return redirect('index')
    else:
        form = ContactForm()
    context = {'info': info, 'posts':posts, 'projects': projects,
    'form':form, 'experience':experience, 'company': company}
    return render(request, 'tailwindapp/index.html', context)

def getPosts(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = CommentPostForm(request.POST)
        if form.is_valid():
            html = render_to_string('tailwindapp/emails/emailtemplate.html',
            {'name': form.cleaned_data['name'],
            'email': form.cleaned_data['email'],
            'message': form.cleaned_data['body']
            })
            form = form.save(commit = False)
            form.post = post
            print("### ", form)
            form.save()
            send_mail('Thank you for your comment!',
            'message',
            'no-reply@mishalalfawaz.com',
            [form.email, 'mishalalfawaz@gmail.com'],
            html_message=html)

            return redirect('getPosts', slug=post.slug)
    else:
        form = CommentPostForm()
    context = {'post':post, 'form': form}
    return render(request, 'tailwindapp/posts.html', context)

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
            print("### ", form)
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