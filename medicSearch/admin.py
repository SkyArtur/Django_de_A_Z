from django.contrib import admin
from medicSearch.models import *


admin.site.register(Speciality)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(Rating)
admin.site.register(DayWeek)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    @admin.display(description='Nascimento')
    def birth(self, obj):
        if obj.birthday:
            return obj.birthday.strftime('%d/%m/%Y')

    @admin.display(description='Especialidades')
    def specialties_list(self, obj):
        return [field.name for field in obj.specialties.all()]

    @admin.display(description='Endereços')
    def addresses_list(self, obj):
        return [field.name for field in obj.addresses.all()]

    fieldsets = (
        ('Usuário', {
            'fields': ('user', 'birthday', 'image')
        }),
        ('Função', {
            'fields': ('role',)
        }),
        ('Extras', {
            'fields': ('specialties', 'addresses')
        }),
    )
    list_display = ('id', 'user', 'role', 'birth', 'specialties_list', 'addresses_list')
    list_display_links = ('id', 'user')
    list_filter = ('user__is_active', 'role')
    # fields = ('user', ('role',), 'image', 'birthday', 'specialties', 'addresses')
    readonly_fields = ('user',)
    search_fields = ('user__username',)
    date_hierarchy = 'created_at'
    empty_value_display = 'Vazio'
    ordering = ('user', 'id')
    birth.empty_value_display = "__/__/__"

    # class Media:
    #     css = {'all': ('css/custom.css',)}
    #     js = {'all': ('css/custom.js',)}


