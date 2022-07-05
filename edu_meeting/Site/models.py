from unicodedata import name
from django.db import models
from django.core.validators import MaxLengthValidator
# Create your models here.
class ReseauSite(models.Model):
    name_reseau = models.CharField(max_length=50)
    icon_reseau =  models.CharField(max_length=50)
    link_reseau =  models.URLField(max_length=255)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at =  models.DateTimeField(null=True)
    def __str__(self):
        return self.name_reseau

class Siteweb(models.Model):
    name_site  = models.CharField(max_length=50)
    Number_phone = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)# info@meeting.edu
    adress = models.CharField(max_length=100)# Rio de Janeiro - RJ, 22795-008, Brésil  
    URL_site_web = models.CharField(max_length=100)# www.meeting.edu
    reseau_social = models.ForeignKey(ReseauSite, on_delete=models.CASCADE,related_name="siteweb_reseau_social") 
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at =  models.DateTimeField(null=True)
    def __str__(self):
        return self.name_site

class Banner(models.Model):
    videos = models.FileField(upload_to="banner_video")
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    desc = models.TextField()
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at =  models.DateTimeField(null=True)
    def __str__(self):
        return self.title1

class Service(models.Model):
    title_service = models.CharField(max_length=100)
    icon_service = models.ImageField(upload_to="service_site")
    desc_service = models.TextField()
    is_active = models.BooleanField(default=True) 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at =  models.DateTimeField(null=True)
    def __str__(self):
        return self.title_service

class AboutUniversity(models.Model):
    number_static = models.PositiveIntegerField()
    name_static = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at =  models.DateTimeField(null=True)
    def __str__(self):
        return self.name_static

class BannerMeeting(models.Model):
    image_banner_meeting = models.ImageField(upload_to="banner_meeting")
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at =  models.DateTimeField(null=True)
    def __str__(self):
        return self.title1