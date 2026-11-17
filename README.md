# tiny-chess

A chess engine in under 4 KB of Python for make.fun's tiny-chess-01.

`main.py` plays the gauntlet through the env at `MAKEFUN_ENV_URL`:
negamax alpha-beta with iterative deepening on a fixed node budget
(no clock, no randomness), quiescence over captures and promotions,
a transposition table, TT/MVV-LVA/killer move ordering, and an
evaluation of material, piece-square tables and the bishop pair.

Python 3.13 standard library only. MIT licensed (see LICENSE).
