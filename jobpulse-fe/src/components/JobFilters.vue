<script setup lang="ts"></script>

<template>
  <div class="space-y-6">
    <div>
      <h3 class="text-sm font-semibold text-gray-900 mb-3">Job Type</h3>
      <div class="space-y-2">
        <label class="flex items-center">
          <input type="checkbox" class="h-4 w-4 text-blue-600 border-gray-300 rounded" />
          <span class="ml-2 text-sm text-gray-600">Full-time</span>
        </label>
        <label class="flex items-center">
          <input type="checkbox" class="h-4 w-4 text-blue-600 border-gray-300 rounded" />
          <span class="ml-2 text-sm text-gray-600">Part-time</span>
        </label>
        <label class="flex items-center">
          <input type="checkbox" class="h-4 w-4 text-blue-600 border-gray-300 rounded" />
          <span class="ml-2 text-sm text-gray-600">Contract</span>
        </label>
        <label class="flex items-center">
          <input type="checkbox" class="h-4 w-4 text-blue-600 border-gray-300 rounded" />
          <span class="ml-2 text-sm text-gray-600">Remote</span>
        </label>
      </div>
    </div>

    <div>
      <h3 class="text-sm font-semibold text-gray-900 mb-3">Experience Level</h3>
      <div class="space-y-2">
        <label class="flex items-center">
          <input type="checkbox" class="h-4 w-4 text-blue-600 border-gray-300 rounded" />
          <span class="ml-2 text-sm text-gray-600">Entry Level</span>
        </label>
        <label class="flex items-center">
          <input type="checkbox" class="h-4 w-4 text-blue-600 border-gray-300 rounded" />
          <span class="ml-2 text-sm text-gray-600">Mid Level</span>
        </label>
        <label class="flex items-center">
          <input type="checkbox" class="h-4 w-4 text-blue-600 border-gray-300 rounded" />
          <span class="ml-2 text-sm text-gray-600">Senior Level</span>
        </label>
      </div>
    </div>

    <div>
      <h3 class="text-sm font-semibold text-gray-900 mb-3">Salary Range</h3>
      <select
        class="block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm rounded-md"
      >
        <option>All Salaries</option>
        <option>$50k - $80k</option>
        <option>$80k - $120k</option>
        <option>$120k - $150k</option>
        <option>$150k+</option>
      </select>
    </div>
  </div>
</template>
