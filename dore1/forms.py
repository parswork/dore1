from django import forms
from .models import UserModel
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'ncode', 'phonenumber', 'rtahsi', 'email','arr']
        labels = {
            'username': 'نام و نام خانوادگی', 
            'ncode': 'شماره ملی', 
            'phonenumber': 'شماره همراه', 
            'rtahsi':'رشته ی تحصیلی',
            'email':'ایمیل',
            'arr':'آدرس' ,
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی', 'class': 'input', 'style': 'text-align: right; display: block;'}),
            'ncode': forms.TextInput(attrs={'placeholder': 'شماره ملی', 'class': 'input', 'style': 'text-align: right; display: block;'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ایمیل', 'class': 'input', 'style': 'text-align: right; display: block;'}),
            'rtahsi': forms.TextInput(attrs={'placeholder': 'رشته ی تحصیلی', 'class': 'input', 'style': 'text-align: right; display: block;'}),
            'phonenumber': forms.TextInput(attrs={'placeholder': 'شماره همراه', 'class': 'input', 'style': 'text-align: right; display: block;'}),
            'arr': forms.TextInput(attrs={'placeholder': 'آدرس', 'class': 'input', 'style': 'text-align: right; display: block;'}),
        }
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if UserModel.objects.filter(email=email).exists():
                raise ValidationError('این ایمیل قبلاً ثبت شده است.')
            return email

        def clean_phonenumber(self):
            phonenumber = self.cleaned_data.get('phonenumber')
            if UserModel.objects.filter(phonenumber=phonenumber).exists():
                raise ValidationError('این شماره همراه قبلاً ثبت شده است.')
            return phonenumber
        