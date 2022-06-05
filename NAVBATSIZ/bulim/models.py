
from datetime import datetime
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from PIL import Image  
from django.utils.timezone import now


class Foydalanuvchi(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
     
        image = models.ImageField(default='7459.jpg',upload_to='profile_pics')   
        location = models.CharField(max_length=300, default='Nomalum')
        ish_vaqti = models.CharField(max_length=100, default='Nomalum')
        korxona_haqida = models.TextField(max_length=1000, default='Nomalum') 
        phone = models.IntegerField(null=True)      
       
     
        def save(self, *args, **kwargs):
             super(Foydalanuvchi, self).save( *args, **kwargs)

             img = Image.open(self.image.path)
             
             if img.height > 300 or img.width > 300 :
                     output_size = (300,300)
                     img.thumbnail(output_size)
                     img.save(self.image.path) 
 
PUL = [
     ("SO'M","SO'M"),
     ("YEVRO","YEVRO"),
     ("DOLLAR","DOLLAR"),
     
]
SOHA = [
     ("Stomotolog","stomotolog"),
     ("duxtir","duxtir")
]



class Post_foydalanuvchi(models.Model):
     user = models.CharField(default='uz',max_length=50)
     user_idsi = models.IntegerField(null=True)
     pul_turi = models.CharField(default="So'm", choices=PUL, max_length=10)
     pub_date = models.DateTimeField(default=now)
     narx = models.IntegerField(null=True, default='0000')
     soha = models.CharField(default='Stomotolog', choices=SOHA, max_length=400)
     qushimcha_malumot = models.TextField(default='Nima uzi bu soha')
     rasm = models.ImageField(default='7459.jpg', upload_to='store')

MEET_TYPE = [
     
     ('OFFLINE','OFFLINE'),
     ('ONLINE','ONLINE')
     
             ]


class Navbat_buyurtma(models.Model):
     korxona_nomi = models.CharField(max_length=340,default='nimadir')
     soha = models.CharField(max_length=50, default='soha')
     time =  models.TimeField(default=now)
     sana = models.DateField(default=now)
     meet_turi = models.CharField(choices=MEET_TYPE, max_length=30, default='nimadir')
     phone_number =  models.IntegerField(default='0000')
         
         
         
         