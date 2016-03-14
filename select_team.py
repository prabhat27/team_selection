res_team1 = None
res_team2 = None

def get_strength(team):
    s = 0
    for player in team:
        s = s + player[2]
    return s

def get_possible_teams(cur_idx, player_role_strength, 
    bats_left_team1, bowl_left_team1, wk_left_team1, player_left_team1,
    bats_left_team2, bowl_left_team2, wk_left_team2, player_left_team2,
    team1, team2
    ):
    # print "hi"
    
    if(cur_idx >= len(player_role_strength)):
        return

    if(player_left_team1 == 0 and player_left_team2 == 0):
        # possible_team_combo.append((team1, team2))
        global res_team1, res_team2
        if(res_team1 == None and res_team2 == None):
            res_team1 = team1
            res_team2 = team2
            # return
        s1 = get_strength(team1)
        s2 = get_strength(team2)
        rs1 = get_strength(res_team1)
        rs2 = get_strength(res_team2)
        if(abs(s2-s1) < abs(rs2-rs1)):
            res_team1 = team1
            res_team2 = team2
        if((abs(s2-s1) == abs(rs2-rs1)) and ((s1+s2) > (rs2+rs1))):
            res_team1 = team1
            res_team2 = team2
        return

    cur_player = player_role_strength[cur_idx][0]
    cur_player_role = player_role_strength[cur_idx][1]
    cur_player_strength = player_role_strength[cur_idx][2]
    
    # Select this player in one team 
    if(cur_player_role == 'bats'):
        # Select this player in team1
        if(bats_left_team1 > 0 and player_left_team1 > 0):
            temp_team1 = team1 + [player_role_strength[cur_idx]]
            get_possible_teams(cur_idx + 1, player_role_strength,
                bats_left_team1 - 1, bowl_left_team1, wk_left_team1, player_left_team1 - 1,
                bats_left_team2, bowl_left_team2, wk_left_team2, player_left_team2,
                temp_team1, team2
            )
        # Select this player in team2
        if(bats_left_team2 > 0 and player_left_team2 > 0):
            temp_team2 = team2 + [player_role_strength[cur_idx]]
            get_possible_teams(cur_idx + 1, player_role_strength,
                bats_left_team1, bowl_left_team1, wk_left_team1, player_left_team1,
                bats_left_team2 - 1, bowl_left_team2, wk_left_team2, player_left_team2 - 1,
                team1, temp_team2
            )
    
    elif(cur_player_role == 'bowl'):
        # Select this player in team1
        if(bowl_left_team1 > 0 and player_left_team1 > 0):
            temp_team1 = team1 + [player_role_strength[cur_idx]]
            get_possible_teams(cur_idx + 1, player_role_strength,
                bats_left_team1, bowl_left_team1 - 1, wk_left_team1, player_left_team1 - 1,
                bats_left_team2, bowl_left_team2, wk_left_team2, player_left_team2,
                temp_team1, team2
            )
        # Select this player in team2
        if(bowl_left_team2 > 0 and player_left_team2 > 0):
            temp_team2 = team2 + [player_role_strength[cur_idx]]
            get_possible_teams(cur_idx + 1, player_role_strength,
                bats_left_team1, bowl_left_team1, wk_left_team1, player_left_team1,
                bats_left_team2, bowl_left_team2 - 1, wk_left_team2, player_left_team2 - 1,
                team1, temp_team2
            )

    else:
        # Select this player in team1
        if(wk_left_team1 > 0 and player_left_team1 > 0):
            temp_team1 = team1 + [player_role_strength[cur_idx]]
            get_possible_teams(cur_idx + 1, player_role_strength,
                bats_left_team1, bowl_left_team1, wk_left_team1 - 1, player_left_team1 - 1,
                bats_left_team2, bowl_left_team2, wk_left_team2, player_left_team2,
                temp_team1, team2
            )
        
        # Select this player in team2
        if(wk_left_team2 > 0 and player_left_team2 > 0):
            temp_team2 = team2 + [player_role_strength[cur_idx]]
            get_possible_teams(cur_idx + 1, player_role_strength,
                bats_left_team1, bowl_left_team1, wk_left_team1, player_left_team1,
                bats_left_team2, bowl_left_team2, wk_left_team2 - 1, player_left_team2 - 1,
                team1, temp_team2
            )
    

    # Do no select this player in any team
    
    get_possible_teams(cur_idx + 1, player_role_strength,
        bats_left_team1, bowl_left_team1, wk_left_team1, player_left_team1,
        bats_left_team2, bowl_left_team2, wk_left_team2, player_left_team2,
        team1, team2
    )

    return

def zip_role_strength(players, strength, batsmen, bowlers, wk):
    res = []
    for (i, player) in enumerate(players):
        if(player in batsmen):
            res.append((player, 'bats', strength[i]))
        elif(player in bowlers):
            res.append((player, 'bowl', strength[i]))
        else:
            res.append((player, 'wk', strength[i]))
    return res

def formatted_result():

    S1 = 0
    T1 = []
    S2 = 0
    T2 = []

    for res_player in res_team1:
        T1.append(res_player[0])
        S1 += res_player[2]

    for res_player in res_team2:
        T2.append(res_player[0])
        S2 += res_player[2]
    
    print 'Team One and its strength: ', (T1, S1)
    print 'Team Two and its strength: ', (T2, S2)
    print 'Difference in strength: ', (abs(S1-S2))

if __name__ == '__main__':
    
    # Input constraints
    N = 10
    players = [1,2,3,4,5,6,7,8,9,10,11]
    
    M = 4
    batsmen = [1,2,3,4]

    O = 2
    bowlers = [5,6]

    P = 5
    wk = [7,8,9,10,11]

    x = 1 # Maximum number of batsmen
    y = 1 # Maximum number of bowlers
    z = 2 # Maximum number of wicket keepers

    k = 4 # Number of player each team must have.

    strength = [5,1,3,1,1,3,2,2,3,4,2]
    
    # Zip the player with role and strength

    player_role_strength = zip_role_strength(players, strength, batsmen, bowlers, wk) 

    # print (player_role_strength)

    get_possible_teams(0, player_role_strength,
        x, y, z, k,
        x, y, z, k,
        [], []
        )
    # print (res_team1, res_team2)

    if(res_team1 and res_team2):
        formatted_result()
    else:
        print "Sorry, no solution for the given configuration !"