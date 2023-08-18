from django.contrib import admin
from .models import Contact


# Copied from VictoriaT87 level_up_loot project
# https://github.com/VictoriaT87/level_up_loot_vt/tree/main
@admin.register(Contact)
class Contact(admin.ModelAdmin):
    """
    Set displays for Contact Form Submissions on the admin panel
    """

    list_display = ("name", "email", "date_posted")
    search_fields = ("name",)
