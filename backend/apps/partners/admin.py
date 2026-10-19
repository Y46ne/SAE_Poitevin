from django.contrib import admin
from .models import Partner, PartnerCategory, PartnerPlacement

admin.site.register((Partner, PartnerCategory, PartnerPlacement))
