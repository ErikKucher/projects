# Generated by Django 4.1.5 on 2023-06-08 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0004_littleimage_userimage_remove_qrcode_user_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='little_user_img',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='editor.littleimage'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qrcode',
            name='user_img',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='editor.userimage'),
            preserve_default=False,
        ),
    ]