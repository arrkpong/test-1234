# Generated by Django 5.1.1 on 2024-09-15 13:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0003_alter_bet_options_bet_name_bet_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='ยอดเงินที่แทง'),
        ),
        migrations.AlterField(
            model_name='bet',
            name='bet_type',
            field=models.CharField(choices=[('two_digit_top', 'สองหลักบน'), ('two_digit_bottom', 'สองหลักล่าง'), ('three_digit_top', 'สามหลักบน'), ('three_digit_mix', 'สามหลักผสม'), ('top_run', 'วิ่งบน'), ('bottom_run', 'วิ่งล่าง')], max_length=20, verbose_name='ประเภทการแทง'),
        ),
        migrations.AlterField(
            model_name='bet',
            name='country',
            field=models.CharField(choices=[('thailand', 'ประเทศไทย'), ('usa', 'สหรัฐอเมริกา'), ('uk', 'สหราชอาณาจักร'), ('vietnam', 'เวียดนาม'), ('laos', 'ลาว')], default='thailand', max_length=20, verbose_name='ประเทศ'),
        ),
    ]
