from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class UserModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email= models.EmailField(max_length=50, null=True, blank=True)
    mobile= models.IntegerField(null=True, blank=True)
    DEPARTMENTS = (
        ('Software Development','Software Development'),
        ('Machine Learning', 'Machine Learning'),
        ('Application Development', 'Application Development'),
    )
    department = models.CharField(max_length=100, null=True, blank=True, choices=DEPARTMENTS)
    GENDERS = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(max_length=10, choices=GENDERS)
    address = models.TextField(max_length=100, null=True, blank=True)
    LANGUAGES = (
        ('English', 'English'),
        ('French', 'French'),
        ('German', 'German'),
    )
    language = MultiSelectField(max_length=150, null=True, blank=True, choices=LANGUAGES)
    date_created = models.DateTimeField(auto_now_add=True)