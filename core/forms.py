from django import forms
from .models import Comment, Subscription


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'description')

        widgets = {
            'description': forms.Textarea(attrs={'rows': '8'})
        }


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('email',)

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Your Email Address'})
        }

