from django.db import models

COUNTRY_CHOICES = [
        ('MY', 'Malaysia'),
        ('IN', 'India'),
        ('CN', 'China'),
        ('KR', 'South Korea'),
        ('QA', 'Qatar'),
    ]

GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('N', 'Prefer not to say'),
    ]
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=7, unique=True, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)
    country = models.CharField(max_length=20, choices=COUNTRY_CHOICES, null=False, blank=False)
    age = models.PositiveIntegerField()
    # after sigining up then only allow changing
    profile_image = models.ImageField(upload_to='images/', default='images/profilepic.jpg')
    is_admin = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False, blank=False)
    
    
    def __str__(self):
        return self.username


#history table 
class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, default='No description')
    keyword = models.CharField(max_length=100, default='No keyword')
    country = models.CharField(max_length=20, choices=COUNTRY_CHOICES, null=False, blank=False) #new add
    offensive = models.BooleanField(null=True, default=None) #new add
    status = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"History for {self.user.username}"