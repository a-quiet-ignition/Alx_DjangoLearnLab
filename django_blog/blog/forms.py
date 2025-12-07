from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post, Comment, Tag
from taggit.forms import TagWidget

# Forms for User and Profile Update
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'profile_picture', 'phone_number'] 
        
        
# Form for Post Model
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 80}),
            'tags': TagWidget(),
        }
        labels = {
            'content': 'Post Content',
        }  
        
        # Ensure form supports creation of new tags
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['tags'].queryset = Tag.objects.all()
        self.fields['tags'].help_text = 'Select existing tags or add new ones separated by commas.'
        self.fields['tags'].widget.attrs.update({'multiple': 'multiple'})
        self.fields['tags'].to_field_name = 'name'

        

# Comment Form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
        labels = {
            'content': 'Add your comment here',
        }
        
    