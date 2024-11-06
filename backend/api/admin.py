from django.contrib import admin
from .models import Student, Course, Enrollment

# Inline display for Enrollment within Student and Course
class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1  # Number of empty slots for new enrollments in the inline form

# Register Enrollment model
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date')
    search_fields = ('student__name', 'course__title')
    model = Enrollment
    extra = 1  # Number of empty slots for new enrollments in the inline form

# Register Student model with Enrollment inline
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'active')
    search_fields = ('name', 'email')
    inlines = [EnrollmentInline]

# Register Course model with Enrollment inline
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'credits')
    search_fields = ('title',)
    inlines = [EnrollmentInline]
