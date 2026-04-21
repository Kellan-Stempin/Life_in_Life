class Component:
    def __init__(self, pattern, top, left, frozen=False, name=""):
        self.pattern = pattern
        self.top = top
        self.left = left
        self.frozen = frozen
        self.name = name

    def place(self, grid):
        rows, cols = grid.shape

        for r, c in self.pattern:
            rr = self.top + r
            cc = self.left + c

            if 0 <= rr < rows and 0 <= cc < cols:
                grid[rr, cc] = 1