<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  },
  ip: {
    type: String,
    required: true
  }
})
</script>

<template>
  <div class="message">
    <h9 class="ip">{{ ip }}</h9>
    <p class="msg">{{ msg }}</p>
  </div>
</template>

<style scoped></style>
