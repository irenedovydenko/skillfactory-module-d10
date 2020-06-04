from random import choice

from django.contrib import admin

from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(CarAdmin, self).get_form(request, obj, **kwargs)

        form.base_fields['year'].initial = choice(range(1900, 2021))
        form.base_fields['transmission'].initial = choice(range(1, 4))
        form.base_fields['color'].initial = choice(range(1, 10))
        form.base_fields['vendor'].initial = 'Kia'

        return form
