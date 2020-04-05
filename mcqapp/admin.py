from django.contrib import admin
from .models import Quiz


class Mcq_Admin(admin.ModelAdmin):
    list_display = ('question','option1', 'option2', 'option3', 'option4','is_published','answers') # details displayed in admin page
    list_display_links = ('question','is_published') # link displayed in admin page



# Register your models here.

admin.site.register(Quiz,Mcq_Admin)
