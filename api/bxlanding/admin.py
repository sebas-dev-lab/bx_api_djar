from django.contrib import admin
from .models import *

admin.site.site_header = "Barux Admin Panel"
admin.site.site_title = "Portal de Administracion"
admin.site.index_title = "Bienvenido al Portal de Administracion de Barux"

admin.site.register(FirstSectionModel)
admin.site.register(AboutSectionModel)
admin.site.register(ShowSectionModel)
admin.site.register(PresentationModel)
