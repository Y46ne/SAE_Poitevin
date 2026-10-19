from django.contrib import admin
from .models import Coach, SportsSeason, TrainingOffer, TrainingPrice

admin.site.register((Coach, SportsSeason, TrainingOffer, TrainingPrice))
