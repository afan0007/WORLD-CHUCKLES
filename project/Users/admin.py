from django.contrib import admin

# Register your models here.
from .models import User, History # Replace 'User' with your custom user model

admin.site.register(User)


admin.site.register(History)