<template>
  <div class="container pt-3">
    <h1 class="text-center mb-4">Rahul's school </h1>

    <!-- Tabs for Students, Courses, and Enrollments -->
    <ul class="nav nav-tabs">
      <li class="nav-item">
        <a class="nav-link active" data-bs-toggle="tab" href="#students">Students</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" data-bs-toggle="tab" href="#courses">Courses</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" data-bs-toggle="tab" href="#enrollments">Enrollments</a>
      </li>
    </ul>

    <div class="tab-content mt-4">
      <div id="students" class="tab-pane fade show active">
        <StudentList 
          :students="students" 
          @add-student="addStudent" 
          @edit-student="editStudent" 
          @delete-student="deleteStudent" 
        />
      </div>
      <div id="courses" class="tab-pane fade">
        <CourseList 
          :courses="courses" 
          @add-course="addCourse" 
          @edit-course="editCourse" 
          @delete-course="deleteCourse" 
        />
      </div>
      <div id="enrollments" class="tab-pane fade">
        <EnrollmentList 
          :enrollments="enrollments" 
          :students="students" 
          :courses="courses" 
          @add-enrollment="addEnrollment" 
          @edit-enrollment="editEnrollment" 
          @delete-enrollment="deleteEnrollment" 
        />
      </div>
    </div>
  </div>
</template>

<script>
import StudentList from './components/StudentList.vue';
import CourseList from './components/CourseList.vue';
import EnrollmentList from './components/Enrollmentlist.vue';

export default {
  components: {
    StudentList,
    CourseList,
    EnrollmentList
  },
  data() {
    return {
      students: [],
      courses: [],
      enrollments: []
    };
  },
  methods: {
    // Fetch all data on mount
    async fetchData() {
      await Promise.all([
        this.fetchStudents(),
        this.fetchCourses(),
        this.fetchEnrollments()
      ]);
    },

    // API Call Methods

    // Students
    async fetchStudents() {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/students/");
        const data = await response.json();
        this.students = data;
      } catch (error) {
        console.error("Error fetching students:", error);
      }
    },
    async addStudent(student) {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/students/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(student)
        });
        const newStudent = await response.json();
        this.students.push(newStudent);
      } catch (error) {
        console.error("Error adding student:", error);
      }
    },
    async editStudent(updatedStudent) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/students/${updatedStudent.id}/`, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(updatedStudent)
        });
        const data = await response.json();
        const index = this.students.findIndex(student => student.id === data.id);
        if (index !== -1) {
          this.students.splice(index, 1, data);
        }
      } catch (error) {
        console.error("Error editing student:", error);
      }
    },
    async deleteStudent(studentId) {
      try {
        await fetch(`http://127.0.0.1:8000/api/students/${studentId}/`, {
          method: "DELETE"
        });
        this.students = this.students.filter(student => student.id !== studentId);
      } catch (error) {
        console.error("Error deleting student:", error);
      }
    },

    // Courses
    async fetchCourses() {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/courses/");
        const data = await response.json();
        this.courses = data;
      } catch (error) {
        console.error("Error fetching courses:", error);
      }
    },
    async addCourse(course) {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/courses/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(course)
        });
        const newCourse = await response.json();
        this.courses.push(newCourse);
      } catch (error) {
        console.error("Error adding course:", error);
      }
    },
    async editCourse(updatedCourse) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/courses/${updatedCourse.id}/`, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(updatedCourse)
        });
        const data = await response.json();
        const index = this.courses.findIndex(course => course.id === data.id);
        if (index !== -1) {
          this.courses.splice(index, 1, data);
        }
      } catch (error) {
        console.error("Error editing course:", error);
      }
    },
    async deleteCourse(courseId) {
      try {
        await fetch(`http://127.0.0.1:8000/api/courses/${courseId}/`, {
          method: "DELETE"
        });
        this.courses = this.courses.filter(course => course.id !== courseId);
      } catch (error) {
        console.error("Error deleting course:", error);
      }
    },

    // Enrollments
    async fetchEnrollments() {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/enrollments/");
        const data = await response.json();
        this.enrollments = data;
      } catch (error) {
        console.error("Error fetching enrollments:", error);
      }
    },
    async addEnrollment(enrollment) {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/enrollments/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(enrollment)
        });
        const newEnrollment = await response.json();
        this.enrollments.push(newEnrollment);
      } catch (error) {
        console.error("Error adding enrollment:", error);
      }
    },
    async editEnrollment(updatedEnrollment) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/enrollments/${updatedEnrollment.id}/`, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(updatedEnrollment)
        });
        const data = await response.json();
        const index = this.enrollments.findIndex(enrollment => enrollment.id === data.id);
        if (index !== -1) {
          this.enrollments.splice(index, 1, data);
        }
      } catch (error) {
        console.error("Error editing enrollment:", error);
      }
    },
    async deleteEnrollment(enrollmentId) {
      try {
        await fetch(`http://127.0.0.1:8000/api/enrollments/${enrollmentId}/`, {
          method: "DELETE"
        });
        this.enrollments = this.enrollments.filter(enrollment => enrollment.id !== enrollmentId);
      } catch (error) {
        console.error("Error deleting enrollment:", error);
      }
    }
  },
  mounted() {
    this.fetchData();
  }
};
</script>

<style scoped>
/* Optional styling */
.modal.show.d-block {
  display: block;
  background: rgba(0, 0, 0, 0.5);
}
</style>