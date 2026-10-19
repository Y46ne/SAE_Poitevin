from django.contrib import admin
from .models import AdministrativeDocument, ClubHistoryEntry, ClubProfile, ClubStaffMember

admin.site.register((AdministrativeDocument, ClubHistoryEntry, ClubProfile, ClubStaffMember))
