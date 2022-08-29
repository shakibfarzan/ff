from django.db import models
from django.core.validators import FileExtensionValidator

class ContactField(models.Model):
    name = models.CharField(max_length=255, unique=True)
    value = models.TextField()
    link = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    

def nameFile(instance, filename):
    return '/'.join(['profile', filename])
    
class Bio(models.Model):
    name = models.CharField(max_length=255)
    profile = models.ImageField(upload_to=nameFile, validators=[FileExtensionValidator(["jpeg", "jpg", "png"])])
    bio = models.TextField()
    
    def __str__(self):
        return "BIO"
    