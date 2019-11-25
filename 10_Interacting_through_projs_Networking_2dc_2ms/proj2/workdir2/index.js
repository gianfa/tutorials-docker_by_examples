const axios = require('axios');

const TARGET_CONTAINER = 'container11';
const TARGET_PORT = 1100;
const host = 'http://' + TARGET_CONTAINER + ':'  + TARGET_PORT;

const f = async () => {
      await new Promise( (res) => { 
            setTimeout(() => {
                  console.log('Starting calling the service in proj1 at ', host); res()
            }, 2* 1000);
      });
      console.log('\n\nNow, let\'s knock knock on the server door...');
      const url = host + '/';
      const r = await axios.get(url);
      console.log('Me: Hey... is there anybody?\nserver: ', r.data);
      const url2 = host + '/calc/sum/';
      const r2 = await axios.get(url2, {params: {a:11, b:22}});
      console.log('Tell me this: how much is 11 +22 ?', r2.data);
};

f().catch( e => console.log(e.host));




