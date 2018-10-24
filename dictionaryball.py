def game_dict():	
	home_players = {'Alan Anderson': {'number': 0,
									'shoe': 16,
									'points': 22,
									'rebounds': 12,
									'assists': 12,
									'steals': 3,
									'blocks': 1,
									'slam dunks': 1},

					'Reggie Evans': {'number': 30,
									'shoe': 14,
									'points': 12,
									'rebounds': 12,
									'assists': 12,
									'steals': 12,
									'blocks': 12,
									'slam dunks': 7},

					'Brook Lopez': {'number': 11,
									'shoe': 17,
									'points': 17,
									'rebounds': 19,
									'assists': 10,
									'steals': 3,
									'blocks': 1,
									'slam dunks': 15},

					'Mason Plumlee': {'number': 1,
									'shoe': 19,
									'points': 26,
									'rebounds': 12,
									'assists': 6,
									'steals': 3,
									'blocks': 8,
									'slam dunks': 5},

					'Jason Terry': {'number': 31,
									'shoe': 15,
									'points': 19,
									'rebounds': 19,
									'assists': 2,
									'steals': 4,
									'blocks': 11,
									'slam dunks': 1}
									}

	away_players = {'Jeff Adrien': {'number': 4,
									'shoe': 18,
									'points': 10,
									'rebounds': 1,
									'assists': 1,
									'steals': 2,
									'blocks': 7,
									'slam dunks': 1},

					'Bismak Biyombo': {'number': 0,
									'shoe': 16,
									'points': 12,
									'rebounds': 4,
									'assists': 7,
									'steals': 7,
									'blocks': 15,
									'slam dunks': 10},

					'DeSagna Diop': {'number': 2,
									'shoe': 14,
									'points': 24,
									'rebounds': 12,
									'assists': 12,
									'steals': 4,
									'blocks': 5,
									'slam dunks': 5},

					'Ben Gordon': {'number': 8,
									'shoe': 15,
									'points': 33,
									'rebounds': 3,
									'assists': 2,
									'steals': 1,
									'blocks': 1,
									'slam dunks': 0},

					'Brendan Haywood': {'number': 33,
									'shoe': 15,
									'points': 6,
									'rebounds': 12,
									'assists': 12,
									'steals': 22,
									'blocks': 5,
									'slam dunks': 12}
									}

	game_dictionary = {'home': {'team_name': 'Brooklyn Nets',
								'colors': 'Black, White',
								'players': home_players},
						'away': {'team_name': 'Charlotte Hornets',
								'colors': 'Turquoise, Purple',
								'players': away_players}
						}
	
	return(game_dictionary)

def player_info(player, attribute):
	if player in game_dict()['away']['players'].keys():
		attr = game_dict()['away']['players'][player][attribute]
	else:
		attr = game_dict()['home']['players'][player][attribute]
	return attr

def team_colors(team):
    if team == game_dict()['home']['team_name']:
    	colors = [game_dict()['home']['colors']]
    else:
    	colors = [game_dict()['away']['colors']]
    return colors

def team_names():
	names = []
	for team in game_dict():
		names.append(game_dict()[team]['team_name'])
	return names

def player_numbers(search_team):
	jerz_nums = []
	for team in game_dict().values():
		# print(team)
		if team['team_name'] == search_team:
			for player in team['players']:
				jerz_nums.append(team['players'][player]['number'])
	return jerz_nums

"""
def conjoin_teams():
	conjoined_teams = {game_dict()['home']['players'], game_dict()['away']['players']}
	return conjoined_teams
"""

def player_stats(search_name):
	if search_name in game_dict().values():
		# print (team)
		pass
		


###################################### execute and print

#print(player_info('Brendan Haywood', 'number'))
# print(player_numbers('Charlotte Hornets'))
print(conjoin_teams())
# print(player_stats('Ben Gordon'))

#####################################