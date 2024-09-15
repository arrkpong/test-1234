from django.urls import path
from .views import IndexView, LotteryBetView, BetHistoryView, LotteryDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('bet/', LotteryBetView.as_view(), name='bet'),
    path('bet-detail/<int:pk>/', LotteryDetailView.as_view(), name='lottery_detail'),
    path('bet-history/', BetHistoryView.as_view(), name='bet_history'),
    # Other URL patterns
]
