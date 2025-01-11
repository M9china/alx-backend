import { createQueue } from 'kue';
import chai from 'chai';
import sinon from 'sinon';
import createPushNotificationsJobs from './8-job';

const expect = chai.expect;

const queue = createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
];

describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    sinon.spy(console, 'log');
  });

  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    sinon.restore();
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit()
  });

  it('display a error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs(1, queue)).to.throw();
    expect(() => createPushNotificationsJobs(1, queue)).to.throw(/Jobs is not an array/);
  });

  it('throws if queue is not a valid kue', function() {
    expect(() => createPushNotificationsJobs(jobs, "")).to.throw();
  });

  it('test the creation of jobs', () => {
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(1);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
    expect(console.log.calledOnceWith(`Notification job created: ${queue.testMode.jobs[0].id}`)).to.be.true;
  });

  it('test job progress event report', (done) => {

