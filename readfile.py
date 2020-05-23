
f = open("testcase.txt", "r")
queries = []
while f.readline():
    query = f.readline()
    splits = query.split(' ')
    queries.append((splits[0],splits[1][:-1]))
