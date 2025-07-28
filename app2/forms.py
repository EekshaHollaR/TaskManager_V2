from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class contactForm(forms.Form):
    name=forms.CharField(label="name", max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'username','required':True}))
    email=forms.CharField(label="email", max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email','required':True}))
    message=forms.CharField(label="message",max_length=500, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your messsage','required':True}))

    def clean(self):
        cleaned_data=super().clean()
        if self.errors:
            return self.cleaned_data
        valid_name=cleaned_data['name']

        if len(valid_name)<3:
            raise forms.ValidationError("Minimum of 3 Characters")
        

# class studentForm(forms.ModelForm):
#     name=forms.CharField(max_length=50)
#     age=forms.IntegerField()
    
#     class Meta:
#         models:student_info
#         fields:"__all__"

class registerForm(forms.ModelForm):
    username=forms.CharField(label="username", max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username','required':True}))
    email=forms.EmailField(label="email", max_length=40 , widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email','required':True}))
    password=forms.CharField(label="password", max_length=50 ,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Password','required':True}))
    confirm_password=forms.CharField(label="confirm_password", max_length=50 ,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Confirm password','required':True}))

    def clean(self):
        cleaned_data=super().clean()
        if self.errors:
            return self.cleaned_data
        valid_password=cleaned_data['password']
        valid_confirm_password=cleaned_data['confirm_password']

        if valid_password!= valid_confirm_password:
            raise forms.ValidationError("Password Mismatched")
    
    class Meta:
        model=User
        fields=['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class loginForm(forms.Form):
    username=forms.CharField(label="username", max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username','required':True}))
    password=forms.CharField(label="password", max_length=50 ,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Password','required':True}))
    