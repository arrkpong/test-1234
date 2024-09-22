from django.contrib import admin
from .models import Lottery, LotteryType

@admin.register(LotteryType)
class LotteryTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Lottery)
class LotteryAdmin(admin.ModelAdmin):
    list_display = ('lottery_type', 'name', 'close_time', 'result_time', 'image')
    search_fields = ('name',)
    list_filter = ('lottery_type', 'close_time', 'result_time')


