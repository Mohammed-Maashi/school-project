from django.contrib import admin
from .models import Students

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ("student_id", "student_name")
    search_fields = ("student_id", "student_name")
    ordering = ("student_id",)
