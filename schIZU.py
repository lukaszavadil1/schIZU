import re, sys # Essentails <3
contents = sys.stdin.read() # Vstupní standardní proud
states_rating = []
for line in contents.split('\n')[12:16]: # mmm tasty unformatted data
    states_rating.append([float(num) for num in re.findall(r'[-+]?\d*\.\d+|[-+]?\d+', line)])
path = [int(num) for num in re.findall(r'stavy\s+(.*)\n', contents)[0].split()]
alpha, gamma = float(re.findall(r'alpha=([\d.]+)', contents)[0]), float(re.findall(r'gamma=([\d.]+)', contents)[0]) # Funny Greek letters
for i in range(len(path) - 1):
    curr_state, next_state = path[i], path[i+1]
    reward = 0 # YOU
    # THE GUY SHE TELLS YOU NOT TO WORRY ABOUT :fuckingcryingrollinggrinninglaughingemojitimesfuckingtendude:
    states_rating[(curr_state-1)//5][(curr_state-1)%5]+=alpha*(reward+gamma*states_rating[(next_state-1)//5][(next_state-1)%5]-states_rating[(curr_state-1)//5][(curr_state-1)%5])
for row in states_rating: # Result
    print(" ".join([f"{states_rating:.3f}" if abs(states_rating) != 1 else f"rew={states_rating:.0f}" for states_rating in row]))
