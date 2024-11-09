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
          <button class="btn btn-danger btn-sm" @click="$emit('delete-enrollment', enrollment.id)">Delete</button>
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
            <form @submit.prevent="isEditMode ? emitEdit() : emitAdd()">
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
  props: {
    enrollments: Array,
    students: Array,
    courses: Array
  },
  data() {
    return {
      showEnrollmentModal: false,
      isEditMode: false,
      currentEnrollment: { id: null, student_id: "", course_id: "", enrollment_date: "", grade: "" },
      newEnrollment: { student_id: "", course_id: "", enrollment_date: "", grade: "" }
    };
  },
  methods: {
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
    emitAdd() {
      this.$emit('add-enrollment', this.currentEnrollment);
      this.closeModal();
    },
    emitEdit() {
      this.$emit('edit-enrollment', this.currentEnrollment);
      this.closeModal();
    }
  }
};
</script>

<style scoped>
.modal.show.d-block {
  display: block;
  background: rgba(0, 0, 0, 0.5);
}
</style>