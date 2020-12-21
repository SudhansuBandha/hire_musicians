from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import *

class TeamAdmin(admin.ModelAdmin):
    
    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display=('id','myphoto','first_name','role','created_date')
    
    #this will make first_name to be a clickable
    list_display_links =('first_name','id')

    #fields for searching based on parameter
    search_fields = ('first_name', 'role')

    #field for filtering based on the parameter
    list_filter = ('role',)


admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)