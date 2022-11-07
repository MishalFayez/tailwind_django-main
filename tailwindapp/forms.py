from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import CommentPost, CommentProject, Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('subject', 'email', 'body')
        subject_class = "bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-indigo-500"
        email_class = "bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-indigo-500"
        body_class = "block p-2.5 h-24 w-full bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-indigo-500"
        widgets = {
            'subject': TextInput(attrs = {
                'class': subject_class,

                'placeholder': 'Subject'
            },
            ),
            'email': EmailInput(attrs = {
                'class': email_class,
                'placeholder': 'Email'
            },
            ),
            'body': Textarea(attrs = {
                'class': body_class,
                'placeholder': 'Your message..'
            },
            )
        }
        labels = {
            'subject': '',
            'email': '',
            'body': ''
        }

class CommentPForm(forms.ModelForm):
    class Meta:
        model = CommentProject
        fields = ('name', 'email', 'body')
        name_class = "block py-2.5 px-0 w-full text-base text-gray-700 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:border-gray-600 dark:focus:border-indigo-500 focus:outline-none focus:ring-0 focus:border-indigo-600 peer"
        email_class = "block py-2.5 px-0 w-full text-base text-gray-700 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:border-gray-600 dark:focus:border-indigo-500 focus:outline-none focus:ring-0 focus:border-indigo-600 peer"
        body_class = "block py-2.5 px-0 w-full text-base text-gray-700 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:border-gray-600 dark:focus:border-indigo-500 focus:outline-none focus:ring-0 focus:border-indigo-600 peer max-h-32"
        widgets = {
            'name': TextInput(attrs = {
                'class': name_class,
                'placeholder': 'Name'
            },
            ),
            'email': EmailInput(attrs = {
                'class': email_class,
                'placeholder': 'Email'
            },
            ),
            'body': Textarea(attrs = {
                'class': body_class,
                'placeholder': 'Your message..'
            },
            )
        }
        labels = {
            'name': '',
            'email': '',
            'body': ''
        }

class CommentPostForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = ('name', 'email', 'body')
        name_class = "block py-2.5 px-0 w-full text-base text-gray-700 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:border-gray-600 dark:focus:border-indigo-500 focus:outline-none focus:ring-0 focus:border-indigo-600 peer"
        email_class = "block py-2.5 px-0 w-full text-base text-gray-700 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:border-gray-600 dark:focus:border-indigo-500 focus:outline-none focus:ring-0 focus:border-indigo-600 peer"
        body_class = "block py-2.5 px-0 w-full text-base text-gray-700 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:border-gray-600 dark:focus:border-indigo-500 focus:outline-none focus:ring-0 focus:border-indigo-600 peer max-h-32"
        widgets = {
            'name': TextInput(attrs = {
                'class': name_class,
                'placeholder': 'Name'
            },
            ),
            'email': EmailInput(attrs = {
                'class': email_class,
                'placeholder': 'Email'
            },
            ),
            'body': Textarea(attrs = {
                'class': body_class,
                'placeholder': 'Your message..'
            },
            )
        }
        labels = {
            'name': '',
            'email': '',
            'body': ''
        }