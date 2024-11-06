from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student, Course, Enrollment
import json
from datetime import datetime

def test_api_view(request):
    return JsonResponse({
        'message': 'Good response!'
    })

@csrf_exempt
def student_list(request):
    if request.method == "GET":
        students = list(Student.objects.values())
        return JsonResponse(students, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        student = Student.objects.create(name=data["name"], email=data["email"], active=data["active"])
        return JsonResponse({"id": student.id, "name": student.name, "email": student.email, "active": student.active})

@csrf_exempt
def student_detail(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return JsonResponse({"error": "Student not found"}, status=404)

    if request.method == "DELETE":
        student.delete()
        return JsonResponse({"message": "Student deleted"})

@csrf_exempt
def course_list(request):
    """Handles GET and POST for courses."""
    if request.method == "GET":
        courses = list(Course.objects.values())
        return JsonResponse(courses, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        course = Course.objects.create(
            title=data["title"], description=data["description"], credits=data["credits"]
        )
        return JsonResponse({
            "id": course.id, "title": course.title, "description": course.description, "credits": course.credits
        })

@csrf_exempt
def course_detail(request, course_id):
    """Handles DELETE for courses."""
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return JsonResponse({"error": "Course not found"}, status=404)

    if request.method == "DELETE":
        course.delete()
        return JsonResponse({"message": "Course deleted"})
    

@csrf_exempt
def enrollment_list(request):
    """Handles GET and POST for enrollments."""
    if request.method == "GET":
        enrollments = list(Enrollment.objects.select_related('student', 'course').values(
            'id', 'student__name', 'course__title', 'enrollment_date', 'grade'
        ))
        return JsonResponse(enrollments, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        student = Student.objects.get(id=data["student_id"])
        course = Course.objects.get(id=data["course_id"])
        enrollment = Enrollment.objects.create(
            student=student,
            course=course,
            enrollment_date=datetime.strptime(data["enrollment_date"], '%Y-%m-%d'),
            grade=data.get("grade", "")
        )
        return JsonResponse({
            "id": enrollment.id,
            "student": enrollment.student.name,
            "course": enrollment.course.title,
            "enrollment_date": enrollment.enrollment_date,
            "grade": enrollment.grade
        })

@csrf_exempt
def enrollment_detail(request, enrollment_id):
    """Handles DELETE for enrollments."""
    try:
        enrollment = Enrollment.objects.get(id=enrollment_id)
    except Enrollment.DoesNotExist:
        return JsonResponse({"error": "Enrollment not found"}, status=404)

    if request.method == "DELETE":
        enrollment.delete()
        return JsonResponse({"message": "Enrollment deleted"})