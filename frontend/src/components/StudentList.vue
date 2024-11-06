<template>
  <div class="container mt-4">
    <h3>Students</h3>
    <div v-if="students && students.length">
      <div v-for="student in students" :key="student.id" class="mb-3 p-2 border rounded d-flex justify-content-between align-items-center">
        <div>
          <h5>{{ student.name }}</h5>
          <p>Email: {{ student.email }}</p>
          <p>Status: {{ student.active ? "Active" : "Inactive" }}</p>
        </div>
        <div>
          <button class="btn btn-primary btn-sm me-2" @click="openEditModal(student)">Edit</button>
          <button class="btn btn-danger btn-sm" @click="deleteStudent(student.id)">Delete</button>
        </div>
      </div>
    </div>
    <p v-else>No students found</p>
    <button @click="openAddModal" class="btn btn-primary mt-3">Add Student</button>

    <!-- Modal for Adding or Editing a Student -->
    <div v-if="showStudentModal" class="modal show d-block" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{ isEditMode ? "Edit Student" : "Add Student" }}</h5>
            <button type="button" class="btn-close" @click="closeModal"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="isEditMode ? updateStudent() : addStudent()">
              <input v-model="currentStudent.name" placeholder="Name" class="form-control mb-2" required />
              <input v-model="currentStudent.email" placeholder="Email" class="form-control mb-2" required />
              <label class="form-check-label">
                <input type="checkbox" v-model="currentStudent.active" class="form-check-input"> Active
              </label>
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
      students: [],
      showStudentModal: false,
      isEditMode: false,
      currentStudent: { id: null, name: "", email: "", active: true }
    };
  },
  methods: {
    async fetchStudents() {
      const response = await fetch("http://127.0.0.1:8000/api/students/");
      this.students = await response.json();
    },
    openAddModal() {
      this.showStudentModal = true;
      this.isEditMode = false;
      this.currentStudent = { name: "", email: "", active: true };
    },
    openEditModal(student) {
      this.showStudentModal = true;
      this.isEditMode = true;
      this.currentStudent = { ...student }; // Populate fields with current data
    },
    closeModal() {
      this.showStudentModal = false;
      this.currentStudent = { id: null, name: "", email: "", active: true };
    },
    async addStudent() {
      const response = await fetch("http://127.0.0.1:8000/api/students/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.currentStudent)
      });
      const addedStudent = await response.json();
      this.students.push(addedStudent);
      this.closeModal();
    },
    async updateStudent() {
      const response = await fetch(`http://127.0.0.1:8000/api/students/${this.currentStudent.id}/`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.currentStudent)
      });
      const updatedStudent = await response.json();

      // Update the student in the local list
      const index = this.students.findIndex(student => student.id === updatedStudent.id);
      this.students.splice(index, 1, updatedStudent);

      this.closeModal();
    },
    async deleteStudent(id) {
      await fetch(`http://127.0.0.1:8000/api/students/${id}/`, { method: "DELETE" });
      this.students = this.students.filter(student => student.id !== id);
    }
  },
  mounted() {
    this.fetchStudents();
  }
};
</script>

<style scoped>
.modal.show.d-block {
  display: block;
  background: rgba(0, 0, 0, 0.5);
}
</style>
