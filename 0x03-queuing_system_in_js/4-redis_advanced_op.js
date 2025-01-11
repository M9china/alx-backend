import { createClient } from 'redis';
const redis = require('redis');
const client = createClient();

client.on('connect', () => {
        console.log('Redis client connected to the server');
});
client.on('error', (err) => {
        console.log(`Redis client not connected to the server: ${err}`);
});

function setHash(key, field, value){
	client.hset(key, field, value, (err, reply) => {
		redis.print(`Reply: ${reply}`);
	});
}

function getAll(key) {
	client.hgetall(key, (err, reply) => {
		if(err){
			console.log(err)
		}else{
			console.log(reply)
		}
	});
}

const key = 'HolbertonSchools';
setHash(key, 'Portland', 50);
setHash(key, 'Seattle', 80 );
setHash(key, 'New York', 20);
setHash(key, 'Bogota', 20);
setHash(key, 'Cali', 40);
setHash(key, 'Paris', 2);

getAll(key);
