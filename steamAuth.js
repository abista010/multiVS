const SteamUser = require('steam-user');

const username = 'abista10';
const password = 'a5a8T$&ii!F#7G#J';
const appid = 1818750;

const steamUser = new SteamUser();
try {
	steamUser.logOn({ accountName: username, password });
} catch (err) {
	throw new Error('Invalid Steam username or password provided!');
}
steamUser.on('loggedOn', async (details) => {
	const ticket = await steamUser.getEncryptedAppTicket(appid, null);

	console.log(ticket.encryptedAppTicket.toString('hex'));

	process.exit(1);
});