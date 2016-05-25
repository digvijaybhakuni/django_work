from django import forms

from blog.models import Post


"""class AuthorForm(forms.Form):
    authorId = forms.AutoField()
    name = forms.CharField(label="Author", max_length=20)
"""

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'datePub']
        widgets = {
            'datePub': forms.DateInput(attrs={'class': 'datepicker'}),
            'content': forms.Textarea(attrs={'class': 'topcoat-textarea', 'rows': '6', 'cols': '30'}),
            'title': forms.TextInput(attrs={'class': 'topcoat-text-input'}),
        }

