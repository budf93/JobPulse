<script setup lang="ts">
import { ref, onMounted } from 'vue'
import SearchBar from '../components/SearchBar.vue'
import JobFilters from '../components/JobFilters.vue'
import JobCard from '../components/JobCard.vue'

const jobs = ref<any[]>([])
const isLoading = ref(true)
const error = ref<string | null>(null)

const fetchJobs = async (searchParams?: { query: string; location: string }) => {
  isLoading.value = true
  error.value = null
  try {
    let url = 'http://localhost:8000/search'
    if (searchParams?.query) {
      const q = searchParams.location 
        ? `${searchParams.query} ${searchParams.location}`
        : searchParams.query
      url += `?q=${encodeURIComponent(q)}`
    } else if (searchParams?.location) {
      url += `?q=${encodeURIComponent(searchParams.location)}`
    }
    
    const response = await fetch(url)
    if (!response.ok) throw new Error('Failed to fetch jobs')
    jobs.value = await response.json()
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'An error occurred'
    console.error('Error fetching jobs:', err)
  } finally {
    isLoading.value = false
  }
}

const handleSearch = (params: { query: string; location: string }) => {
  fetchJobs(params)
}

onMounted(() => {
  fetchJobs()
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
            <span v-if="isLoading">Loading jobs...</span>
            <span v-else>Showing {{ jobs.length }} jobs</span>
          </h2>
          <div v-if="!isLoading" class="flex items-center gap-2 text-sm text-gray-600">
            <span>Sort by:</span>
            <select class="border-none bg-transparent font-medium text-gray-900 focus:ring-0">
              <option>Newest</option>
              <option>Salary</option>
            </select>
          </div>
        </div>

        <div v-if="error" class="bg-red-50 text-red-600 p-4 rounded-lg">
          {{ error }}
        </div>

        <div v-if="!isLoading && jobs.length === 0" class="text-center py-12 text-gray-500">
          No jobs found matching your search.
        </div>

        <JobCard v-for="job in jobs" :key="job.id" :job="job" />
      </div>
    </div>
  </div>
</template>
