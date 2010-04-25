from django.shortcuts import render_to_response
from testing.versioned.models import Item

def item(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {'item': item}
    return render_to_response("item.html", context)
