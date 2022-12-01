from django.contrib import admin
from .models import departments,tickets,fields,knowledgebases,roless,staffss,nuserss

# Register your models here.

admin.site.register(departments)
admin.site.register(tickets)
admin.site.register(fields)
admin.site.register(knowledgebases)
admin.site.register(roless)
admin.site.register(staffss)
admin.site.register(nuserss)



