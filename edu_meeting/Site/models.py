from django.db import models

# Create your models here.
class ReseauSite(models.Model):
    name_reseau = models.CharField(max_length=50)
    icon_reseau =  models.CharField(max_length=50)
    link_reseau =  models.URLField(max_length=255)
    si_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at =  models.DateTimeField(null=True)
    def __str__(self):
        return self.name_reseau

class Siteweb(models.Model):
    name  = models.CharField(max_length=50)
    
    reseau_social = models.ForeignKey(ReseauSite, on_delete=models.CASCADE,related_name="siteweb_reseau_social") 
    def __str__(self):
        return self.name
    