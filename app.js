const { Client } = require('multiversus.js');
const client = new Client('tttVhEVHWFIMa23VCEJXFZHDPewZ8FdahGVdOJb0vNR99tqQcxKbReTtdFEjPWLYPxhOStM+8V4dhU0th0EXlEOpzsk9pVW54Wqr8V1gXF6E//U67eElgn9S8coNuhx1gs1hHMuYFTe6uPkGig/coWqEa8BzzdjMWx8SR5fTFFbjHUy8Wz4/lg==');
// (async () => {
// 	const leaderboardData = await client.getLeaderboard('2v2'); // The type of the leaderboard to be retrieved can also //be set to '1v1'.
// 	console.log(leaderboardData);
// })();
(async () => {
	const searchData = await client.getLeaderboard('1v1',); // A second parameter can also be defined to limit the results returned.
	//console.log(searchData);
	//console.log(JSON.stringify(searchData.leaders[20].account.identity.username));
	
	const usernameSearch =await client.searchByUsername('yoshiFine');
	console.log(usernameSearch);
})();