from django.contrib import admin

from cars.models import Color, Brand, CarModel, Order


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', )

    list_filter = ('name',)

    search_fields = ('name', )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', )

    list_filter = ('name',)

    search_fields = ('name', )


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):

    list_display = ('name',)

    list_filter = ('name',)

    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ('amount', 'date')

    list_filter = ('date',)

    search_fields = ('date',)
