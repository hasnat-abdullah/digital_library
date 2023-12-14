import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from config.settings import AUTH_USER_MODEL


class TimeStampedBaseModel(models.Model):
    id = models.UUIDField(verbose_name=_("UUID"), primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True, auto_now=False, editable=False)
    updated_at = models.DateTimeField(
        verbose_name=_("Updated at"), auto_now_add=False, auto_now=True, null=True, blank=True
    )

    class Meta:
        abstract = True


class AuditModel(models.Model):
    created_by = models.ForeignKey(to=AUTH_USER_MODEL, verbose_name=_("Created by"), null=True, blank=True,
                                   related_name="%(class)s_created", on_delete=models.SET_NULL,
                                   )
    updated_by = models.ForeignKey(to=AUTH_USER_MODEL, verbose_name=_("Updated by"), null=True, blank=True,
                                   related_name="%(class)s_updated", on_delete=models.SET_NULL,
                                   )

    class Meta:
        abstract = True
