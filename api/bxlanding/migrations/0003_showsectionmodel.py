# Generated by Django 3.2.6 on 2022-05-29 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bxlanding', '0002_auto_20220529_0527'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowSectionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstVisualtitle', models.CharField(max_length=250)),
                ('firstVisualSubtitle', models.CharField(max_length=250)),
                ('firstVisualThumbnail', models.CharField(blank=True, max_length=500, null=True)),
                ('position', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1)),
                ('detailTitle', models.CharField(max_length=250)),
                ('detailDescriptionTitle', models.CharField(max_length=1000)),
                ('detailSubtitle', models.CharField(max_length=250)),
                ('detailDescriptionSubtitle', models.CharField(max_length=1000)),
                ('videoUrl', models.CharField(max_length=500)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='inactive', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sh_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
