import createPushNotificationsJobs from "./8-job";
import { createQueue } from "kue";

const chai = require('chai');
const expect = chai.expect;

const queue = createQueue();

describe('Testing Job Creation', () => {
    before(function() {
        queue.testMode.enter();
      });

    afterEach(function() {
        queue.testMode.clear();
    });
      
    after(function() {
        queue.testMode.exit()
    });
      
    const jobs = [
        {
            name: 'Reem',
            message: 'Hello there, wassup!!!!'
        },
        {
            name: 'Lina',
            message: 'Haya Bonjour!'
        }
    ]
    it('Creation of two new jobs', () => {
        createPushNotificationsJobs(jobs, queue);
        expect(queue.testMode.jobs.length).to.equal(2);
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
    })
    it('Displays an Error message if jobs is not an array', () => {
        expect(function() {
            createPushNotificationsJobs("jobs", queue);
        }).to.throw(Error, 'Jobs is not an array');
    })
})