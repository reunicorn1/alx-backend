import { createQueue } from 'kue';

const queue = createQueue();
const jobData = {
    phoneNumber: "123-456-7890",
    message: "Hello Unicorn!",
  }

const push_notification_code = queue.create('message', jobData).save()
    .on('enqueue', () => console.log('Notification job created:', push_notification_code.id))
    .on('complete', () => console.log('Notification job completed'))
    .on('failed', () => console.log('Notification job failed'))