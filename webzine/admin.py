from django.contrib import admin
from .models import Question, Photo, WebzineContents

# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'content',
    )
    search_fields = [
        'subject',
    ]
admin.site.register(WebzineContents)
admin.site.register(Photo)