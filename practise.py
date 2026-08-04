# You are given a list representing goals scored by a player in consecutive matches:
# goals = [2, 1, 0, 3, 1, 2]
# Write a function: analyze_player(goals):

# That returns a dictionary with:

# "total_goals" → sum of all goals

# "longest_streak" → longest consecutive matches where goals > 0

# "factorial_bonus" → factorial of total goals (use recursion)
# Use a loop to calculate total goals and streak

# Use a recursive function to calculate factorial

# If total goals > 10 → return "Too many goals!" instead of factorial

goals = [2, 1, 0, 3, 1, 2, 4, 7, 3, 2]

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def analyze_player(goals):
    # Calculate total goals
    total = 0
    for goal in goals:
        total += goal

    # Calculate longest scoring streak
    streak = 0
    longest = 0

    for goal in goals:
        if goal > 0:
            streak += 1
            if streak > longest:
                longest = streak
        else:
            streak = 0

    # Calculate factorial bonus
    if total > 10:
        bonus = "Too many goals!"
    else:
        bonus = factorial(total)

    return {
        "total_goals": total,
        "longest_streak": longest,
        "factorial_bonus": bonus
    }

print(analyze_player(goals))
