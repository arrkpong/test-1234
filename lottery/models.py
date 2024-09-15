from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

class Bet(models.Model):
    BET_TYPE_CHOICES = [
        ('two_digit_top', 'สองหลักบน'),
        ('two_digit_bottom', 'สองหลักล่าง'),
        ('three_digit_top', 'สามหลักบน'),
        ('three_digit_mix', 'สามหลักผสม'),
        ('top_run', 'วิ่งบน'),
        ('bottom_run', 'วิ่งล่าง'),
    ]
    
    COUNTRY_CHOICES = [
        ('thailand', 'ประเทศไทย'),
        ('usa', 'สหรัฐอเมริกา'),
        ('uk', 'สหราชอาณาจักร'),
        ('vietnam', 'เวียดนาม'),
        ('laos', 'ลาว'),
    ]

    bet_type = models.CharField(max_length=20, choices=BET_TYPE_CHOICES, verbose_name='ประเภทการแทง')
    bet_number = models.CharField(max_length=10, verbose_name='หมายเลขที่แทง')
    country = models.CharField(max_length=20, choices=COUNTRY_CHOICES, default='thailand', verbose_name='ประเทศ')
    name = models.CharField(max_length=100, verbose_name='ชื่อของผู้แทง', blank=True, null=True)
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="เบอร์โทรศัพท์ไม่ถูกต้อง")],
        verbose_name='เบอร์โทรศัพท์ของผู้แทง',
        blank=True
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)], verbose_name='ยอดเงินที่แทง', blank=True, null=True)
    placed_at = models.DateTimeField(auto_now_add=True, verbose_name='เวลาที่แทง')

    def __str__(self):
        return f'{self.get_bet_type_display()} - {self.bet_number} ({self.get_country_display()}) by {self.name or "Anonymous"}'

    class Meta:
        verbose_name = 'การแทงหวย'
        verbose_name_plural = 'การแทงหวย'


    @classmethod
    def get_bet_types(cls):
        return dict(cls.BET_TYPE_CHOICES)

    @classmethod
    def get_countries(cls):
        return dict(cls.COUNTRY_CHOICES)
