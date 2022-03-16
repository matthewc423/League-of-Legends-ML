
from riotwatcher import LolWatcher, ApiError
import pandas as pd

# golbal variables
api_key = 'RGAPI-c664e61b-40ce-4d1b-b804-92455cbe64ef'
watcher = LolWatcher(api_key)
my_region = 'NA1'

me = watcher.summoner.by_name(my_region, 'Doublelift')
print(me)

match1 = watcher.match.by_id(my_region, '4117183079')
print(match1)