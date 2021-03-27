from django.contrib import admin

from .models import Company


class CompanyAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False


admin.site.register(Company, CompanyAdmin)
