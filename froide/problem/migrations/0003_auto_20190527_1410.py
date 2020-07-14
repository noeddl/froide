# Generated by Django 2.1.8 on 2019-05-27 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0002_auto_20181107_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemreport',
            name='kind',
            field=models.CharField(choices=[('bounce_publicbody', 'You received a bounce mail from the public body.'), ('message_not_delivered', 'Your message was not delivered.'), ('attachment_broken', "The attachments don't seem to work."), ('redaction_needed', 'You need more redaction.'), ('foi_help_needed', 'You need help to understand or reply to this message.'), ('other', 'Something else...')], max_length=50),
        ),
    ]