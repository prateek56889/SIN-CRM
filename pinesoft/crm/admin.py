from django.contrib import admin
from .models import clients,Notification
admin.site.site_header="primescore"
admin.site.index_title="primescore"
admin.site.site_title="primescore"
class lst(admin.ModelAdmin):
    list_display=["aadhar","branch","created_by","name","PAN","DOB"]
class notif(admin.ModelAdmin):
    list_display=["name","info","time"]
admin.site.register(clients,lst)
admin.site.register(Notification,notif)