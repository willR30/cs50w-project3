# Generated by Django 4.0.5 on 2022-06-10 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Autentication', '0002_category_prodcuts_type_orden_item_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]