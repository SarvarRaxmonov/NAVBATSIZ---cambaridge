
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from django.dispatch import receiver
from .models import Foydalanuvchi, Post_foydalanuvchi

from django.core.signals import request_finished
from django.dispatch import receiver



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Foydalanuvchi.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.foydalanuvchi.save()


@receiver(post_save,sender=Post_foydalanuvchi)
def my_callback(sender, instance,**kwargs):
    print(sender.user)
    
