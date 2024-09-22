from django.urls import path
from .views import IndexView, LotteryDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('bet-detail/<int:pk>/', LotteryDetailView.as_view(), name='lottery_detail'),
    
]
