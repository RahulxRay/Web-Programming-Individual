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
          <button class="btn btn-danger btn-sm" @click="deleteCourse(course.id)">Delete</button>
        </div>
      </div>
    </div>
    <p v-else>No courses found</p>
    <button @click="showAddCourseModal = true" class="btn btn-primary mt-3">Add Course</button>

    <!-- Modal to add a course -->
    <div v-if="showAddCourseModal" class="modal show d-block" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add Course</h5>
            <button type="button" class="btn-close" @click="showAddCourseModal = false"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="addCourse">
              <input v-model="newCourse.title" placeholder="Title" class="form-control mb-2" required />
              <input v-model="newCourse.credits" type="number" placeholder="Credits" class="form-control mb-2" required />
              <textarea v-model="newCourse.description" placeholder="Description" class="form-control mb-2"></textarea>
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
      courses: [],
      showAddCourseModal: false,
      newCourse: { title: "", description: "", credits: 1 }
    };
  },
  methods: {
    async fetchCourses() {
      const response = await fetch("http://127.0.0.1:8000/api/courses/");
      this.courses = await response.json();
    },
    async addCourse() {
      const response = await fetch("http://127.0.0.1:8000/api/courses/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.newCourse)
      });
      const addedCourse = await response.json();
      this.courses.push(addedCourse);
      this.showAddCourseModal = false;
      this.newCourse = { title: "", description: "", credits: 1 };
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

<style scoped>
.modal.show.d-block {
  display: block;
  background: rgba(0, 0, 0, 0.5);
}
</style>
