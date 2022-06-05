import imp
from attr import field

from django.contrib.auth.forms import UserCreationForm
from django import forms 

from django.contrib.auth.models import User
from .models import Foydalanuvchi, Navbat_buyurtma, Post_foydalanuvchi 

class CreateUserForm(UserCreationForm):
      class Meta:
          model = User
          fields = ['username','email','password1','password2'] 
  
          
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']         
 
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Foydalanuvchi
        fields = ['image','location','ish_vaqti','korxona_haqida','phone']     
     
class Postform(forms.ModelForm):
    class Meta:
        model = Post_foydalanuvchi
        fields = ['narx','soha','qushimcha_malumot','rasm','pul_turi']
class NavbatForm(forms.ModelForm):
    class Meta:
        model = Navbat_buyurtma
        fields = ['korxona_nomi','soha','time','sana','meet_turi','phone_number']
        
        