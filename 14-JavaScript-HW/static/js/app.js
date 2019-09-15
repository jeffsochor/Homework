// from data.js
var tableData = data;

// YOUR CODE HERE!

//                    CREATE TABLE                       //
// grab the table body so that we can put in the data
let tableBody = d3.select('tbody');

// loop through the list of records
for (let index = 0; index < tableData.length; index++) {

  // grab a reference to each dictionary
  let dictionary = tableData[index];

  // dictionary is each dictionary
  // dictionary =
  // {
  //   datetime: "1/1/2010",
  //   city: "benton",
  //   state: "ar",
  //   country: "us",
  //   shape: "circle",
  //   durationMinutes: "5 mins.",
  //   comments: "4 bright green circles high in the sky going in circles then one bright green light at my front door."
  // }
  
  // grab reference to each of the values in the dictionary
  let date = dictionary.datetime;
  let city = dictionary.city;
  let state = dictionary.state;
  let country = dictionary.country;
  let shape = dictionary.shape;
  let duration = dictionary.durationMinutes;
  let comments = dictionary.comments;

  // create a row (dynamically) using D3
  var tableRow = tableBody.append("tr"); // create a <tr> element and put it inside the table body

  // create cells in each row that will contain all of the values in the dictionary
  // Date	City	State	Country	Shape	Duration	Comments
  tableRow.append('td').text(date);
  tableRow.append('td').text(city);
  tableRow.append('td').text(state);
  tableRow.append('td').text(country);
  tableRow.append('td').text(shape);
  tableRow.append('td').text(duration);
  tableRow.append('td').text(comments);

}

//ADDED ID DATE TO HTML
// let textBox = d3.select("#datetime");

// function FilterDates() {

//   let txt = d3.select("#datetime").property("value");

// d3.select(".table-head>date").text(txt);
// }

// textBox.on("change", FilterDates);

var button = d3.select("#filter-btn");
button.on("click", function () { 
    d3.event.preventDefault(); //prevents form from trying to refresh page
    var inputElement = d3.select("#datetime");
    var inputValue = inputElement.property("value");
    var filteredData = tableData.filter(row => row.datetime === inputValue);
    console.log(filteredData);
   tableAppend(filteredData); 
});




