from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False  # Prevent accidental deletion
    verbose_name = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]

admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), CustomUserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'plan']  # Campos exibidos na lista
    search_fields = ['user__username']