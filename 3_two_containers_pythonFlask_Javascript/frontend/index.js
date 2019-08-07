const axios = require('axios');

console.log('What about Chuck Norris today?');
axios.get('https://api.chucknorris.io/jokes/random') // external call: Chuck Norris API
  .then( r => console.log(r.data.value))
  .then( () => console.log('\n\nNow, let\'s knock knock to the server door...'))
  .then( () => {

    const url = 'http://localhost:5000/greetings/'; // internal call: flask server
    axios.get(url)
      .then( r => console.log('Me: Hey... is there anybody?\nserver: ', r.data))
      .catch( e => console.log(e) );

 })
  .catch( e => console.log(e) );





