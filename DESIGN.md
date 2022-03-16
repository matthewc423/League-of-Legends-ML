datacollection.py (.ipynb)

The first function getElo(player) takes in a player summoner id (different from their puuid) and calculates their numeric elo value from their rank. This is done by allocating 400 points for each tier, and 100 points for each division within the tier. Every one that is master tier or above doesn't have divisions anymore and just have a flat elo number above the master elo number, which is 2400. The next bunch of functions take in a match and output a certain detail of the match that we want. For example, the getKills(match) function takes in a match and adds up the kills from each player in the game. This is all set up in the next block of code, where we iterate through all divisions of a given tier, get a list of players in that division of that tier, and append their puuids to a list of player puuids. Because the puuid is not listed when getting the list of players and their information, we must take the summoner id of the player, which is listed, and send a request to the api to return their summoner information, which will include their puuid. The puuid is required since it's the only thing that can be used to get a list of matches from a certain player. In the next few lines, we iterate through each player's puuid in the list of puuids and request a list of 5 match ids from the api of that player in the ranked 5v5 queue type, which is represented by the number 420. We will then send a request to the api to return all the match data to us from the provided match id, and append that match data to the list of allmatches. Now we start the creation of eventual csv file. First we append the headers of the columns into the list matchdata. Then we iterate through all the matches in allmatches and retrieve all data we need by passing all the above-mentioned functions the match data. Since the match data is a multi-layer dictionary, it is easy to access the information. However, I had to use the riot api on riot's website to test it with a match in order to see how the data is formatted and all the key value pairs. After retrieving the specific information, it is appended to the matchdata. After all the matches are run through, the matchdata list is converted into a csv file. The one big issue that was extremely limiting during data collection is that riot api only allows 100 requests per 2 minutes. This means that every time the library riotwatcher was used, a request was sent. This led to an extremely time consuming data collection process, where most of the time was spent calculating the elo of the match itself. This is because once the match data is found, the elo is found by getting the all 10 players' summoner information in order to find out what their ranks were and then averaging all 10 players' ranks. This means that every match, there are already 10 api calls to find the match rank. With 3800 matches, this would be 38000 api calls just to get the rank of the match. If we can have 100 requests every 2 minutes, that would be 760 minutes just to find the match elos themselves. This doesn't even include the calls it took to find the players, find the matches, get the match data, etc. Not to mention the times when my api key expired in the middle of the data collection, or when the wifi randomly crashed so data collection stopped. Because of the time consumption, I could not implement a way to filter out players who had less than 50 games played total, or players who may be inactive. I also couldn't filter out matches that were too short to actually get any substantive data from. For some strange reason, despite my code setting up 40 players per division, so 160 players per tier, so 960 players total with 4800 games total, certain tiers only outputted 500-600 games, so I was only able to end up with 3800. Without the api restriction, the data collection could've been much cleaner and I would've had more time to adjust what was being collected as well as increasing the sample size as a whole. 

training.py (.ipynb) and training2.py (.ipynb)

Both of these were much easier to make in comparison to the data collection, despite it being my first time ever touching machine learning. Everything is quite straightforward, with the creation of a dataframe from loading in the data.csv file, deleting certain columns from the data, etc. The data separation into independent and dependent variables as well as splitting the data into training and testing was very simple. For training.py, I use scikit's linear regression and mlp regressor as some basic models, and after training both models, the MSE for mlp regressor was slightly better for both the training data and testing data. However, the MSE was quite high, so I tried plotting scatterplots of the independent variables and the matchElos in training2.py using seaborn. The scatterplots showed that while some attributes had small trends, the data was just too widespread for each elo for there to be any strong correlations created. I think that not filtering out the matches and players definitely played a part in this, but also having more matches would make the outliers have less of an effect. Then I created a sequential model using keras and added 8 layers to it, eventually converging on one number, which would be the matchElo. After training the model, the resulting mse was slightly lower than the ones generated by scikit's models, but still not very accurate, again most likely due to the data collected. 