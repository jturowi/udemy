from django.contrib import admin

from udemy_api.models import Usuario
# Register your models here.

# admin.site.register(models.Usuario)
# admin.site.register(models.StatusUpdate)
# admin.site.register(models.Message)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'is_active', 'is_staff', 'tipo', 'nombre', 
                    'apellido', 'genero_codigo', 'codigo_gen', 'fecha_gen', 'fecha_nacimiento',
                    'last_login', 'password', 'token')