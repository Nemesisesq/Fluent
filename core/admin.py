from django.contrib import admin
from core.models import *

# Register your models here.
admin.site.register(Campaign, admin.ModelAdmin)
admin.site.register(Customer, admin.ModelAdmin)
admin.site.register(Ambassador, admin.ModelAdmin)
admin.site.register(FacebookPoint, admin.ModelAdmin)
admin.site.register(TwitterPoint, admin.ModelAdmin)
admin.site.register(Signup, admin.ModelAdmin)
