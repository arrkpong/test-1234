# lottery/models.py
from django.db import models

class LotteryType(models.Model):
    name = models.CharField(max_length=100, verbose_name='ประเภทหวย')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ประเภทหวย'
        verbose_name_plural = 'ประเภทหวย'

class Lottery(models.Model):
    lottery_type = models.ForeignKey(LotteryType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='ประเภทหวย')
    name = models.CharField(max_length=100, verbose_name='ชื่อหวย')
    close_time = models.TimeField(verbose_name='เวลาปิดรับ')
    result_time = models.TimeField(verbose_name='เวลาออกผล')
    image = models.ImageField(upload_to='lottery_images/', null=True, blank=True, verbose_name='รูปภาพหวย')

    def __str__(self):
        return f"{self.name} ({self.lottery_type})"

    class Meta:
        verbose_name = 'หวย'
        verbose_name_plural = 'หวย'

class Bet(models.Model):
    lottery = models.ForeignKey(Lottery, on_delete=models.CASCADE, verbose_name='หวยที่เดิมพัน')
    number = models.CharField(max_length=10, verbose_name='เลขที่เดิมพัน')
    top = models.CharField(max_length=10, null=True, blank=True, verbose_name='บน')
    bottom = models.CharField(max_length=10, null=True, blank=True, verbose_name='ล่าง')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='วันที่เดิมพัน')

    def __str__(self):
        return f"Bet {self.number} on {self.lottery.name}"

    class Meta:
        verbose_name = 'โพยเดิมพัน'
        verbose_name_plural = 'โพยเดิมพัน'