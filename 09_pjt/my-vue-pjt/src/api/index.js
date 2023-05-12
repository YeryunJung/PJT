const apiKey = '7b5bb97f41130e89e5310193fef63921';
// 날씨를 가져올 도시의 이름
const city = 'Seoul';
// API 요청 URL 생성
const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;

function fetchWeather(){
  return fetch(apiUrl)
}
const recommend = weather =>{
  if (weather=="Clear"){
    const recommend_list = ['28', '12', '16']
    return recommend_list
  }
  else if(weather=="Clouds"){
    const recommend_list = ['35', '80', '99']
    return recommend_list
  }
  else if(weather=="Rain"){
    const recommend_list = ['18', '10751', '14']
    return recommend_list
  }
  else if(weather=="Snow"){
    const recommend_list = ['36', '27', '10402']
    return recommend_list
  }
  else{
    const recommend_list = ['9648', '10749', '878']
    return recommend_list
  }
  
}

export {fetchWeather, recommend}
