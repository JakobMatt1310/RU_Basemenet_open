from csv import DictWriter

fixture_list = []
fixture_list = ["Leaders", 45, "Crockets", 3]
    

def write_results(fixture_list):
    field_names = ['home_team', 'home_score', 'away_team', 'away_score']
            
            
    dict = {'home_team': fixture_list[0], 'home_score': fixture_list[1], 'away_team': fixture_list[2], 'away_score': fixture_list[3]}
            
            
    with open('points.csv', 'a') as f_object:
            
               
        dictwriter_object = DictWriter(f_object, fieldnames=field_names)
            
        dictwriter_object.writerow(dict)
        
        f_object.close()


write_results(fixture_list)