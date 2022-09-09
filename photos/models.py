from django.db import models
from django.core.validators import FileExtensionValidator
from categories.models import Category, SubCategory

def nameFile(instance, filename):
    return '/'.join(['images', filename])

class Photo(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    src = models.ImageField(upload_to=nameFile, validators=[FileExtensionValidator(["jpeg", "jpg", "png"])])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.src.path}"
    

