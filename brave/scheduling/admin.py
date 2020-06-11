from django.contrib import admin
from .models import *

admin.site.register(DigitalEditor)
admin.site.register(GraphicEditor)
admin.site.register(VideoEditor)
admin.site.register(DigitalSchedule)
admin.site.register(VideoEditorSchedule)
admin.site.register(GraphicSchedule)
admin.site.register(PreProductionSchedule)
