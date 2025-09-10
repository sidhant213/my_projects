from django.conf import settings
from django import forms
from .models import reigister
class RegisterForm(forms.ModelForm):
    class Meta:
        model = reigister
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
            'pro_pic': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not str(phone).isdigit():
            raise forms.ValidationError("Phone number must be numeric.")
        return phone