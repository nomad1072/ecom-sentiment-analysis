function plotChart(ctx, values, labels){
  var config = {
    type: 'line',
    data: {
        labels,
        datasets: [{
            "label": "event count",
            "data": values,
            "fill": true,
            "backgroundColor": "rgba(75, 192, 192, 0.3)",
            "borderColor": "#4BC0C0",
            "lineTension": 0.1
        }]
    },
    options: {
      responsive: true,
      title: {
        display: true,
        text: 'Event Log for past week'
      },
      tooltips: {
        mode: 'index',
        intersect: false,
      },
      hover: {
        mode: 'nearest',
        intersect: true
      },
      scales: {
        xAxes: [{
          display: true,
          scaleLabel: {
            display: true,
            labelString: 'Date'
          }
        }],
        yAxes: [{
          display: true,
          scaleLabel: {
            display: true,
            labelString: 'Event Count'
          }
        }]
      }
    }
  }

  return new Chart(ctx, config);
}

function getEventsGenerated(){
  var requestOptions = {
    method: 'POST',
    redirect: 'follow'
  };

  return fetch("http://localhost:5001/api/v1/timeseries", requestOptions)
    .then(response => response.text())
    .then(result => {
      return result;
    })
    .catch(error => console.log('error', error));
}
