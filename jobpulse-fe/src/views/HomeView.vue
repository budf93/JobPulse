<script setup lang="ts">
import { onMounted } from 'vue'
import { useJobStore } from '../stores/job'
import SearchBar from '../components/SearchBar.vue'
import JobFilters from '../components/JobFilters.vue'
import JobCard from '../components/JobCard.vue'

const jobStore = useJobStore()

const handleSearch = (params: { query: string; location: string }) => {
  jobStore.fetchJobs(params.query, params.location)
}

onMounted(() => {
  jobStore.fetchJobs()
})
</script>

<template>
  <div class="space-y-8">
    <section>
      <h1 class="text-3xl font-bold text-gray-900 mb-2">Find your next dream job</h1>
      <p class="text-gray-600 mb-6">Browse through thousands of job opportunities across the globe.</p>
      <SearchBar @search="handleSearch" />
    </section>

    <div class="flex flex-col md:flex-row gap-8">
      <aside class="w-full md:w-64 flex-shrink-0">
        <JobFilters />
      </aside>

      <div class="flex-grow space-y-4">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-lg font-semibold text-gray-900">
            <span v-if="jobStore.isLoading">Loading jobs...</span>
            <span v-else>Showing {{ jobStore.jobs.length }} jobs</span>
          </h2>
          <div v-if="!jobStore.isLoading" class="flex items-center gap-2 text-sm text-gray-600">
            <span>Sort by:</span>
            <select class="border-none bg-transparent font-medium text-gray-900 focus:ring-0">
              <option>Newest</option>
              <option>Salary</option>
            </select>
          </div>
        </div>

        <div v-if="jobStore.error" class="bg-red-50 text-red-600 p-4 rounded-lg">
          {{ jobStore.error }}
        </div>

        <div v-if="!jobStore.isLoading && jobStore.jobs.length === 0" class="text-center py-12 text-gray-500">
          No jobs found matching your search.
        </div>

        <JobCard v-for="job in jobStore.jobs" :key="job.id" :job="job" />
      </div>
    </div>
  </div>
</template>
