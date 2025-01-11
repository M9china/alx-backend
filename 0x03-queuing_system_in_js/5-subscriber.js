import { createClient } from 'redis';
const redis = require('redis');
const client = createClient();

client.on('connect', () => {
        console.log('Redis client connected to the server');
});
client.on('error', (err) => {
        console.log(`Redis client not connected to the server: ${err}`);
});

client.subscribe('holberton school channel');

client.on('message', (chl, msg) => {
	if (msg === 'KILL_SERVER') {
		client.unsubscribe();
		client.quit()
	}
	console.log(msg)
})
