from django.contrib import admin
from carshare.models import Auto, AutoModel, AutoUser, AutoBrand
from django.utils.safestring import mark_safe


# Register your models here.


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('vin_code',)
    list_filter = ('auto_model__brand', 'status')
    search_fields = ('vin_code',)
    ordering = ('auto_model__brand',)

    def set_status_free(admin_model, request, queryset):
        queryset.update(status='FREE')

    def set_status_booked(admin_model, request, queryset):
        queryset.update(status='INUSE')


@admin.register(AutoModel)
class AutoModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'count_of_auto', )
    list_filter = ('brand',)

    def count_of_auto(self, instance):
        count = Auto.objects.filter(auto_model__vin_code=instance.name).count()
        return count

    count_of_auto.short_description = 'Auto'


class AutoModelInline(admin.TabularInline):
    model = AutoModel


@admin.register(AutoBrand)
class AutoBrandAdmin(admin.ModelAdmin):
    list_display = ('brand',)

    inlines = [AutoModelInline]

    readonly_fields = ('preview',)

    def preview(self, instance: AutoBrand):
        if not instance.image:
            return mark_safe(f'<b>without logo</b>')
        return mark_safe(f'<img src="{instance.image.url_image}" style="max-width: 25px">')


@admin.register(AutoUser)
class AutoUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone',)
