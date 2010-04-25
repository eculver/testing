from django.contrib import admin
from reversion.admin import VersionAdmin
from testing.versioned.models import Item

class ItemAdmin(VersionAdmin):
    pass

admin.site.register(Item, ItemAdmin)