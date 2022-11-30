
from user_data import User_Data
from player_data import Player_Data
from tournaments_data import Tournaments_Data
from associations_data import Associations_Data

data_class = User_Data()
result = data_class.read_all_users()

data_class = Player_Data()
result = data_class.read_all_players()

data_class = Tournaments_Data()
result = data_class.read_all_tournaments()

data_class = Associations_Data()
result = data_class.read_all_associations()


for elem in result:
    print(elem)