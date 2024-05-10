from django.contrib import admin
from map.models import Types,Cardss

# admin.site.register(Cardss)
#admin.site.register(Types)

@admin.register(Cardss)
class CardssAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}