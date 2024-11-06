<template>
  <div class="container pt-3">
    <div class="h1 text-center border rounded bg-light p-2 mb-3">API Client</div>

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

    <div class="tab-content">
      <div id="students" class="tab-pane fade show active">
        <StudentList />
      </div>
      <div id="courses" class="tab-pane fade">
        <CourseList />
      </div>
      <div id="enrollments" class="tab-pane fade">
        <EnrollmentList />
      </div>
    </div>
  </div>
</template>

<script>
import StudentList from './components/StudentList.vue';
import CourseList from './components/CourseList.vue';
import EnrollmentList from './components/EnrollmentList.vue';

export default {
  components: {
    StudentList,
    CourseList,
    EnrollmentList
  }
};
</script>
