const { Client } = require('multiversus.js');
const client = new Client('tttVhEVHWFIMa23VCEJXFZHDPewZ8FdahGVdOJb0vNR99tqQcxKbReTtdFEjPWLYPxhOStM+8V7jNg6sWPRbAEOpzsk9pVW54Wqr8V1gXF6E//U67eElgn9S8coNuhx1gs1hHMuYFTe6uPkGig/coWqEa8BzzdjMWx8SR5fTFFbjHUy8Wz4/lg==');
// (async () => {
// 	const leaderboardData = await client.getLeaderboard('2v2'); // The type of the leaderboard to be retrieved can also //be set to '1v1'.
// 	console.log(leaderboardData);
// })();

	//console.log(JSON.stringify(searchData.leaders[20].account.identity.username));
	
	// const usernameSearch =await client.searchByUsername('yoshifine');
	// const juice= await client.getAccount(usernameSearch.results[0].result.account_id);
	// console.log(juice);
	// console.log(juice.server_data.Characters.character_bugs_bunny);

	// const testo =await client.getLeaderboardForCharacter('1v1','character_shaggy');
	// console.log(testo);
(async () => {
	const searchData = await client.getLeaderboard('1v1',); // A second parameter can also be defined to limit the results returned.
	console.log(searchData)
	console.log(await client.getProfile(searchData.leaders[0].member));
	const uwu=(await client.getAccount(searchData.leaders[14].member));
	const requireeeee=uwu.identity.alternate.wb_network[0].username;

	const htmlData=<div class="name">requireeeee</div>
	
	const testDiv=document.querySelector('.megaTesto')
	testDiv.innerHTML=htmlData

})();

fetch('')