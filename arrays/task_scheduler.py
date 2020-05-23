



def leastInterval(tasks, n):
    char_map = [0] * 26
    for c in tasks:
        char_map[ord(c) - ord('A')] +=1
    char_map.sort()
    max_val = char_map[25] -1
    idle_slots = max_val * n
    for i in range(24, -1, -1):
        idle_slots -= min(char_map[i], max_val)
    if idle_slots > 0:
        return idle_slots + len(tasks)
    else:
        return len(tasks)


tasks = ['A','A','A','B','B','B']

char_map = leastInterval(tasks, 2)

print("The number of intervals for completing all the tasks with an idle interval of {} is {} ".format(leastInterval(tasks, 2), 2))