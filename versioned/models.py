from django.db import models
from testing.contrib.utils import html
import reversion

class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.title
        
    def save(self, force_insert=False, force_update=False):
        self.title = html.convert_1252_codes(self.title)
        self.description = html.convert_1252_codes(self.description)
        super(Item, self).save(force_insert=force_insert, force_update=force_update)

reversion.register(Item)
