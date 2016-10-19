import copy
COLOUMN_MAPPING = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
COLOUMN_NAME_MAPPING = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
MINUS_INFINITY = -99999
PLUS_INFINITY = 99999
BOARD_SIZE = 0
PLAYER_TURN = None
SEARCH_DEPTH = 0
ALGORITHM = None
RAID = 'Raid'
STAKE = 'Stake'
cell_value = []
board_status = []
root = None

class Node(object):
    def __init__(self, state, move, unoccupied_squares):
        self.state = copy.deepcopy(state)
        self.children = []
        self.move = move
        self.score = None
        self.unoccupied_squares = unoccupied_squares

    def compute_score(self):
        score_dict = {'X' : 0, 'O' : 0, '.' : 0}
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                score_dict[self.state[i][j]] += cell_value[i][j]
        self.score = score_dict['X'] - score_dict['O'] if PLAYER_TURN == 'X' else score_dict['O'] - score_dict['X']
        return self.score

def init_problem():
    global SEARCH_DEPTH, PLAYER_TURN, ALGORITHM, BOARD_SIZE, cell_value, board_status, root
    with open('input.txt') as f_input:
        file = list(f_input)
    f_input.close()
    BOARD_SIZE = int(file[0].rstrip('\n'))
    ALGORITHM = file[1].rstrip('\n')
    PLAYER_TURN = file[2].rstrip('\n')
    SEARCH_DEPTH = int(file[3].rstrip('\n'))
    for cell_value_line in file[4:4+BOARD_SIZE]:
        cell_value.append([int(value) for value in cell_value_line.rstrip('\n').split(' ')])
    for cell_status_line in file[4+BOARD_SIZE:4+2*BOARD_SIZE]:
        board_status.append(list(cell_status_line.rstrip('\n')))
    unoccupied_squares = 0
    for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board_status[i][j] == '.': unoccupied_squares += 1
    root = Node(board_status, None, unoccupied_squares)

def write_move():
    for child in root.children:
        if root.score == child.score:
            game_move = child.move
            move_split = game_move.split(' ')
            shift_index = int(move_split[0][1:]) + 1
            game_move = move_split[0][0:1] + str(shift_index) + ' ' + move_split[1]
            game_state = child.state
            break
    output = game_move
    for status_line in game_state:
        output = output + '\n' + ''.join(status_line)  
    f_output = open('output.txt', 'w')
    f_output.write(output)
    f_output.close()

def possible_moves(node, maximizingPlayer):
    if maximizingPlayer:
        turn = PLAYER_TURN
    else:
        turn = 'O' if PLAYER_TURN == 'X' else 'X'
    raid_moves = []
    stake_moves = []
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if node.state[i][j] == turn:
                if j-1 >= 0 and node.state[i][j-1] == '.': raid_moves.append(COLOUMN_MAPPING[j-1] + str(i) + ' ' + RAID)            #left raid possibility
                if j+1 < BOARD_SIZE and node.state[i][j+1] == '.': raid_moves.append(COLOUMN_MAPPING[j+1] + str(i) + ' ' + RAID)    #right raid possibility
                if i+1 < BOARD_SIZE and node.state[i+1][j] == '.': raid_moves.append(COLOUMN_MAPPING[j] + str(i+1) + ' ' + RAID)    #bottom raid possibility
                if i-1 >= 0 and node.state[i-1][j] == '.': raid_moves.append(COLOUMN_MAPPING[j] + str(i-1) + ' ' + RAID)            #up raid possibility
            elif node.state[i][j] == '.':
                stake_moves.append(COLOUMN_MAPPING[j] + str(i) + ' ' + STAKE)
            else:
                continue
    return stake_moves + raid_moves

def generate_next_state(node, action, maximizingPlayer):
    """
    generates next state of state in node and returns it
    """
    if maximizingPlayer:
        turn = PLAYER_TURN
    else:
        turn = 'O' if PLAYER_TURN == 'X' else 'X'
    next = Node(node.state, action, node.unoccupied_squares-1)
    node.children.append(next)
    action_split = action.split(' ')
    action_index = action_split[0]
    coloumn = COLOUMN_NAME_MAPPING[action_index[0:1]]
    row = int(action_index[1:])
    action_type = action_split[1]
    if action_type == STAKE:
        next.state[row][coloumn] = turn
    else:                                           #else RAID
        next.state[row][coloumn] = turn
        if coloumn-1 >= 0 and next.state[row][coloumn-1] != '.' and next.state[row][coloumn-1] != turn: next.state[row][coloumn-1] = turn           #left conqured
        if coloumn+1 < BOARD_SIZE and next.state[row][coloumn+1] != '.' and next.state[row][coloumn+1] != turn: next.state[row][coloumn+1] = turn   #right conqured
        if row+1 < BOARD_SIZE and next.state[row+1][coloumn] != '.' and next.state[row+1][coloumn] != turn: next.state[row+1][coloumn] = turn       #bottom conqured
        if row-1 >= 0 and next.state[row-1][coloumn] != '.' and next.state[row-1][coloumn] != turn: next.state[row-1][coloumn] = turn               #up conqured
    return next

def minimax(node, depth, maximizingPlayer):
    if depth == 0 or node.unoccupied_squares == 0:
        return node.compute_score()
    if maximizingPlayer:
        bestValue = MINUS_INFINITY
        moves = possible_moves(node, True)
        for action in moves:
            v = minimax(generate_next_state(node, action, True), depth-1, False)
            bestValue = max(bestValue, v)
            node.score = bestValue
        return bestValue
    else:    # minimizing player
        bestValue = PLUS_INFINITY
        moves = possible_moves(node, False)
        for action in moves:
            v = minimax(generate_next_state(node, action, False), depth-1, True)
            bestValue = min(bestValue, v)
            node.score = bestValue
        return bestValue

def alphabeta_max(node, alpha, beta, depth):
    if depth == 0 or node.unoccupied_squares == 0:
        return node.compute_score()
    bestValue = MINUS_INFINITY
    moves = possible_moves(node, True)
    for action in moves:
        bestValue = max(bestValue, alphabeta_min(generate_next_state(node, action, True), alpha, beta, depth-1))
        node.score = bestValue
        if bestValue >= beta: return bestValue
        alpha = max(alpha, bestValue)
    return bestValue

def alphabeta_min(node, alpha, beta, depth):
    if depth == 0 or node.unoccupied_squares == 0:
        return node.compute_score()
    bestValue = PLUS_INFINITY
    moves = possible_moves(node, False)
    for action in moves:
        bestValue = min(bestValue, alphabeta_max(generate_next_state(node, action, False), alpha, beta, depth-1))
        node.score = bestValue
        if bestValue <= alpha: return bestValue
        beta = min(beta, bestValue)
    return bestValue

init_problem()
if ALGORITHM == 'MINIMAX':
    value = minimax(root, SEARCH_DEPTH, True)
elif ALGORITHM == 'ALPHABETA':
    value = alphabeta_max(root, MINUS_INFINITY, PLUS_INFINITY, SEARCH_DEPTH)
else:
    print 'Invalid Algorithm'
write_move()