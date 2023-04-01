from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    text = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'block w-full pr-20 mt-1 text-sm text-black dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray form-input',
            'placeholder': 'Type your comment here...',
            'rows': '1'
        })
    )

    class Meta:
        model = Comment
        fields = ('text',)
