from django.contrib import admin
from .models.models import CustomUser

@admin.register(CustomUser)
class   CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','email', 'is_menu_manager', 'is_customer')
    list_editable = ('is_menu_manager', 'is_customer')  # Permite editar diretamente na lista