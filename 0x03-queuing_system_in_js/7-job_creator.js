import { createQueue } from 'kue';

const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
  ];


  const queue = createQueue()
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
    })

  for (let job of jobs) {
    queue.create('push_notification_code_2', job).save()
  }