<template>
  <div id="app">
    <!-- <span>{{weather_data}}</span> -->
    <!-- <span>{{genreId}}</span> -->
    <h2>훈이 전용 영화(반박시 최예훈)</h2>
    <img :src="`https://image.tmdb.org/t/p/w500${recommend_movie?.poster_path}`" alt="">
    <p>{{recommend_movie?.title}}</p>
  </div>
</template>

<script>
import {fetchWeather, recommend} from "@/api/index"
import {fetchRecommendMovie} from "@/api/recommend"



export default {
  name: 'App',
  data(){
    return{
      weather_data : null,
      movie_data : null,
      genreId : null,
      recommend_movie : null,
    }
  },
  methods: {
    async weather() {
      try {
        const response = await fetchWeather();
        const data = await response.json();
        this.weather_data = data.weather[0].main;
        this.genreId = recommend(this.weather_data)
        this.recommend_movie = await fetchRecommendMovie(this.genreId)
        
      }
      catch(err) {
        console.log(err)
      }
  }},
  async created() {
    await this.weather()
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>