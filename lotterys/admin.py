from django.contrib import admin
from .models import Lottery

class LotteryAdmin(admin.ModelAdmin):
    list_display = ('name', 'close_time', 'result_time', 'image_tag')
    
    readonly_fields = ['image_tag']
    
    def image_tag(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" />'
        return "-"
    
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

admin.site.register(Lottery, LotteryAdmin)
