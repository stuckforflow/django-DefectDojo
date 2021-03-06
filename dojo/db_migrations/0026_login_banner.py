# Generated by Django 2.2.4 on 2019-12-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0025_jira_security_issuetype'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerConf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_enable', models.BooleanField(blank=True, default=False, null=True)),
                ('banner_message', models.CharField(default='', help_text='This message will be displayed on the login page', max_length=500)),
            ],
        ),
    ]
