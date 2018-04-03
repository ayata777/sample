from django.contrib import admin
from .models import Question,Answer,Good,Bad

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Good)
admin.site.register(Bad)
