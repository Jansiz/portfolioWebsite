from django.contrib import admin
from .models import contact, project, skills
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.
class projectAdmin(admin.ModelAdmin):
    fields = ["project_title", "project_content","project_link_title", "project_link", "project_image"]

formfield_overrides = {
    models.TextField: {'widget': TinyMCE()}
}


class contactAdmin(admin.ModelAdmin):

     fields = ["First_Name", "Last_Name","Email", "Subject", "Body"]



class skillsAdmin(admin.ModelAdmin):

     fields = ["skill_title", "skill_image", "skill_file"]

admin.site.register(project, projectAdmin)
admin.site.register(contact, contactAdmin)
admin.site.register(skills, skillsAdmin)
