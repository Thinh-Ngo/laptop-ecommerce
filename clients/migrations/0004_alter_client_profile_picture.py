# Generated by Django 3.2.3 on 2021-05-31 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_client_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='profile_picture',
            field=models.ImageField(blank=True, default='niceblog/blog-2_zq82wf.jpg', null=True, upload_to=''),
        ),
    ]
