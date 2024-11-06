<template>
    <div class="container mt-4">
      <h3>Enrollments</h3>
      <div v-if="enrollments && enrollments.length">
        <div v-for="enrollment in enrollments" :key="enrollment.id" class="mb-3 p-2 border rounded d-flex justify-content-between align-items-center">
          <div>
            <h5>{{ enrollment.student__name }} enrolled in {{ enrollment.course__title }}</h5>
            <p>Enrollment Date: {{ enrollment.enrollment_date }}</p>
            <p>Grade: {{ enrollment.grade || "N/A" }}</p>
          </div>
          <div>
            <button class="btn btn-danger btn-sm" @click="deleteEnrollment(enrollment.id)">Delete</button>
          </div>
        </div>
      </div>
      <p v-else>No enrollments found</p>
      <button @click="showAddEnrollmentModal = true" class="btn btn-primary mt-3">Add Enrollment</button>
  
      <!-- Modal to add an enrollment -->
      <div v-if="showAddEnrollmentModal" class="modal show d-block" tabindex="-1">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Add Enrollment</h5>
              <button type="button" class="btn-close" @click="showAddEnrollmentModal = false"></button>
            </div>
            <div class="modal-body">
              <form @submit.prevent="addEnrollment">
                <label>Student:</label>
                <select v-model="newEnrollment.student_id" class="form-control mb-2">
                  <option v-for="student in students" :value="student.id">{{ student.name }}</option>
                </select>
                <label>Course:</label>
                <select v-model="newEnrollment.course_id" class="form-control mb-2">
                  <option v-for="course in courses" :value="course.id">{{ course.title }}</option>
                </select>
                <label>Enrollment Date:</label>
                <input v-model="newEnrollment.enrollment_date" type="date" class="form-control mb-2" />
                <label>Grade:</label>
                <input v-model="newEnrollment.grade" placeholder="Grade" class="form-control mb-2" />
                <button type="submit" class="btn btn-primary mt-3">Save</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        enrollments: [],
        students: [],
        courses: [],
        showAddEnrollmentModal: false,
        newEnrollment: { student_id: "", course_id: "", enrollment_date: "", grade: "" }
      };
    },
    methods: {
      async fetchEnrollments() {
        const response = await fetch("http://127.0.0.1:8000/api/enrollments/");
        this.enrollments = await response.json();
      },
      async fetchStudents() {
        const response = await fetch("http://127.0.0.1:8000/api/students/");
        this.students = await response.json();
      },
      async fetchCourses() {
        const response = await fetch("http://127.0.0.1:8000/api/courses/");
        this.courses = await response.json();
      },
      async addEnrollment() {
        const response = await fetch("http://127.0.0.1:8000/api/enrollments/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(this.newEnrollment)
        });
        const addedEnrollment = await response.json();
        this.enrollments.push(addedEnrollment);
        this.showAddEnrollmentModal = false;
        this.newEnrollment = { student_id: "", course_id: "", enrollment_date: "", grade: "" };
      },
      async deleteEnrollment(id) {
        await fetch(`http://127.0.0.1:8000/api/enrollments/${id}/`, { method: "DELETE" });
        this.enrollments = this.enrollments.filter(enrollment => enrollment.id !== id);
      }
    },
    mounted() {
      this.fetchEnrollments();
      this.fetchStudents();
      this.fetchCourses();
    }
  };
  </script>
  
  <style scoped>
  .modal.show.d-block {
    display: block;
    background: rgba(0, 0, 0, 0.5);
  }
  </style>
  