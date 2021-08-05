from django.contrib import admin

# Register your models here.
from .models import Lead, Agent, User

admin.site.register(Agent)
admin.site.register(Lead)
admin.site.register(User)