function getSentiment(){
  var requestOptions = {
    method: 'POST',
    redirect: 'follow',
    mode: 'cors'
  };
  return fetch("http://localhost:5001/api/v1/average_sentiment", requestOptions)
    .then(response => response.text())
    .then(result => {
      return result;
    })
    .catch(error => console.log('error', error));
}
