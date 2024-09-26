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

class Bills(models.Model):
    product = models.CharField(max_length=100, verbose_name='สินค้า')
    date = models.DateField(verbose_name='ประจำวันที่')
    time = models.TimeField(verbose_name='เวลา')
    status = models.CharField(max_length=20, verbose_name='สถานะ')
    total = models.IntegerField(verbose_name='ยอดรวม')
    correct = models.IntegerField(verbose_name='ถูก', default=0)
    remaining = models.IntegerField(verbose_name='คงเหลือ', default=0)
    note = models.TextField(null=True, blank=True, verbose_name='note')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='วันที่สร้าง')

    def __str__(self):
        return f"Bill {self.product} on {self.date}"

    class Meta:
        verbose_name = 'บิล'
        verbose_name_plural = 'บิล'