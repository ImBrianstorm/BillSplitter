"""User's admin"""

from django.contrib import admin

from .models import Splitter

admin.site.register(Splitter)
