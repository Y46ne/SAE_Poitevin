from django.contrib import admin
from .models import OpenDraw, OpenDrawMatch, OpenEdition, OpenEditorial, OpenPhoto, OpenProgramItem


@admin.register(OpenEdition)
class OpenEditionAdmin(admin.ModelAdmin):
    list_display = ("year", "title", "is_current", "is_archived", "is_published")
    list_filter = ("is_current", "is_archived", "is_published")
    search_fields = ("title", "subtitle", "description")


admin.site.register((OpenDraw, OpenDrawMatch, OpenEditorial, OpenPhoto, OpenProgramItem))
