function createPushNotificationsJobs(jobs, queue){
	if (Array.isArray(jobs)){
		for (let i = 0; i < jobs.length; i++) {
        		const job = queue.create('push_notification_code_2', jobs[i])
        	.save((err) => {
                	if (!err) {
                        	console.log(`Notification job created ${job.id}`);
                	}
        	})
        	job.on('complete', () => {console.log(`Notification job ${job.id} completed`);});
        	job.on('failure', (err) => {console.log(`Notification job ${job.id} failed: ${err}`)})
        	job.on('progress', (progress) => {console.log(`Notification job ${job.id} ${progress}% complete`)})
		}
	}else{
		throw new Error('Jobs is not an array');
	}
}

module.exports = createPushNotificationsJobs;
