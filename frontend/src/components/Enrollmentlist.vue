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
            <button class="btn btn-primary btn-sm me-2" @click="openEditModal(enrollment)">Edit</button>
            <button class="btn btn-danger btn-sm" @click="deleteEnrollment(enrollment.id)">Delete</button>
          </div>
        </div>
      </div>
      <p v-else>No enrollments found</p>
      <button @click="openAddModal" class="btn btn-primary mt-3">Add Enrollment</button>
  
      <!-- Modal for Adding or Editing an Enrollment -->
      <div v-if="showEnrollmentModal" class="modal show d-block" tabindex="-1">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">{{ isEditMode ? "Edit Enrollment" : "Add Enrollment" }}</h5>
              <button type="button" class="btn-close" @click="closeModal"></button>
            </div>
            <div class="modal-body">
              <form @submit.prevent="isEditMode ? updateEnrollment() : addEnrollment()">
                <label>Student:</label>
                <select v-model="currentEnrollment.student_id" class="form-control mb-2">
                  <option v-for="student in students" :value="student.id">{{ student.name }}</option>
                </select>
                <label>Course:</label>
                <select v-model="currentEnrollment.course_id" class="form-control mb-2">
                  <option v-for="course in courses" :value="course.id">{{ course.title }}</option>
                </select>
                <label>Enrollment Date:</label>
                <input v-model="currentEnrollment.enrollment_date" type="date" class="form-control mb-2" />
                <label>Grade:</label>
                <input v-model="currentEnrollment.grade" placeholder="Grade" class="form-control mb-2" />
                <button type="submit" class="btn btn-primary mt-3">{{ isEditMode ? "Save Changes" : "Save" }}</button>
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
        showEnrollmentModal: false,
        isEditMode: false,
        currentEnrollment: { id: null, student_id: "", course_id: "", enrollment_date: "", grade: "" },
        newEnrollment: { student_id: "", course_id: "", enrollment_date: "", grade: "" },
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
        openAddModal() {
        this.showEnrollmentModal = true;
        this.isEditMode = false;
        this.currentEnrollment = { ...this.newEnrollment };
        },
        openEditModal(enrollment) {
        this.showEnrollmentModal = true;
        this.isEditMode = true;
        this.currentEnrollment = { ...enrollment }; // Populate fields with current data
        },
        closeModal() {
        this.showEnrollmentModal = false;
        this.currentEnrollment = { id: null, student_id: "", course_id: "", enrollment_date: "", grade: "" };
        },
        async addEnrollment() {
        const response = await fetch("http://127.0.0.1:8000/api/enrollments/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(this.currentEnrollment)
        });
        const addedEnrollment = await response.json();
        this.enrollments.push(addedEnrollment);
        this.closeModal();
        },
        async updateEnrollment() {
        const response = await fetch(`http://127.0.0.1:8000/api/enrollments/${this.currentEnrollment.id}/`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(this.currentEnrollment)
        });
        const updatedEnrollment = await response.json();
        
        // Update the enrollment in the local list
        const index = this.enrollments.findIndex(enrollment => enrollment.id === updatedEnrollment.id);
        this.enrollments.splice(index, 1, updatedEnrollment);
        
        this.closeModal();
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
