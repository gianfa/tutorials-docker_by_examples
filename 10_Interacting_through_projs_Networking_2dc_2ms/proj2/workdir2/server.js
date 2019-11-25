var express = require('express');


var app = express();
var PORT = 2200;

app.get('/', function (req, res) {
  res.send('Hello World by JS! From proj2 serv2');
});


app.listen(PORT, function () {
  console.log('Example app listening on port '+ PORT +'!');
});
