from django.contrib import admin
from import_export import resources

from .models import *


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["title", "country"]


@admin.register(Automobile)
class AutomobileAdmin(admin.ModelAdmin):
    list_display = ["title", "manufacturer", "start_year", "end_year"]


@admin.register(Commentaries)
class CommentariesAdmin(admin.ModelAdmin):
    list_display = ["email", "automobile", "comment"]
    readonly_fields = ['create_data']


class AutomobileResource(resources.ModelResource):
    class Meta:
        model = Automobile
        fields = ["id", "title", "manufacturer", "start_year", "end_year"]
        export_order = ("id", "title", "manufacturer", "start_year", "end_year")


class CountryResource(resources.ModelResource):
    class Meta:
        model = Country
        fields = ["id", "title"]
        export_order = ("id", "title")


class ManufacturerResource(resources.ModelResource):
    class Meta:
        model = Manufacturer
        fields = ["id", "title", "country"]
        export_order = ("id", "title", "country")


class CommentariesResource(resources.ModelResource):
    class Meta:
        model = Commentaries
        fields = ["id", "email", "automobile", "create_data", "comment"]
        export_order = ("id", "email", "automobile", "create_data", "comment")