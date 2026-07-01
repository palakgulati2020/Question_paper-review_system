from decimal import Decimal
from django.db import migrations, models
from django.core.validators import MinValueValidator


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_exam_max_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='weightage',
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal('100.00'),
                help_text='Exam contribution weight (recommended total across course = 100).',
                max_digits=6,
                validators=[MinValueValidator(Decimal('0.01'))],
            ),
        ),
    ]
