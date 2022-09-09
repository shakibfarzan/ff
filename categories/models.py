from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name