const { Client } = require('multiversus.js');
const client = new Client('tttVhEVHWFIMa23VCEJXFZHDPewZ8FdahGVdOJb0vNR99tqQcxKbReTtdFEjPWLYPxhOStM+8V7aNunN/guRtEOpzsk9pVW54Wqr8V1gXF6E//U67eElgn9S8coNuhx1gs1hHMuYFTe6uPkGig/coWqEa8BzzdjMWx8SR5fTFFbjHUy8Wz4/lg==');
// (async () => {
// 	const leaderboardData = await client.getLeaderboard('2v2'); // The type of the leaderboard to be retrieved can also //be set to '1v1'.
// 	console.log(leaderboardData);
// })();
(async () => {
	// const searchData = await client.getLeaderboard('1v1',); // A second parameter can also be defined to limit the results returned.
	// console.log(searchData);
	//console.log(JSON.stringify(searchData.leaders[20].account.identity.username));
	
	//const usernameSearch =await client.searchByUsername('swenko');
	//const juice= await client.getAccount(usernameSearch.results[0].result.account_id);
	//console.log(juice);
	//console.log(juice.server_data.Characters.character_bugs_bunny);

	const testo =await client.getLeaderboardForCharacter('1v1','character_shaggy');
	console.log(testo);

})();