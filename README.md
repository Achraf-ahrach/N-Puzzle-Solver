# N-Puzzle

## Bonus option: random generation iterations

The puzzle generator supports a custom shuffle depth:

```bash
python npuzzle-gen.py 3 -s -i 10000
```

Available option:

```text
-i, --iterations ITERATIONS
						Iterations for random generation (default: 10000)
```

You can also use it through `make`:

```bash
make gen SIZE=4 ITERATIONS=5000
make gen_unsolvable SIZE=4 ITERATIONS=5000
```