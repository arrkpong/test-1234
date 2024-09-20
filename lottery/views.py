from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Bet, Lottery, LotteryType
from django.views.generic import TemplateView
from datetime import datetime
import pytz

class LotteryDetailView(TemplateView):
    template_name = 'bet_detail.html'  # Updated to match your template name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lottery_id = self.kwargs.get('pk')
        lottery = get_object_or_404(Lottery, pk=lottery_id)
        
        # Get the current time in Bangkok timezone
        bangkok_tz = pytz.timezone('Asia/Bangkok')
        now = datetime.now(bangkok_tz)
        thai_months = [
            'มกราคม', 'กุมภาพันธ์', 'มีนาคม', 'เมษายน', 'พฤษภาคม', 'มิถุนายน',
            'กรกฎาคม', 'สิงหาคม', 'กันยายน', 'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม'
        ]
        formatted_date = f"{now.day} {thai_months[now.month - 1]} {now.year + 543}"  # Format as Thai date

        context['lottery'] = lottery
        context['lottery_name'] = lottery.name
        context['draw_date'] = formatted_date
        context['total_amount'] = '0฿'  # Replace with actual data
        context['close_time'] = lottery.close_time.strftime('%H:%M:%S')
        return context

    
class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        # ดึงข้อมูลประเภทของหวยทั้งหมด
        lottery_types = LotteryType.objects.all()

        # สร้างดิกชันนารีเพื่อเก็บหวยที่เกี่ยวข้องกับแต่ละประเภท
        lotteries_by_type = {}
        for lottery_type in lottery_types:
            lotteries_by_type[lottery_type] = Lottery.objects.filter(
                lottery_type=lottery_type
            ).order_by('close_time')

        context = {
            'lotteries_by_type': lotteries_by_type
        }
        return render(request, self.template_name, context)
    
class LotteryBetView(View):
    def get(self, request):
        return render(request, 'bet.html')

    def post(self, request):
        bet_type = request.POST.get('bet_type')
        bet_number = request.POST.get('bet_number')
        country = request.POST.get('country')
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        amount = request.POST.get('amount')

        # บันทึกข้อมูลลงในฐานข้อมูล
        Bet.objects.create(
            bet_type=bet_type,
            bet_number=bet_number,
            country=country,
            name=name,
            phone_number=phone_number,
            amount=amount
        )

        messages.success(request, f'แทงหวยสำเร็จ: {bet_type} หมายเลข {bet_number} ยอดเงิน {amount} บาท')

        return redirect('bet')


class BetHistoryView(View):
    def get(self, request):
        bet_type = request.GET.get('bet_type', '')
        country = request.GET.get('country', '')
        start_date = request.GET.get('start_date', '')
        end_date = request.GET.get('end_date', '')

        bets = Bet.objects.all()

        if bet_type:
            bets = bets.filter(bet_type=bet_type)
        if country:
            bets = bets.filter(country=country)
        if start_date:
            bets = bets.filter(placed_at__gte=start_date)
        if end_date:
            bets = bets.filter(placed_at__lte=end_date)

        context = {
            'bets': bets,
            'bet_types': Bet.get_bet_types().items(),  # ใช้ get_bet_types() เพื่อดึงค่าที่แปลแล้ว
            'countries': Bet.get_countries().items(),  # ใช้ get_countries() เพื่อดึงค่าที่แปลแล้ว
        }

        return render(request, 'bet_history.html', context)