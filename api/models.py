from django.db import models


class TrackingAttributes(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True


class SoftDeleteAttribute(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True


class Account(TrackingAttributes, SoftDeleteAttribute):
    email = models.EmailField()

    class Meta:
        db_table = "accounts"


class Todo(TrackingAttributes):
    task = models.CharField(max_length=180)
    completed = models.BooleanField(default=False, blank=True)

    class Meta:
        db_table = "todos"

    def __str__(self):
        return f"{self.task}"
