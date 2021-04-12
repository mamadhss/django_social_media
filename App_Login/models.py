from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    profile_pic = models.ImageField(upload_to = 'profile_pics',blank=True)
    dob = models.DateField(blank=True,null=True)
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)


class Follow(models.Model):
    following = models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')
    follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower')




"""  A post_save signal received when a User instance is created """

@receiver(signals.post_save,sender=User)
def profile_receiver(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)


