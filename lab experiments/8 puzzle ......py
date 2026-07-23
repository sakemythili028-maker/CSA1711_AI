from queue import Queue

goal = [1,2,3,4,5,6,7,8,0]

def solve(start):
    q = Queue()
    q.put(start)
    visited = []

    while not q.empty():
        state = q.get()

        if state == goal:
            print("Goal Reached")
            return

        if state not in visited:
            visited.append(state)
            i = state.index(0)

            for j in [i-3, i+3, i-1, i+1]:
                if 0 <= j < 9:
                    new = state[:]
                    new[i], new[j] = new[j], new[i]
                    q.put(new)

start = [1,2,3,4,0,6,7,5,8]
solve(start)   
