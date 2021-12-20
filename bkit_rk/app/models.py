from django.db import models


class Processor(models.Model):
    name = models.CharField(max_length=256, verbose_name="processor name")
    frequency = models.FloatField(verbose_name="processor frequency")

    def __str__(self):
        return self.name


class Computer(models.Model):
    name = models.CharField(max_length=256, verbose_name="computer name")
    processor = models.ForeignKey(
        Processor,
        on_delete=models.SET_DEFAULT,
        null=True,
        default=None,
        related_name="computers"
    )

    def __str__(self):
        return self.name
