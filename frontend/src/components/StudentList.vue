<template>
  <div>
    <h3>Students</h3>
    <ul v-if="students.length > 0">
      <li v-for="student in students" :key="student.id" class="mb-3 p-2 border rounded d-flex justify-content-between align-items-center">
        <div>
          <h5>{{ student.name }}</h5>
          <p>Email: {{ student.email }}</p>
          <p>Status: {{ student.active ? "Active" : "Inactive" }}</p>
        </div>
        <div>
          <button class="btn btn-primary btn-sm me-2" @click="openEditModal(student)">Edit</button>
          <button class="btn btn-danger btn-sm" @click="$emit('delete-student', student.id)">Delete</button>
        </div>
      </li>
    </ul>
    <p v-else>No students found.</p>
    <button @click="openAddModal" class="btn btn-primary mt-3">Add Student</button>

    <!-- Add/Edit Modal -->
    <div v-if="showModal" class="modal show d-block" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{ isEditMode ? "Edit Student" : "Add Student" }}</h5>
            <button type="button" class="btn-close" @click="closeModal"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="isEditMode ? emitEdit() : emitAdd()">
              <input v-model="studentData.name" placeholder="Name" class="form-control mb-2" required />
              <input v-model="studentData.email" placeholder="Email" class="form-control mb-2" required />
              <label class="form-check-label">
                <input type="checkbox" v-model="studentData.active" class="form-check-input"> Active
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
  props: ['students'],
  data() {
    return {
      showModal: false,
      isEditMode: false,
      studentData: { id: null, name: '', email: '', active: true }
    };
  },
  methods: {
    openAddModal() {
      this.showModal = true;
      this.isEditMode = false;
      this.studentData = { name: '', email: '', active: true };
    },
    openEditModal(student) {
      this.showModal = true;
      this.isEditMode = true;
      this.studentData = { ...student };
    },
    closeModal() {
      this.showModal = false;
      this.studentData = { id: null, name: '', email: '', active: true };
    },
    emitAdd() {
      this.$emit('add-student', this.studentData);
      this.closeModal();
    },
    emitEdit() {
      this.$emit('edit-student', this.studentData);
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
