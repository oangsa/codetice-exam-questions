match_count = int(input())
stats = {}

for _ in range(match_count):
    team_a, score_a, team_b, score_b = input().split()
    score_a = int(score_a)
    score_b = int(score_b)

    if team_a not in stats:
        stats[team_a] = {"points": 0, "gf": 0, "ga": 0}
    if team_b not in stats:
        stats[team_b] = {"points": 0, "gf": 0, "ga": 0}

    stats[team_a]["gf"] += score_a
    stats[team_a]["ga"] += score_b
    stats[team_b]["gf"] += score_b
    stats[team_b]["ga"] += score_a

    if score_a > score_b:
        stats[team_a]["points"] += 3
    elif score_a < score_b:
        stats[team_b]["points"] += 3
    else:
        stats[team_a]["points"] += 1
        stats[team_b]["points"] += 1

rows = []
for team, team_stats in stats.items():
    goal_diff = team_stats["gf"] - team_stats["ga"]
    rows.append((-team_stats["points"], -goal_diff, -team_stats["gf"], team, team_stats["points"], goal_diff, team_stats["gf"]))

rows.sort()

print("Standings:")
for _, _, _, team, points, goal_diff, goals_for in rows:
    print(f"{team}: {points} pts, GD {goal_diff}, GF {goals_for}")
