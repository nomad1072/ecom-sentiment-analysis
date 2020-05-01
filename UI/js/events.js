function getEventCounts(category){
  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  var raw = JSON.stringify(category);

  var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow',
    mode: 'cors'
  };

  return fetch("http://localhost:5001/api/v1/event_count", requestOptions)
    .then(response => response.text())
    .then(result => {
      return result;
    })
    .catch(error => console.log('error', error));
}
