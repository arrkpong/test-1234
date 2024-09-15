from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Lottery
from django.urls import reverse_lazy

# List view for displaying all lotteries
class LotteryListView(ListView):
    model = Lottery
    template_name = 'lottery_list.html'
    context_object_name = 'lotteries'

# Create view for adding new lottery
class LotteryCreateView(CreateView):
    model = Lottery
    fields = ['name', 'close_time', 'result_time']
    template_name = 'lottery_form.html'
    success_url = reverse_lazy('lottery_list')

# Update view for editing an existing lottery
class LotteryUpdateView(UpdateView):
    model = Lottery
    fields = ['name', 'close_time', 'result_time']
    template_name = 'lottery_form.html'
    success_url = reverse_lazy('lottery_list')

# Delete view for deleting a lottery
class LotteryDeleteView(DeleteView):
    model = Lottery
    template_name = 'lottery_confirm_delete.html'
    success_url = reverse_lazy('lottery_list')
