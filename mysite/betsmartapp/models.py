from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

User = get_user_model()

class Plan(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    plan = models.CharField(max_length=50, blank=True, null=True)
    is_premium = models.BooleanField(default=False)
    max_daily_bets = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)  # Campo opcional

    def __str__(self):
        return f"Profile of {self.user.username}"
