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
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_per_page = 5
    date_hierarchy = 'pub_date'


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
