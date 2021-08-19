def checkMove(obs):
    curr, moves = 2, 0
    obs = obs + [0]
    n = len(obs) - 1

    for i in range(n):
        
        if obs[i] == curr:
            if obs[i+1] == 1:
                moves += 1
                curr = 3
            elif obs[i+1] == 3:
                moves += 1
                curr = 1
            elif obs[i+1] == 2:
                moves += 1
                if curr == 1:
                    curr = 3
                elif curr == 3:
                    curr = 1
            elif obs[i+1] == 0:
                moves+=1
                break

    return moves

obs = [2, 1, 3, 2, 3, 2, 3, 2, 2, 3]
moves = checkMove(obs)
print(f' **************** ')
print(f' Minimum Race Moves : {moves}')
print(f' **************** ')



