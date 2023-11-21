import copy
from rubik_solver.Move import Move
from .. import Solver
from ..Beginner import WhiteCrossSolver
from . import F2LSolver
from . import OLLSolver
from . import PLLSolver

# from rubik_solver.Printer import TtyPrinter

class CFOPSolver(Solver):
    def solution(self):

        # print("CFOPSolver.solution: start")
        # printer = TtyPrinter(self.cube, True)
        # printer.pprint()

        cube = copy.deepcopy(self.cube)
        solution = WhiteCrossSolver.WhiteCrossSolver(cube).solution()

        # print("CFOPSolver.solution: after WhiteCrossSolver")
        # printer = TtyPrinter(cube, True)
        # printer.pprint()

        solution += F2LSolver.F2LSolver(cube).solution()
        solution += OLLSolver.OLLSolver(cube).solution()
        solution += PLLSolver.PLLSolver(cube).solution()
        # Align top layer
        while cube.cubies['F'].facings['F'] != cube.cubies['FU'].facings['F']:
            cube.move(Move('U'))
        return [Move(m) for m in solution]
