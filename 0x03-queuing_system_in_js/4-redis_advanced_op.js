import { createClient } from 'redis';

const client = createClient({
    socket: {
      host: '127.0.0.1',
      port: 6379,
    }
})
  .on('error', (err) => console.log('Redis client not connected to the server: ', err))
  .on('connect', () => console.log('Redis client connected to the server'));
    
client.connect();

async function hashSet (field, key, value) {
    const hsetResult = await client.hSet(field , key, value)
    console.log('Reply:', hsetResult);
}

async function getSet (field) {
    const hGetAllResult = await client.hGetAll(field);
    console.log(hGetAllResult);
}

const field = 'HolbertonSchools'
const dictionary = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2
}
for (const [key, value] of Object.entries(dictionary)) {
    hashSet(field, key, value);
  }

getSet(field);