from django.conf import settings
from django.db import models


class Routine(models.Model):
    class Difficulty(models.TextChoices):
        BEGINNER = "BEGINNER", "Principiante"
        INTERMEDIATE = "INTERMEDIATE", "Intermedio"
        ADVANCED = "ADVANCED", "Avanzado"

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="routines",
    )
    difficulty = models.CharField(max_length=16, choices=Difficulty.choices)
    master_video = models.FileField(upload_to="routines/%Y/%m/", blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.name
