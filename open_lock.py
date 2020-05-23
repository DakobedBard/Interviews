def openLock(deadends, target):
    deadends = set(deadends)
    visited = set("0000")
    queue = ["0000"]
    level = 0
    while queue:

        size = len(queue)
        while size > 0:
            lockposition = queue.pop(0)
            if lockposition in deadends:
                size -= 1
                continue
            if lockposition == target:
                return level
            sb = lockposition
            for i in range(4):
                current_position = sb[i]
                incremenetdigit = "0" if current_position == "9" else str(int(current_position)+1)
                decrementdigit = "9" if current_position == "0" else str(int(current_position)-1)
                increment_string = sb[:i] + incremenetdigit + sb[i+1:]
                decrement_string = sb[:i] + decrementdigit + sb[i+1:]

                if increment_string not in visited and increment_string not in deadends:
                    queue.append(increment_string)
                    visited.add(increment_string)
                if decrement_string not in visited and decrement_string not in deadends:
                    queue.append(decrement_string)
                    visited.add(decrement_string)
            size -= 1
        level +=1
    return -1

deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"

#deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
#arget = "8888"

print("The minimum number of moves to open this loock is {} ".format(openLock(deadends, target)))