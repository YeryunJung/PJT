<template>
  <div>
    <img :src="`https://image.tmdb.org/t/p/w500${randomMovie.poster_path}`" alt="">
    <div>{{ randomMovie.title }}</div>
    <p>{{ randomMovie.overview }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'RandomView',
  data() {
    return {
      topMovies: '',
      randomMovie: '',
    }
  },
  methods: {
    getRandom() {
      const BASE_URL = 'https://api.themoviedb.org/3/movie/top_rated'
      const params = {
        'api_key': '8189d7f86439a7dd168ff05d6e420fb5',
      }
      
      axios({
        method: 'get',
        url: BASE_URL,
        params: params,
      })
      .then((res) => {
        this.topMovies = res.data.results
        const randomNum = Math.floor(Math.random() * 20);
        this.randomMovie = this.topMovies[randomNum]
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  created() {
    this.getRandom()
    console.log('불러오기 완료')
  }
}
</script>

<style>

</style>