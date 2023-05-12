<template>
  <div>
    <MovieCard :movies="topMovies"/>
  </div>
</template>

<script>
import axios from 'axios'
import MovieCard from '@/components/MovieCard'

export default {
  name: 'MoviesView',
  data() {
    return {
      topMovies: '',
    }
  },
  components: {
    MovieCard,
  },
  methods: {
    getToprated() {
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
        console.log(this.topMovies)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  created() {
    this.getToprated()
    console.log('불러오기 완료')
  }
}
</script>

<style>

</style>