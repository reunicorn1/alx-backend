import { createClient } from "redis";

async function main() {
  const client = createClient({
    socket: {
      host: '127.0.0.1',
      port: 6379,
    }
  })
    .on('error', (err) => console.log('Redis client not connected to the server: ', err))
    .on('connect', () => console.log('Redis client connected to the server'));
    
  await client.connect();
}

main();
