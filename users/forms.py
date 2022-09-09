from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms


class SignUpForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']
# aşağısı sign upta gereksiz yazıların görünmesini engellemek için
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for fieldname in ['username','email','password1','password2']:
            self.fields[fieldname].help_text=None
            