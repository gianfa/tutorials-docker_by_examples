const axios = require('axios');

console.log('What about Chuck Norris today?');


const f = async () => {
      await new Promise( (res) => { 
            setTimeout(() => {console.log('over'); res()}, 4* 1000);
      });
      // const cn = await axios.get('https://api.chucknorris.io/jokes/random');
      // console.log(cn.data.value);
      console.log('\n\nNow, let\'s knock knock on the server door...');
      const url = 'http://appflask:5000/greetings/';
      const r = await axios.get(url);
      console.log('Me: Hey... is there anybody?\nserver: ', r.data);
      const url2 = 'http://appflask:5000/calc/sum/';
      const r2 = await axios.get(url2, {params: {a:11, b:22}});
      console.log('Tell me this: how much is 11 +22 ? ', r2.data);
};

f().catch( e => console.log(e) );




