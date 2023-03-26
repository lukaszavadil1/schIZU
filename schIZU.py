import re, sys # Essentials <3
contents = sys.stdin.read() # mmm unformatted chunk of data
sys.stdout.write(contents + 3 * '\n')
states_rating = []
# Limst compremhemsioms
[states_rating.append([float(num) for num in re.findall(r'[-+]?\d*\.\d+|[-+]?\d+', line)]) for line in contents.split('\n')[12:16]]
path = [int(num) for num in re.findall(r'stavy\s+(.*)\n', contents)[0].split()] # Funny Greek letters
alpha, gamma = float(re.findall(r'alpha=([\d.]+)', contents)[0]), float(re.findall(r'gamma=([\d.]+)', contents)[0])
for i in range(len(path) - 1):
    curr_state, next_state = path[i], path[i+1]
    # Get reward of the next state
    reward = 0 if abs(int(states_rating[(next_state - 1) // len(states_rating[0])][(next_state - 1) % len(states_rating[0])])) != 1 else int(states_rating[(next_state - 1) // len(states_rating[0])][(next_state - 1) % len(states_rating[0])])
    # The final boss of debug
    states_rating[(curr_state - 1) // len(states_rating[0])][(curr_state - 1) % len(states_rating[0])] += alpha * (reward + gamma * (states_rating[(next_state - 1) // len(states_rating[0])][(next_state - 1) % len(states_rating[0])] if abs(int(states_rating[(next_state -1) // len(states_rating[0])][(next_state - 1) % len(states_rating[0])])) != 1 else 0.0) - states_rating[(curr_state - 1) // len(states_rating[0])][(curr_state - 1) % len(states_rating[0])])
[print(" ".join([f"{rating:.3f}" if abs(rating) != 1 else f"rew={int(rating)}" for rating in row])) for row in states_rating]
