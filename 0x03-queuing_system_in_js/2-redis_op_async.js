import { createClient } from 'redis';
const redis = require('redis');
const client = createClient();
const util = require('util');
const getAsync = util.promisify(client.get).bind(client);

client.on('connect', () => {
        console.log('Redis client connected to the server');
});
client.on('error', (err) => {
        console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value){
        client.set(schoolName, value, (err, reply) => {
                redis.print(`Reply: ${reply}`);
        });
}

async function displaySchoolValue(schoolName){
	try {
		const reply = await getAsync(schoolName);
		console.log(reply);
	} catch(err) {
		console.log(err);
	}
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

client.quit()

