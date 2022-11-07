from tkinter import CASCADE
from django.db import models

class Skills(models.Model):
    skill = models.CharField(max_length = 255)
    percent = models.IntegerField()

    def __str__(self):
        return self.skill + ' - ' + str(self.percent) + '%'

class Info (models.Model):
    title = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    position = models.CharField(max_length = 255)
    email = models.EmailField()
    phone = models.IntegerField()
    description = models.TextField(max_length = 500)
    image = models.ImageField(null = True,blank=True, upload_to="images/")
    cv = models.FileField(null = True)
    skills = models.ManyToManyField(Skills)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(null = True, max_length=25)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=255, null=True)
    type = models.ManyToManyField(Category)
    image = models.ImageField(null = True,blank=True, upload_to="images/")
    body = models.TextField()
    author = models.ForeignKey(Info, on_delete=models.CASCADE)
    feature = models.ImageField(null = True,blank=True, upload_to="images/")
    released = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-released']

class Post(models.Model):
    author = models.ForeignKey(Info, on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(null = True,blank=True, upload_to="images/")
    intro = models.TextField()
    body = models.TextField()
    released = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-released']

class CommentPost(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['date_added']

class CommentProject(models.Model):
    post = models.ForeignKey(Project, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-date_added']

class Contact(models.Model):
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField(max_length=1000)

class CompanyExp(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Experience(models.Model):
    person = models.ForeignKey(Info, on_delete= models.CASCADE)
    company = models.ForeignKey(CompanyExp, on_delete = models.CASCADE)
    title = models.CharField(max_length = 255, null = True)
    description = models.TextField(max_length = 1000)
    date = models.DateField(null=True)

    def __str__(self):
        return self.title
    def get_date(self):
        return self.strftime('%b %Y')