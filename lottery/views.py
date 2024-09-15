from django.contrib import messages
from django.shortcuts import redirect
from django.views import View
from django.shortcuts import render
from .models import Bet

class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name, {'success': False})

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