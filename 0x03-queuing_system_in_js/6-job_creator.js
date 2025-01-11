const kue = require('kue');
const queue = kue.createQueue();

let data = {
  phoneNumber: '0909090909',
  message: 'DoHardThings',
}

const job = queue.create('push_notification_code', data)
	.save((err) => {
	if (!err){
		console.log(`Notification job created: ${job.id}`)
	}
});
job.on('complete', ()=>{
	console.log('Notification job completed')
})
job.on('failing', () => {
	console.log('Notification job failed')
})
