from django.contrib import admin
from django.utils.html import format_html
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ('id', 'ism', 'familya', 'yosh', 'email', 'phon', 'image_tag')
    search_fields = ('ism', 'familya', 'email', 'phon', 'slug')
    list_filter = ('yosh',)
    ordering = ('-id',)
    list_per_page = 10

    readonly_fields = ('slug',)

    def image_tag(self, obj):
        if obj.picture:
            return format_html(
                '<img src="{}" width="40" style="border-radius:50%;" />',
                obj.picture.url
            )
        return "Rasm topilmadi"

    image_tag.short_description = "Rasm"