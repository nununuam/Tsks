from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categories(models.Model):
    CATEGORIES = [
        ('Personal', 'Personal'),
        ('Errands', 'Errands'),
        ('Work', 'Work'),
        ('Friends', 'Friends'),
        ('Special Occasion', 'Special Occasion'),
        ('Classes', 'Classes'),
        ('Extracricular', 'Extracricular'),
        ('Random', 'Random'),
        ('Un-assigned', 'Un-assigned')
    ]
    categories = models.CharField(
        max_length=16,
        choices=CATEGORIES,
    )
    
    def __str__(self):
        return self.categories


class Task(models.Model):
    title = models.CharField(max_length = 60)
    categories = models.ManyToManyField(Categories)
    discription = models.CharField(max_length = 250)
    date_time = models.DateTimeField()
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']