goal = 10000
steps = 0

while steps < 10000:
    new_steps = input()
    if new_steps != "Going home":
        steps += int(new_steps)
    else:
        new_steps = int(input())
        steps += new_steps
        break
if steps >= 10000:
    print('Goal reached! Good job!')
    print(f"{steps - goal} steps over the goal!")
else:
    print(f"{goal - steps} more steps to reach goal.")
