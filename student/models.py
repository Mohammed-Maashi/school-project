from django.db import models

class Students(models.Model):
    student_id = models.IntegerField(unique=True)
    student_name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f"{self.student_id} - {self.student_name}"
