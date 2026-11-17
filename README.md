# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/hbltz09543-code/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/hbltz09543-code/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in under 4 KB of Python for make.fun's tiny-chess-01 bounty. `main.py` (4,095 bytes) plays the gauntlet through the env at `MAKEFUN_ENV_URL`: negamax alpha-beta with iterative deepening on a fixed node budget (no clock, no randomness, so every game is deterministic), quiescence over captures and promotions, a transposition table, TT/MVV-LVA/killer move ordering, and an evaluation of material, piece-square tables and the bishop pair. A global node counter steps the per-move budget down as the trial's total thinking time grows, and the search scores a draw once the fifty-move counter passes 99 plies. Python 3.13 standard library only. MIT licensed (see LICENSE).

## Run it

```sh
# Start a make.fun env server (see the competition kit), then:
MAKEFUN_ENV_URL=http://localhost:8123 python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
