<script setup lang="ts">
import { RouterLink } from 'vue-router'

defineProps<{
  job: {
    id: number
    title: string
    company: string
    location: string
    type: string
    salary: string
    postedAt: string
  }
}>()
</script>

<template>
  <div
    class="bg-white p-6 shadow-sm rounded-lg border border-transparent hover:border-blue-300 transition-all"
  >
    <div class="flex justify-between items-start">
      <div>
        <h2 class="text-xl font-bold text-gray-900 hover:text-blue-600 transition-colors">
          <RouterLink :to="`/job/${job.id}`">{{ job.title }}</RouterLink>
        </h2>
        <p class="text-gray-600 font-medium">{{ job.company }}</p>
      </div>
      <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
        {{ job.type }}
      </span>
    </div>
    <div class="mt-4 flex items-center gap-4 text-sm text-gray-500">
      <div class="flex items-center gap-1">
        <svg
          class="h-4 w-4"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
          ></path>
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
          ></path>
        </svg>
        {{ job.location }}
      </div>
      <div class="flex items-center gap-1">
        <svg
          class="h-4 w-4"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
          ></path>
        </svg>
        {{ job.salary }}
      </div>
      <div class="flex items-center gap-1">
        <svg
          class="h-4 w-4"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
          ></path>
        </svg>
        {{ job.postedAt }}
      </div>
    </div>
  </div>
</template>
