import { createClient } from 'redis';

const CHANNEL_NAME = 'holberton school channel'

const client = createClient({
    socket: {
      host: '127.0.0.1',
      port: 6379,
    }
})
  .on('error', (err) => console.log('Redis client not connected to the server: ', err))
  .on('connect', () => console.log('Redis client connected to the server'));
    
client.connect()

client.subscribe(CHANNEL_NAME, (message) => {
    console.log(message);
    if (message === "KILL_SERVER") {
        client.unsubscribe(CHANNEL_NAME);
        client.quit();
    }
});