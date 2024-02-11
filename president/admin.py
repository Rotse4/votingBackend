from django.contrib import admin
from django.utils.html import format_html
from . models import Candidate

from django.utils.text import Truncator

# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    model = Candidate
    list_display = ('id', 'name', 'party', 'seat', 'school', 'get_image', 'short_description', 'description', 'votes')

    def get_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
    get_image.short_description = 'Image'

    def short_description(self, obj):
        max_length = 50  # Maximum length of the truncated description
        truncated = Truncator(obj.description).chars(max_length)
        return truncated

    short_description.short_description = 'Description'

    def has_add_permission(self, request):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

admin.site.register(Candidate, CandidateAdmin)