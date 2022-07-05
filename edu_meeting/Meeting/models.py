from pickletools import decimalnl_long
from unicodedata import decimal
from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.
class CategoryMeeting(models.Model):
    nome_cate = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    def __str__(self):
        return self.nome_cate


class Meetings(models.Model):
    category = models.ForeignKey(CategoryMeeting, on_delete=models.CASCADE, related_name="Meeting_category")
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="meeting_image")
    date = models.DateField(default=False, null=True)
    desc = models.TextField()
    price = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    is_UPCOMING_meeting = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    
    def __str__(self):
            return self.title


class CoursPop(models.Model):
    image = models.ImageField(upload_to="CoursPop_image")
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    
    def __str__(self):
            return self.title
