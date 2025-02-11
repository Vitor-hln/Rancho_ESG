from django.contrib.auth.models import Group, permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from app_accounts.models.models import CustomUser