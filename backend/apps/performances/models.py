from django.conf import settings
from django.db import models


class Performance(models.Model):
    class Status(models.TextChoices):
        UPLOADED = "UPLOADED", "Subida"
        QUEUED = "QUEUED", "En cola"
        PROCESSING = "PROCESSING", "Procesando"
        COMPLETED = "COMPLETED", "Completada"
        FAILED = "FAILED", "Fallida"

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="performances",
    )
    routine = models.ForeignKey(
        "routines.Routine",
        on_delete=models.PROTECT,
        related_name="performances",
    )
    video = models.FileField(upload_to="performances/%Y/%m/", blank=True)
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.UPLOADED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.student} · {self.routine}"
