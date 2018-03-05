from django.contrib import admin
from .models import Question, Choice

# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """
    Representation in `Question` admin page
    """
    # fields = ['pub_date', 'question_text']

    fieldsets = [
        ('Date Information', {'fields': ['pub_date']}),
        ('Text Information', {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInline]
    list_display = ['question_text', 'pub_date', 'was_published_recently']


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
