<template>
  <div class="container mt-4">
    <h3>Courses</h3>
    <div v-if="courses && courses.length">
      <div v-for="course in courses" :key="course.id" class="mb-3 p-2 border rounded d-flex justify-content-between align-items-center">
        <div>
          <h5>{{ course.title }}</h5>
          <p>Credits: {{ course.credits }}</p>
          <p>{{ course.description }}</p>
        </div>
        <div>
          <button class="btn btn-primary btn-sm me-2" @click="openEditModal(course)">Edit</button>
          <button class="btn btn-danger btn-sm" @click="deleteCourse(course.id)">Delete</button>
        </div>
      </div>
    </div>
    <p v-else>No courses found</p>
    <button @click="openAddModal" class="btn btn-primary mt-3">Add Course</button>

    <!-- Modal for Adding or Editing a Course -->
    <div v-if="showCourseModal" class="modal show d-block" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{ isEditMode ? "Edit Course" : "Add Course" }}</h5>
            <button type="button" class="btn-close" @click="closeModal"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="isEditMode ? updateCourse() : addCourse()">
              <input v-model="currentCourse.title" placeholder="Title" class="form-control mb-2" required />
              <input v-model="currentCourse.credits" type="number" placeholder="Credits" class="form-control mb-2" required />
              <textarea v-model="currentCourse.description" placeholder="Description" class="form-control mb-2"></textarea>
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
      courses: [],
      showCourseModal: false,
      isEditMode: false,
      currentCourse: { id: null, title: "", description: "", credits: 1 },
      newCourse: { title: "", description: "", credits: 1 }
    };
  },
  methods: {
    async fetchCourses() {
      const response = await fetch("http://127.0.0.1:8000/api/courses/");
      this.courses = await response.json();
    },
    openAddModal() {
      this.showCourseModal = true;
      this.isEditMode = false;
      this.currentCourse = { ...this.newCourse }; // Set to default values
    },
    openEditModal(course) {
      this.showCourseModal = true;
      this.isEditMode = true;
      this.currentCourse = { ...course }; // Populate with existing course data
    },
    closeModal() {
      this.showCourseModal = false;
      this.currentCourse = { id: null, title: "", description: "", credits: 1 };
    },
    async addCourse() {
      const response = await fetch("http://127.0.0.1:8000/api/courses/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.currentCourse)
      });
      const addedCourse = await response.json();
      this.courses.push(addedCourse);
      this.closeModal();
    },
    async updateCourse() {
      const response = await fetch(`http://127.0.0.1:8000/api/courses/${this.currentCourse.id}/`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          title: this.currentCourse.title,
          credits: this.currentCourse.credits,
          description: this.currentCourse.description
        })
      });
      const updatedCourse = await response.json();

      // Update the course in the local list
      const index = this.courses.findIndex(course => course.id === updatedCourse.id);
      this.courses.splice(index, 1, updatedCourse);

      this.closeModal();
    },
    async deleteCourse(id) {
      await fetch(`http://127.0.0.1:8000/api/courses/${id}/`, { method: "DELETE" });
      this.courses = this.courses.filter(course => course.id !== id);
    }
  },
  mounted() {
    this.fetchCourses();
  }
};
</script>
