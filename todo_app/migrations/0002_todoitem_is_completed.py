from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
