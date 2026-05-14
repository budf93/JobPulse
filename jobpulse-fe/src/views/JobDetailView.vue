<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const jobId = route.params.id

// Mock data for detail
const job = {
  id: jobId,
  title: 'Senior Frontend Engineer',
  company: 'TechFlow',
  location: 'Remote',
  type: 'Full-time',
  salary: '$120k - $160k',
  postedAt: '2 days ago',
  description: `
    <p class="mb-4">We are looking for a Senior Frontend Engineer to join our growing team. You will be responsible for building and maintaining the user interface of our core products.</p>
    <h3 class="text-lg font-bold mb-2">Requirements:</h3>
    <ul class="list-disc pl-5 mb-4">
      <li>5+ years of experience with modern JavaScript frameworks (Vue, React, or Angular)</li>
      <li>Strong understanding of CSS and responsive design</li>
      <li>Experience with TypeScript</li>
      <li>Excellent communication skills</li>
    </ul>
    <h3 class="text-lg font-bold mb-2">Benefits:</h3>
    <ul class="list-disc pl-5 mb-4">
      <li>Competitive salary and equity</li>
      <li>Remote-first culture</li>
      <li>Flexible working hours</li>
      <li>Health and dental insurance</li>
    </ul>
  `,
}
</script>

<template>
  <div class="max-w-4xl mx-auto">
    <button
      @click="router.back()"
      class="flex items-center text-blue-600 hover:text-blue-800 mb-6 transition-colors"
    >
      <svg
        class="h-5 w-5 mr-1"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M10 19l-7-7m0 0l7-7m-7 7h18"
        ></path>
      </svg>
      Back to jobs
    </button>

    <div class="bg-white shadow-sm rounded-lg overflow-hidden">
      <div class="p-8 border-b border-gray-100">
        <div class="flex justify-between items-start">
          <div>
            <h1 class="text-3xl font-bold text-gray-900">{{ job.title }}</h1>
            <p class="text-xl text-blue-600 font-medium mt-1">{{ job.company }}</p>
          </div>
          <button class="bg-blue-600 text-white px-8 py-3 rounded-lg font-bold hover:bg-blue-700 shadow-md transition-all">
            Apply Now
          </button>
        </div>

        <div class="mt-6 flex flex-wrap gap-6 text-gray-600">
          <div class="flex items-center gap-2">
            <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
            {{ job.location }}
          </div>
          <div class="flex items-center gap-2">
            <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
            </svg>
            {{ job.type }}
          </div>
          <div class="flex items-center gap-2">
            <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            {{ job.salary }}
          </div>
        </div>
      </div>

      <div class="p-8 prose prose-blue max-w-none text-gray-700" v-html="job.description"></div>
    </div>
  </div>
</template>
