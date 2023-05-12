const fetch = require('node-fetch');

// TMDB API 키
const apiKey = '84216c3a0ee24447b6798e642dbfa540';

// 인기 있는 영화 목록 가져오기
const apiUrl = `https://api.themoviedb.org/3/movie/top_rated?api_key=${apiKey}&language=ko-KR`;

const fetchRecommendMovie = async (recommend) => {
  const desiredGenreId = parseInt(recommend[Math.floor(Math.random() * recommend.length)]);
  
  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    
    const movies = data.results;
    const filteredMovies = movies.filter(movie => {
      return movie.genre_ids.includes(desiredGenreId);
    });
    
    if (filteredMovies.length === 0) {
      return movies[Math.floor(Math.random() * movies.length)];
    } else {
      const randomIndex = Math.floor(Math.random() * filteredMovies.length);
      return filteredMovies[randomIndex];
    }
  } catch (error) {
    console.log('Failed to fetch top rated movies:', error);
    throw error;
  }
};

export { fetchRecommendMovie };