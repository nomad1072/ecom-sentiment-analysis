function getTopNProds(){
  var raw = "";

  var requestOptions = {
    method: 'POST',
    body: raw,
    redirect: 'follow',
    mode: 'cors'
  };

  return fetch("http://localhost:5001/api/v1/topN", requestOptions)
    .then(response => response.text())
    .then(result => {
      return result;
    })
    .catch(error => console.log('error', error));
}
