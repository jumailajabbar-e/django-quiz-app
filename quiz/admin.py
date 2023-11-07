

# Register your models here.
from django.contrib import admin
from .models import Question, Choice
class ChoiceInline(admin.TabularInline):  # or admin.StackedInline for a different display style
    model = Choice
    extra = 3  # You can adjust the number of choices displayed

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
# admin.site.register(Question)
# admin.site.register(Choice)



