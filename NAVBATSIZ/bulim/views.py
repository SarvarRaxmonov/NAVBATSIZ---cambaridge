
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from requests import RequestException
from .models import Foydalanuvchi, Navbat_buyurtma, Post_foydalanuvchi
from .forms import CreateUserForm, NavbatForm, Postform, UserUpdateForm , ProfileUpdateForm 

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import sqlite3
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
def MainPage(request):
  
    return render(request, 'bulim/index.html')


def Store(request):
    form = Post_foydalanuvchi.objects.all().order_by('-pub_date')
    context = {"form":form}
    return render(request, 'bulim/st.html', context)



@login_required(login_url='main:login')
def Profile(request):
    eski_nom= str(request.user)
    if request.method == 'POST':
        
         u_form = UserUpdateForm(request.POST,instance=request.user)
         p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.foydalanuvchi)
        
         if u_form.is_valid() and p_form.is_valid():
               newnameuser= u_form.cleaned_data.get('username')
               oldname= eski_nom
               conn = sqlite3.connect('db.sqlite3')
               bb = usercheck(newnameuser)
            
               if newnameuser !='uzbek':      
                    conn.row_factory = sqlite3.Row        
                    c = conn.cursor()
           
                    c.execute(f"SELECT id FROM auth_user WHERE username='{newnameuser}'")
                    
            
                    for i in c:
                      c.execute(f"""UPDATE bulim_post_foydalanuvchi SET user_idsi = ? WHERE user = ?""",(i[0], newnameuser))
                    c.execute(f"""UPDATE bulim_post_foydalanuvchi SET user = ? WHERE user = ?""",(newnameuser,oldname))
                    conn.commit()
                
                
                    u_form.save()
                    p_form.save() 
                    
                    messages.success(request, 'Qoyil yangi malumotlar profilni yangiladi')
                    return redirect('main:profile') 
               else:
                    messages.error(request,"Iltimos boshqa nom tanlang")
           
                    return render(request, 'bulim/User_panel/profile_user.html')
    else:
           u_form = UserUpdateForm(instance=request.user)
           p_form = ProfileUpdateForm(instance=request.user.foydalanuvchi)
    
    context = {
        'u_form':u_form,
        'p_form':p_form,
    }
    
    return render(request, 'bulim/User_panel/pages-profile.html', context)

def usercheck(usernomi):
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row
    d = conn.cursor()
    d.execute("SELECT username FROM auth_user")
    for i in d:
           if usernomi == i['username']:
               return False
           
    return True

@login_required(login_url='main:login')
def Post_joylash(request):
    post = Postform(request.POST)
    if request.method == 'POST':
        pul_type = request.POST["pul_turi"]
        narxi = request.POST["narx"]
        qushimcha_malumotlar = request.POST["qushimcha_malumot"]
        sohasi = request.POST["soha"]
        rasmi =  request.FILES["rasm"]
            
        if sohasi and pul_type and narxi and qushimcha_malumotlar  is not None:
            obj = Post_foydalanuvchi(user=str(request.user),soha=sohasi, rasm=rasmi, pul_turi=pul_type, narx=narxi, qushimcha_malumot=qushimcha_malumotlar)
            obj.save()
            messages.success(request, 'Postingiz yuklandi')
            return redirect('main:post_joylash')
        else:
            messages.error(request, "Postingizda xato bor")
    context = {
        "post":post
    }
    return render(request,'bulim/User_panel/post_joylash.html', context)

@login_required(login_url='main:login')
def User_postlari(request):
    posts = Post_foydalanuvchi.objects.all().order_by('-pub_date')
    context = {
        'post':posts
    }
    return render(request, 'bulim/User_panel/user_postlari.html', context)

@login_required(login_url='main:login')
def delet_post(request, pk):
    post_name = Post_foydalanuvchi.objects.get(id=pk)
    if request.method == 'POST':
        post_name.delete()  
        return redirect('main:postlarim')
    
    return render(request,'bulim/User_panel/delet_uchun.html', {'post_name':post_name})
 
def view_post(request, pk):
    form = NavbatForm(request.POST)
    if request.method == 'POST':
        form = NavbatForm(request.POST)
        if form.is_valid():
            form.save()
            
            
            nomi = request.POST.get("korxona_nomi")
            soha = request.POST.get("soha")
            sana = request.POST.get("sana")
            vaqt = request.POST.get("time")
            meet_turi = request.POST.get("meet_turi")
            phone = request.POST.get("phone_number")
        
          #  messages.success(request,f"nomi: {nomi} <br> soha: {soha} \n vaqti : {vaqt} \n ko'rik turi : {meet_turi} Navbat junatildi  Huddi shu malumotlarni eslatma sifatida telegram botimiz orqali olasiz : @telegram ")
            context = {'formnew':form,'nomi':nomi,'soha':soha,'sana':sana, 'vaqt':vaqt,'meet_turi':meet_turi,"phone":phone }
            return render(request,'bulim/navbat_qabul.html',context) 
            
 
        else:
            messages.error(request,'Hamma malumotlarni tuldiring')
            return redirect('view_post')
    post_all_info = Post_foydalanuvchi.objects.get(id=pk)
    Foydalanuvchi_malumotlari = Foydalanuvchi.objects.all()
    context = {'post_all_infos':post_all_info,        
               'foydalanuvchi_data': Foydalanuvchi_malumotlari,
               "forms":form}   
    return render(request,'bulim/page_view.html',context)            
def qabul_qil(request):
    form = Navbat_buyurtma.objects.all()
    if request.method == 'POST':
        form = NavbatForm(request.POST)
        if form.is_valid():
            form.save()
            
            return render(request,'view_post',context) 
        else:
            messages.error(request,'Hamma malumotlarni tuldiring')
            return redirect('view_post')
    context = {'form':form}
    return render(request,'bulim/navbat_qabul.html',context) 

@login_required(login_url='main:login')
def navbatlar(request):
    navbatlar = Navbat_buyurtma.objects.all()
    return render(request,'bulim/User_panel/st.html',{'navbatlar':navbatlar})
# faqat bitta userning postini delete va update uchun Class ishlatdik 




class PostUpdateView(LoginRequiredMixin, UpdateView):
       model = Post_foydalanuvchi
       form_class = Postform
       template_name = 'bulim/User_panel/update_uchun.html'
       def get_success_url(self):
           return reverse('main:postlarim')
       def get_queryset(self):
                 
           return Post_foydalanuvchi.objects.filter(user=self.request.user)
       


    
    
   
           
#################################################### Register and login va logout #####################################


def RegisterPage(request):
    
    if request.user.is_authenticated:
        return redirect('main:home')
    else:
        form = CreateUserForm(request.POST)
        if request.method == 'POST':
            
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.cleaned_data.get('username')
                form.save()      
                messages.success(request, 'Siz register buldingiz ' + user)    
                return redirect('main:login')
            
            else:
                messages.info(request, 'Parol yoki email xato , Parol misol : Twist2004?')  
        return render(request,'bulim/registration.html',{'form':form})

def LoginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
              login(request, user)
              return redirect('main:home')
        else:
            messages.error(request, 'Parol yoki username xato')
            return redirect('main:login')
    return render(request,'bulim/login.html')   


def logoutUser(request):
    logout(request)
    return redirect('main:login')     




