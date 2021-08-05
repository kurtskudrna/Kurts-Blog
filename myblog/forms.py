from django import forms
from .models import BlogComments, Category, Post

# create form fields for model
catnames = Category.objects.all().values_list('catname', 'catname')
catlist = []

for cat in catnames:
    catlist.append(cat)


class CreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'author', 'value': '', 'type': 'hidden'}),
            'category': forms.Select(choices=catlist, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=catlist, attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComments
        fields = ('user', 'comment')

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }
