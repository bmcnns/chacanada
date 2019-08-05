from django.contrib import admin
from .models import Post, Event, Volunteer, Item, User

# Register your models here.
admin.site.register(Post)
admin.site.register(Event)
admin.site.register(Volunteer)
admin.site.register(Item)
admin.site.register(User)