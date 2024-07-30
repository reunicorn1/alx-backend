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

async function setNewSchool (schoolName, value) {
    const reply = await client.set(schoolName, value); // usage of redis.print doen't seem to work
    console.log('Reply:', reply);
}


async function displaySchoolValue(schoolName) { // redis replaced the callback feature with async/await
    const value = await client.get(schoolName);
    console.log(value);
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');