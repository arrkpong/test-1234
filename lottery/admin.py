from django.contrib import admin
from .models import Lottery, Bet, LotteryType

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

@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):
    list_display = ('bet_type', 'bet_number', 'country', 'name', 'phone_number', 'amount', 'placed_at')
    search_fields = ('bet_number', 'name', 'phone_number')
    list_filter = ('bet_type', 'country', 'placed_at')
    ordering = ('-placed_at',)
