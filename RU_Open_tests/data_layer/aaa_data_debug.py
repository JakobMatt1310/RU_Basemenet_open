
from user_data import User_Data
from player_data import Player_Data
from tournaments_data import Tournaments_Data
from associations_data import Associations_Data
from teams_data import Teams_Data

data_class_user = User_Data()
result = data_class_user.read_all_users()

for elem in result:
    print(elem)
    
data_class_player = Player_Data()
result = data_class_player.read_all_players()

for elem in result:
    print(elem)
    
data_class_tournament = Tournaments_Data()
result = data_class_tournament.read_all_tournaments()

for elem in result:
    print(elem)
    
data_class_association = Associations_Data()
result = data_class_association.read_all_associations()

for elem in result:
    print(elem)
          
data_class_teams = Teams_Data()
result = data_class_association.read_all_associations()

for elem in result:
    print(elem)