from django.contrib import admin
from .models import project
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.
class projectAdmin(admin.ModelAdmin):
    fields = ["project_title", "project_content","project_link_title", "project_link", "project_image"]

formfield_overrides = {
    models.TextField: {'widget': TinyMCE()}
}

admin.site.register(project, projectAdmin)