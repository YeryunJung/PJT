<template>
  <div>
    <div v-for="(movie, idx) in movies" :key="idx">
      <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="">
      <div>{{ movie.title }}</div>
      <p>{{ movie.overview }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movies: Object,
  }
}
</script>

<style>

</style>