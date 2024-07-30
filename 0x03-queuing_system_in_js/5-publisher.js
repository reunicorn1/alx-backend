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

function publishMessage(message, time) {
    setTimeout(() => {
        console.log("About to send", message);
        client.publish(CHANNEL_NAME, message)
    }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);