from sudoku import Board

class Solver(object):

    def __init__(self):
        self.tablero = Board()

    def some(self, seq):
        for e in seq:
            if e: return e
        return False

    def solver(self, tablero):
        r = []
        r.append(tablero)
        while len(r) > 0:
            original = r.pop()
            if original.is_solved():
                self.tablero = original
                return True
            t = original.minimo()
            if t[0] == 0:
                continue
            for a in original.cells[t[1]][t[2]]:
                copia = Board()
                copia.setup(original.clone())
                copia.set_value(t[1], t[2], a)
                r.append(copia)
        return False

    def solve(self, p):
        self.tablero.setup(p)
        print("Tablero Original")
        print(self.tablero)
        if self.solver(self.tablero):
            print("Solucion")
            print(self.tablero)
        else:
            print('No hay Solucion')

fd = open('sudoku.txt')
fd.readline()
p = fd.readline()
b = Solver()
b.solve(p)
