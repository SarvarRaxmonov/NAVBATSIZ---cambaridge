
from django.urls import path
from . import views
from .views import PostUpdateView
app_name = 'main'
urlpatterns = [
     path('home/',views.Store, name='home'), 
     path('register/',views.RegisterPage, name='register'), ################
     path('login/',views.LoginPage, name='login'), #####################
     path('profile/', views.Profile, name='profile'), ##############################################3
     path('post_joylash/', views.Post_joylash, name='post_joylash'), #########################################
     path('postlarim/', views.User_postlari, name='postlarim'), 
     path('logout/', views.logoutUser, name='logout') , ###############################3
     path('delet/<int:pk>', views.delet_post, name='delet') , #########################################
     path('detail/<int:pk>', views.view_post, name='view_post'),
     path('navbatlar/',views.navbatlar, name='navbatlar'),
   # Faqat update lar uchun generic viewlar ishlatilindi projectda   
     path('update/<int:pk>', PostUpdateView.as_view(), name="update" ) , ##########################
  
]  
 
 
 
 
 
 
 
 






