import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useJobStore = defineStore('job', () => {
  const jobs = ref<any[]>([])
  const isLoading = ref(false)
  const error = ref<string | null>(null)
  const searchQuery = ref('')
  const searchLocation = ref('')

  const fetchJobs = async (query?: string, location?: string) => {
    isLoading.value = true
    error.value = null
    searchQuery.value = query || ''
    searchLocation.value = location || ''
    
    try {
      let url = 'http://localhost:8000/search'
      const params = new URLSearchParams()
      
      if (query || location) {
        const q = [query, location].filter(Boolean).join(' ')
        params.append('q', q)
      }
      
      if (params.toString()) {
        url += `?${params.toString()}`
      }

      const response = await fetch(url)
      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.detail || 'Failed to fetch jobs')
      }
      jobs.value = await response.json()
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'An error occurred'
      console.error('Error fetching jobs:', err)
    } finally {
      isLoading.value = false
    }
  }

  return {
    jobs,
    isLoading,
    error,
    searchQuery,
    searchLocation,
    fetchJobs
  }
})
