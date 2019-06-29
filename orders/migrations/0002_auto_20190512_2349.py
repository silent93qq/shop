# Generated by Django 2.2 on 2019-05-12 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cartitem_line_total'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='cart.Cart'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='abc', max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Обзвон', 'Обзвон'), ('пох', 'пох'), ('finished', 'finished')], default='Обзвон', max_length=120),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
