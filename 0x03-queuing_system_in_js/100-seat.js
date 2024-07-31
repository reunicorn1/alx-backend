import { createClient } from 'redis';
import { createQueue } from 'kue';
import express from 'express';


// Redis
const client = createClient({
    socket: {
      host: '127.0.0.1',
      port: 6379,
    }
})
  .on('error', (err) => console.log('Redis client not connected to the server: ', err))
  .on('connect', () => console.log('Redis client connected to the server'));
    
client.connect();

async function reserveSeat(number) {
    await client.set("available_seats", number);
}

async function getCurrentAvailableSeats() {
    return await client.get("available_seats");
} // promisify of Redis can't be used 

reserveSeat(50);
let reservationEnabled = true;

// Kue`
const queue = createQueue();


// Server
const app = express();
const PORT = 1245;

app.get('/available_seats', async (req, res) => {
    const seats = await getCurrentAvailableSeats()
    res.json({"numberOfAvailableSeats": seats});
});

app.get('/reserve_seat', (req, res) => {
    if (!reservationEnabled) {
        res.json({ "status": "Reservation are blocked" });
    } else {
        const job = queue.create('reserve_seat', {
            seat: 1
        }).save((err)=> {
            if (err) res.json({ "status": "Reservation failed" });
            else res.json({ "status": "Reservation in process" });
        })
        .on('complete', (result) => console.log(`Seat reservation job ${job.id} completed`))
        .on('failed', (err) => console.log(`Seat reservation job ${job.id} failed: ${err}`));
    }
})

app.get('/process', (req, res) => {
    res.json({ "status": "Queue processing" });
    queue.process('reserve_seat', async (job, done) => {
        const seats = await getCurrentAvailableSeats();
        if (Number(seats) === 0) {
            return done(new Error("Not enough seats available"));
        } else {
            reserveSeat(Number(seats) - 1)
            if (Number(seats) - 1 == 0) {reservationEnabled = false};
        }
        done()
    })
})

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));