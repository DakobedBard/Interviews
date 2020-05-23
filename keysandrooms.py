def canVisitAllRooms(rooms):
    visited = {0}
    stack = [rooms[0]]
    while stack:
        keys = stack.pop()
        for key in keys:
            if key not in visited:
                stack.append(rooms[key])
                visited.add(key)
    if len(visited) == len(rooms):
        return True
    return False

#
# rooms = [[1],[2],[3],[]]
rooms = [[1,3],[3,0,1],[2],[0]]
print("I can visit all of the rooms {}".format(canVisitAllRooms(rooms)))
