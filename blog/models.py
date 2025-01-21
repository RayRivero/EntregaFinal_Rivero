from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse
from django.db.models.signals import post_save

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    
    class Meta:
        app_label = 'blog'
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.avatar}"