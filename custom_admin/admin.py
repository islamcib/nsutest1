from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

class CustomAdminSite(admin.AdminSite):
    site_header = _('Административная панель НГУ')
    site_title = _('Административная панель НГУ')
    index_title = _('Добро пожаловать в административную панель')

    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        # Сортируем приложения в нужном порядке
        app_ordering = {
            'main': 1,
            'faculties': 2,
            'news': 3,
            'education': 4,
            'science': 5,
            'contacts': 6,
            'applicants': 7,
        }
        app_list.sort(key=lambda x: app_ordering.get(x['app_label'], 999))
        return app_list

# Создаем экземпляр кастомной админ-панели
custom_admin_site = CustomAdminSite(name='custom_admin')

# Регистрируем модели
custom_admin_site.register(User, CustomUserAdmin) 