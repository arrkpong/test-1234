from django.urls import path
from .views import LotteryListView, LotteryCreateView, LotteryUpdateView, LotteryDeleteView

urlpatterns = [
    path('lottery', LotteryListView.as_view(), name='lottery_list'),
    path('add/', LotteryCreateView.as_view(), name='lottery_add'),
    path('edit/<int:pk>/', LotteryUpdateView.as_view(), name='lottery_edit'),
    path('delete/<int:pk>/', LotteryDeleteView.as_view(), name='lottery_delete'),
]
