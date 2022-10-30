from tkinter import CASCADE
from django.db import models


# Create your models here.
class Info (models.Model):
    title = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    position = models.CharField(max_length = 255)
    email = models.EmailField()
    phone = models.IntegerField()
    description = models.TextField(max_length = 500)
    image = models.ImageField(null = True,blank=True, upload_to="images/")
    cv = models.FileField(null = True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(null = True, max_length=25)

    def __str__(self):
        return self.name

class Project(models.Model):
    TYPE_CHOICES = [
    ('odoo', 'Odoo'),
    ('django', 'Django'),
    ('cybersecurity', 'CyberSecurity'),
    ('xml', 'XML'),
    ('python', 'Python'),
    ]
    title = models.CharField(max_length=255, null=True)
    # type = models.CharField(max_length = 25,
    #     choices = TYPE_CHOICES,
    #     default = 'odoo')
    type = models.ManyToManyField(Category)
    image = models.ImageField(null = True,blank=True, upload_to="images/")
    body = models.TextField()
    author = models.ForeignKey(Info, on_delete=models.CASCADE)
    released = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-released']