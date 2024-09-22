#lottery\views.py
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from lottery.models import Bet, Lottery, LotteryType
from datetime import datetime
import json
import pytz

class LotteryDetailView(TemplateView):
    template_name = 'bet_detail.html'

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
        context['draw_date'] = formatted_date
        return context

    def post(self, request, *args, **kwargs):
        lottery_id = self.kwargs.get('pk')
        lottery = get_object_or_404(Lottery, pk=lottery_id)

        # Get bet data from form
        bet_data = request.POST.get('bet_data')
        if bet_data:
            bets = json.loads(bet_data)

            for bet in bets:
                Bet.objects.create(
                    lottery=lottery,
                    number=bet['number'],
                    top=bet['top'] if bet['top'] else None,
                    bottom=bet['bottom'] if bet['bottom'] else None
                )

            # Optionally, add a success message
            messages.success(request, "โพยของคุณถูกบันทึกเรียบร้อยแล้ว")

        return redirect('lottery_detail', pk=lottery_id)  # Redirect to the same page after submitting


    
class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        # ดึงข้อมูลประเภทของหวยทั้งหมด
        lottery_types = LotteryType.objects.all()

        # สร้างดิกชันนารีเพื่อเก็บหวยที่เกี่ยวข้องกับแต่ละประเภท
        lotteries_by_type = {}
        for lottery_type in lottery_types:
            lotteries_by_type[lottery_type] = Lottery.objects.filter(lottery_type=lottery_type)

        context = {
            'lotteries_by_type': lotteries_by_type
        }
        return render(request, self.template_name, context)