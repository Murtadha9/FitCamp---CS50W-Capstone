from django import forms
from .models import Comment

class RecipeSearchForm(forms.Form):
    search_query = forms.CharField(label='' , max_length=100)


####################################################

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']