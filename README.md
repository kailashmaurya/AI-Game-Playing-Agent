# AI-Game-Playing-Agent
Implements Adversarial search strategies like Alpha-Beta and Minimax Algo for Game Playing Agent next move determination

# Adversarial Search Strategies: MiniMax Algorithm and Alpha-Beta Pruning.

MiniMax Algorithm : It is a recursive algorithm for choosing the next move in an n-player game, here implemented as a two-player game. A value is associated with each position or state of the game. This value is computed by means of a board evaluation function and it indicates how good it would be for a player to reach that board position. The player then makes the move that maximizes the minimum value of the position resulting from the opponent's possible following moves.

Alpha-Beta Pruning : It is a search algorithm that seeks to decrease the number of nodes that are evaluated by the minimax algorithm in its search tree. It is commonly used for machine playing of two-player games (for example Tic-tac-toe, Chess etc). It stops completely evaluating a move when at least one possibility has been found that proves the move to be worse than a previously examined move.

# How to execute:
Make sure GamePlayingAgent.py and input.txt are in the same directory before running the script file. When you run the GamePlayingAgent.py file, it reads input.txt and applies adversarial algorithms on the input to look for the best possible move to make. The script generates output.txt which holds the move decided by the algorithm and the next board state.

# Input Format:
$lt;N&gt;
<br>$lt;MODE&gt;
<br>$lt;YOUPLAY&gt;s
<br>$lt;DEPTH&gt;
<br>$lt;… CELL VALUES …&gt;
<br>$lt;… BOARD STATE …&gt;
<br>where
<br>$lt;N&gt; is the board width and height, e.g., N=5 for a 5x5 board. N is an positive integer.
<br>$lt;MODE&gt; is “MINIMAX” or “ALPHABETA”.
<br>$lt;YOUPLAY&gt; is either “X” or “O” and is the player which will play on this turn.
<br>$lt;DEPTH&gt; is the max depth of the search. By convention, the root of the search tree is considered to be at depth 0.
<br>$lt;… CELL VALUES …&gt; contains N lines with, in each line, N positive integer numbers each separated by a single space. These numbers represent the value of each location.
<br>$lt;… BOARD STATE …&gt; contains N lines, each with N characters “X” or ”O” or “.” to represent the state of each cell as occupied by X, occupied by O, or free.

# Output Format:
&lt;MOVE&gt; &lt;MOVETYPE&gt;<br>
&lt;NEXT BOARD STATE&gt;<br><br>
where,<br>
&lt;MOVE&gt; is the move decided.<br>
&lt;MOVETYPE&gt; is “Stake” or “Raid” and is the type of move that the &lt;MOVE&gt; is.<br>
&lt;NEXT BOARD STATE&gt; a description of the new board state after the move decided has been made. Same format as &lt;BOARD STATE&gt; in input file.

# Runner:
You can test the script on multiple inputs using the Runner.py utility, Make sure you keep the 'cases' directory at the same level as Runner.py and GamePlayingAgent.py
