from .filter_solver import FilterSolver, DistinctFilterSolver
from .random_solver import RandomSolver

all_solvers = [
    RandomSolver,
    FilterSolver,
    DistinctFilterSolver,
]
