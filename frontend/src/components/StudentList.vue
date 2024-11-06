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
          <button class="btn btn-danger btn-sm" @click="deleteStudent(student.id)">Delete</button>
        </div>
      </div>
    </div>
    <p v-else>No students found</p>
    <button @click="showAddStudentModal = true" class="btn btn-primary mt-3">Add Student</button>

    <!-- Modal to add a student -->
    <div v-if="showAddStudentModal" class="modal show d-block" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add Student</h5>
            <button type="button" class="btn-close" @click="showAddStudentModal = false"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="addStudent">
              <input v-model="newStudent.name" placeholder="Name" class="form-control mb-2" required />
              <input v-model="newStudent.email" placeholder="Email" class="form-control mb-2" required />
              <label class="form-check-label">
                <input type="checkbox" v-model="newStudent.active" class="form-check-input"> Active
              </label>
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
      students: [],
      showAddStudentModal: false,
      newStudent: { name: "", email: "", active: true }
    };
  },
  methods: {
    async fetchStudents() {
      const response = await fetch("http://127.0.0.1:8000/api/students/");
      this.students = await response.json();
    },
    async addStudent() {
      const response = await fetch("http://127.0.0.1:8000/api/students/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.newStudent)
      });
      const addedStudent = await response.json();
      this.students.push(addedStudent);
      this.showAddStudentModal = false;
      this.newStudent = { name: "", email: "", active: true }; // Reset the new student modal
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
