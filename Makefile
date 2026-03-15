PYTHON ?= python3
PUZZLE ?= puzzle.txt
SIZE ?= 3
ITERATIONS ?= 10000
HEURISTIC ?= linear
ALGORITHM ?= auto
GEN_FLAGS ?= -s

.PHONY: help solve solve-path random generate clean

help:
	@echo "Available targets:"
	@echo "  make solve                        Solve PUZZLE=$(PUZZLE)"
	@echo "  make solve-path                   Solve and print the full solution path"
	@echo "  make random                       Generate and solve a random puzzle"
	@echo "  make generate                     Generate a puzzle with npuzzle-gen.py"
	@echo "  make clean                        Remove Python cache files"
	@echo ""
	@echo "Variables:"
	@echo "  PYTHON=$(PYTHON)"
	@echo "                        Python executable used to run scripts"
	@echo "  PUZZLE=$(PUZZLE)"
	@echo "                        Path to puzzle file for solve/solve-path"
	@echo "  SIZE=$(SIZE)"
	@echo "                        Puzzle size for random/generate"
	@echo "  ITERATIONS=$(ITERATIONS)"
	@echo "                        Number of shuffle passes (default: 10000)"
	@echo "  HEURISTIC=$(HEURISTIC)"
	@echo "                        Heuristic: linear, manhattan, hamming"
	@echo "  ALGORITHM=$(ALGORITHM)"
	@echo "                        Algorithm: auto, astar, idastar"
	@echo "  GEN_FLAGS=$(GEN_FLAGS)"
	@echo "                        Generator flags: -s (solvable) or -u (unsolvable)"
	@echo ""
	@echo "Examples:"
	@echo "  make solve HEURISTIC=manhattan"
	@echo "  make solve ALGORITHM=idastar"
	@echo "  make random SIZE=4 ITERATIONS=500 HEURISTIC=hamming"

solve:
	$(PYTHON) main.py $(PUZZLE) -f $(HEURISTIC) -a $(ALGORITHM)

solve-path:
	$(PYTHON) main.py $(PUZZLE) -f $(HEURISTIC) -a $(ALGORITHM) -p

random:
	$(PYTHON) main.py -s $(SIZE) -i $(ITERATIONS) -f $(HEURISTIC) -a $(ALGORITHM)

generate:
	@echo "# $(PYTHON) npuzzle-gen.py $(SIZE) $(GEN_FLAGS) -i $(ITERATIONS)"
	@$(PYTHON) npuzzle-gen.py $(SIZE) $(GEN_FLAGS) -i $(ITERATIONS)

clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} +