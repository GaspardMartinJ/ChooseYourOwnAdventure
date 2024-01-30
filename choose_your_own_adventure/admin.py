from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from choose_your_own_adventure.models import User

admin.site.register(User)