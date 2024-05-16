from django.contrib import admin
from map.models import Types, Cardss, Areas


# admin.site.register(Cardss)
#admin.site.register(Types)

@admin.register(Cardss)
class CardssAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Areas)
class AreasAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
