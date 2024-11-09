<template>
  <div>
    <h3>Courses</h3>
    <ul v-if="courses.length > 0">
      <li v-for="course in courses" :key="course.id" class="mb-3 p-2 border rounded d-flex justify-content-between align-items-center">
        <div>
          <h5>{{ course.title }}</h5>
          <p>Credits: {{ course.credits }}</p>
          <p>{{ course.description }}</p>
        </div>
        <div>
          <button class="btn btn-primary btn-sm me-2" @click="openEditModal(course)">Edit</button>
          <button class="btn btn-danger btn-sm" @click="$emit('delete-course', course.id)">Delete</button>
        </div>
      </li>
    </ul>
    <p v-else>No courses found.</p>
    <button @click="openAddModal" class="btn btn-primary mt-3">Add Course</button>

    <!-- Add/Edit Modal -->
    <div v-if="showModal" class="modal show d-block" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{ isEditMode ? "Edit Course" : "Add Course" }}</h5>
            <button type="button" class="btn-close" @click="closeModal"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="isEditMode ? emitEdit() : emitAdd()">
              <input v-model="courseData.title" placeholder="Title" class="form-control mb-2" required />
              <input v-model="courseData.credits" type="number" placeholder="Credits" class="form-control mb-2" required />
              <textarea v-model="courseData.description" placeholder="Description" class="form-control mb-2"></textarea>
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
  props: ['courses'],
  data() {
    return {
      showModal: false,
      isEditMode: false,
      courseData: { id: null, title: '', credits: 0, description: '' }
    };
  },
  methods: {
    openAddModal() {
      this.showModal = true;
      this.isEditMode = false;
      this.courseData = { title: '', credits: 0, description: '' };
    },
    openEditModal(course) {
      this.showModal = true;
      this.isEditMode = true;
      this.courseData = { ...course };
    },
    closeModal() {
      this.showModal = false;
      this.courseData = { id: null, title: '', credits: 0, description: '' };
    },
    emitAdd() {
      this.$emit('add-course', this.courseData);
      this.closeModal();
    },
    emitEdit() {
      this.$emit('edit-course', this.courseData);
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
