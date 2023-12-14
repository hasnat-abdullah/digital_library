from datetime import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import TimeStampedBaseModel, AuditModel
from django.core.validators import MaxValueValidator, MinValueValidator


class Book(TimeStampedBaseModel, AuditModel):
    author = models.ForeignKey(to="user.User", related_name="BookAuthor",
                               verbose_name=_("Author"), on_delete=models.RESTRICT, db_index=True
                               )
    title = models.CharField(max_length=500, verbose_name=_("Book Title"), db_index=True)
    isbn = models.CharField(max_length=18, verbose_name=_("International Standard Book Number"), unique=True,
                            db_index=True)
    publication_year = models.PositiveSmallIntegerField(verbose_name=_("Publication Year"), db_index=True,
                                                        validators=[MinValueValidator(1000),
                                                                    MaxValueValidator(datetime.now().year)])
    brief_summary = models.TextField(verbose_name=_("Brief Summary"))
