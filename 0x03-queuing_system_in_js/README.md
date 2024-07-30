# 0x03. Queuing System in JS

Redis is often used in conjunction with JavaScript for job scheduling and queue management. It's a powerful in-memory data structure store that can be used as a database, cache, and message broker.
n the context of job scheduling, you might use Redis to store jobs that need to be processed at a later time. Each job would be added to a queue, and a separate worker process would periodically check the queue and process jobs as they come in.
There are several libraries available that can help with this, such as Bull or Kue. These libraries provide a higher-level API for managing job queues with Redis, including features like priority, job events, concurrency control, and more.

## Kue
Kue is a priority job queue for Node.js backed by Redis. It allows you to schedule and process jobs, with features like priority, job events, concurrency, and delayed jobs.
Here's a basic example of how you might use Kue to create and process a job:
```jsx
var kue = require('kue');
var queue = kue.createQueue();

// Create a job
var job = queue.create('myJob', {title: 'myTitle'}).save();

// Process jobs
queue.process('myJob', function(job, done){
  console.log('Processing job with title:', job.data.title);
  done();
});
```

## Tasks/files

|    Tasks       |     Files                     |
|----------------|-------------------------------|
|0. Install a redis instance|``README.md``, ``dump.rdb``|
|1. Node Redis Client|``0-redis_client.js``|
|2. Node Redis client and basic operations|`1-redis_op.js`|
|3. Node Redis client and async operations|`2-redis_op_async.js`|
|4. Node Redis client and advanced operations|``4-redis_advanced_op.js``|
|5. Node Redis client publisher and subscriber|``5-subscriber.js``, ``5-publisher.js``|
|6. Create the Job creator|``6-job_creator.js``|
|7. Create the Job processor|``6-job_processor.js``|
|8. Track progress and errors with Kue: Create the Job creator|``7-job_creator.js``|
|9. Track progress and errors with Kue: Create the Job processor|``7-job_processor.js``|
|10. Writing the job creation function| ``8-job.js``|
|11. Writing the test for job creation|``8-job.test.js``|
|12. In stock?| ``9-stock.js``|




