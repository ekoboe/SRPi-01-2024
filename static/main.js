function fetchData_1() {
fetch('/sensorData')
    .then(response => response.json())
    .then(data => {
          document.getElementById('temperature').innerText = data.temperature.toFixed(2) + "   °C";
          document.getElementById('humidity').innerText = data.humidity.toFixed(2) + " %";
                  })

fetch('/updateClient')
    .then(response => response.json())
    .then(data => {
          document.getElementById('current').innerText = data.reading_data_1.toFixed(2) + "    A";
          document.getElementById('voltage').innerText = data.reading_data_2.toFixed(2) + "    V";
          document.getElementById('ActivePower').innerText = data.reading_data_3.toFixed(2) + "    W";
          document.getElementById('ActiveEnergy').innerText = data.reading_data_4.toFixed(2) + "   Wh";
                  })
}
setInterval(fetchData_1, 1000);

function fetchData_2() {

fetch('/updateClient')
    .then(response => response.json())
    .then(data => {
          document.getElementById('current').innerText = data.reading_data_1.toFixed(2) + "    A";
          document.getElementById('voltage').innerText = data.reading_data_2.toFixed(2) + "    V";
          document.getElementById('ActivePower').innerText = data.reading_data_3.toFixed(2) + "    W";
          document.getElementById('ActiveEnergy').innerText = data.reading_data_4.toFixed(2) + "   Wh";
                  })
}
setInterval(fetchData_2, 100);

