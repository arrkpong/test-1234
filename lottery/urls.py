from django.urls import path
from .views import IndexView, LotteryDetailView , LotterryBills

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('bet-detail/<int:pk>/', LotteryDetailView.as_view(), name='lottery_detail'),
    path('bills/',LotterryBills.as_view(), name='bills'),

]
