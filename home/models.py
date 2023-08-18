from django.db import models
from django.utils import timezone


# Copied from VictoriaT87 level_up_loot project
# https://github.com/VictoriaT87/level_up_loot_vt/tree/main
class Contact(models.Model):
    """
    Contact Form that will be posted in the admin
    """
    class Meta:
        # Name for admin panel
        verbose_name = "Contact Request"

    email = models.EmailField(blank=False)
    name = models.CharField(max_length=50, blank=False)
    message = models.TextField(blank=False)
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name}, {self.email}"
