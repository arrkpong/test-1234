from django.db import models

class Lottery(models.Model):
    name = models.CharField(max_length=100)  # ชื่อหวย
    close_time = models.TimeField()  # เวลาปิดรับ
    result_time = models.TimeField()  # เวลาออกผล
    image = models.ImageField(upload_to='lottery_images/', null=True, blank=True)  # รูปภาพหวย (optional)

    def __str__(self):
        return self.name
