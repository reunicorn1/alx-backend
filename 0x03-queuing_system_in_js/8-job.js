import { createQueue } from 'kue';
const queue = createQueue();

export default function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) throw new Error('Jobs is not an array');

    queue
        .on('job enqueue', (id, type) => {
            console.log('Notification job created:', id);
        })
        .on('job complete', (id, result) => {
            console.log(`Notification job ${id} completed`);
        })
        .on('job failed', (id, err) => {
            console.log(`Notification job ${id} failed: ${err}`);
        })
        .on('job progress', (id, progress, data) => {
            console.log(`Notification job ${id} ${progress}% complete`)
        });

    for (let job of jobs) {
        queue.create('push_notification_code_3', job).save()
    }
}