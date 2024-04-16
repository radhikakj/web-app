from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from scientiaarc_app.models import UserProfile

class Attendance(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(auto_now_add=True,null=True)
    button_clicked = models.CharField(max_length=50,null=True)