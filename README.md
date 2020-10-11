# Reversi

> Developed by [Paul Vigneau](https://github.com/paulvigneau) and [Robin Montfermé](https://github.com/RobinMontferme) and ends to the 3rd place at the championship organized by the University of Bordeaux, France for the AI course of the Computer Science Master.

## Run

```
python ./localGame.py
```

## AI description

Search algorithm used :

Nega Alpha-Beta pruning with cutoffs.

## Heuristic description

The heuristic is used to evaluate the board by computing :

- The number of corners owned.
- The mobility of each player (number of possible moves for each player for a specific state of the board).
- The stability score per player. A piece is stable when no other piece can be played that will cause it to be flipped.

Each value of the player is multiplied by 1 and each value of the opponent is multiplied by -1. (View details in the [Evaluator.py](https://github.com/paulvigneau/Reversi/blob/master/Evaluator.py) comments)

Each value is multiplied by 100 and are added together. The sum corresponds to the heuristic result.

If the game is over, the heuristic corresponds to the parity (the number of pieces owned per player).

## Other algorithms to improve performances

- The program uses the multi-processing module in order to compute faster. The number of threads depends on the number of cores the computer has.
- The use of a transition table. This table permits to keep in memory the heuristic result for a specific board configuration. It is very useful when the `depth` value of the search algorithm is high.

- Time limit. For the University championship, the max computing time for each player was 5 minutes. In order to not exceed this limit, the program decreases the depth of the search algorithm.

- Opening book. Like other board games, Reversi has an opening book that indicates the firsts moves of the game without having to compute them.
