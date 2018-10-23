import pdb

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

def team_colors():
    pass

def team_names():
    pass

def player_numbers():
    pass

def player_stats():
    pass

def good_practices():
  for location, team_stats in game_dict().items():
    # are you ABSOLUTELY SURE what 'location' and 'team_stats' are? use pdb.set_trace() to find out!
    import pdb; pdb.set_trace()
    for stats, data in team_stats.items():
        # are you ABSOLUTELY SURE what 'stats' and 'data' are? use pdb.set_trace() to find out!
        import pdb; pdb.set_trace()
        # what is 'data' at each level of the for loop block? when will we be able to iterate through a list? 
        # When would the following line of code break?
        for item in data:
            print(item)

######################################

print(player_info('Brendan Haywood', 'number'))

#(good_practices())