import pandas as pd

grading_week = 15

gradebook = pd.read_csv("players_data_book.csv")
week_key = pd.read_csv(f"week{grading_week}/Week{grading_week}_key.csv")
scores = []
incorrect_games = []
correct_games = []


def most_frequent(List):
    return max(set(List), key=List.count)


for i in range(len(gradebook)):
    alias = gradebook['alias'][i]
    try:
        player_picks = pd.read_csv(f"week{grading_week}/Week{grading_week}_{alias}.csv")
        player_alias = alias
    except:
        player_picks = pd.read_csv(f"week{grading_week}/Week{grading_week}_cofav.csv")
        player_alias = f"{alias}_cofav"

    player_score = 0
    print(f"Grading: {player_alias}")

    for game in range(len(player_picks)):
        if player_picks['winner_copy_paste'][game] == week_key['winner_copy_paste'][game]:
            player_score += 1
            if player_picks['winner_copy_paste'][game] == 'LSU':
                print('LSU')
            else:
                pass
            correct_games.append(player_picks['winner_copy_paste'][game])
        else:
            incorrect_games.append(player_picks['winner_copy_paste'][game])

    scores.append(player_score)
    print(f"{alias}: {player_score}")

gradebook[f'Week{grading_week}'] = scores
biggest_loser = most_frequent(incorrect_games)
biggest_winner = most_frequent(correct_games)
bl_count = incorrect_games.count(biggest_loser)
bw_count = correct_games.count(biggest_winner)

print(gradebook)
print(f"Biggest Loser: {biggest_loser} ({bl_count})")
print(f"Biggest Winner: {biggest_winner} ({bw_count})")
# print(correct_games)

# gradebook.to_csv("players_data_book.csv")
