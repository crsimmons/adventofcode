import itertools


class FixedGrid:
    '''Fixed size grid utility class to simplify grid operations and minimize
    bugs.
    '''
    def __init__(self, grid):
        self._grid = grid
        self._height = len(self._grid)
        self._width = len(self._grid[0])

    @staticmethod
    def parse(s, linesplit_fn=None, line_separator='\n', value_fn=None):
        grid = []
        for line in s.split(line_separator):
            if linesplit_fn is not None:
                line = linesplit_fn(line)
            if value_fn is None:
                grid.append(list(line))
            else:
                grid.append(list(map(value_fn, line)))
        return FixedGrid(grid)

    @staticmethod
    def from_dict(d, missing=None):
        '''Converts a coordinate->value dictionary to a FixedGrid.
        Expects that minimum r and c coordinates in the grid are both 0.

        Arguments:
        missing -- Value to use for any coordinates not present in the dictionary
        '''
        low_r, high_r = None, None
        low_c, high_c = None, None
        for c, r in d.keys():
            if low_c is None:
                low_r, high_r = r, r
                low_c, high_c = c, c
            else:
                low_r = min(low_r, r)
                high_r = max(high_r, r)
                low_c = min(low_c, c)
                high_c = max(high_c, c)

        assert(low_r == low_c == 0)

        return FixedGrid([[d.get((r, c), missing)
                           for r in range(low_r, high_r+1)]
                          for c in range(low_c, high_c+1)])

    def to_dict(self):
        return {(r,c): val
                for r,row in enumerate(self._grid)
                for c,val in enumerate(row)}

    def transpose(self):
        return FixedGrid([[self._grid[r][c]
                          for c in range(self._width)]
                           for r in range(self._height)])

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def rows(self):
        return self._grid

    @property
    def columns(self):
        return list(zip(*self._grid))

    @property
    def area(self):
        return self._width * self._height

    def __contains__(self, coord):
        r, c = coord
        return 0 <= r < self._height and 0 <= c < self._width

    def __getitem__(self, coord):
        r, c = coord
        assert(0 <= r < self._height and 0 <= c < self._width)
        return self._grid[r][c]

    def __setitem__(self, coord, val):
        r, c = coord
        assert(0 <= r < self._height and 0 <= c < self._width)
        self._grid[r][c] = val

    def items(self, column_first = False):
        '''Generates all coordinate,value pairs in the grid for iteration.

        Arguments:
        column_first -- Iterate by column first rather than by row first
        '''
        if column_first:
            for c in range(self._width):
                for r, row in enumerate(self._grid):
                    yield (r, c), row[c]
        else:
            for r, row in enumerate(self._grid):
                for c, val in enumerate(row):
                    yield (r, c), val

    def adj(self, r, c, diagonals=False, ignore_bounds=False):
        if not ignore_bounds:
            assert(0 <= r < self._height and 0 <= c < self._width)
        if diagonals:
            for nr, nc in itertools.product((r-1, r, r+1),
                                            (c-1, c, c+1)):
                if r == nr and c == nc:
                    continue
                if (0 <= nr < self._height and 0 <= nc < self._width) or ignore_bounds:
                    yield nr, nc
        else:
            if ignore_bounds:
                yield r-1, c
                yield r+1, c
                yield r, c-1
                yield r, c+1
            else:
                if 0 < r:
                    yield r-1, c
                if r+1 < self._height:
                    yield r+1, c
                if 0 < c:
                    yield r, c-1
                if c+1 < self._width:
                    yield r, c+1

    def print(self, line_spacing=' '):
        print(self.as_str(line_spacing))

    def as_str(self, line_spacing=' '):
        return '\n'.join(line_spacing.join(str(self._grid[r][c])
                                           for c in range(self._height))
                         for r in range(self._width))

    def find(self, ch):
        """
        Find the first occurrence of a character in the grid.

        Args:
            ch (str): The character to search for.

        Returns:
            tuple[int, int] or None: The index of the first occurrence of the character in the grid,
                represented as a tuple (row, column). Returns None if the character is not found.
        """
        for r, row in enumerate(self._grid):
            for c, val in enumerate(row):
                if val == ch:
                    return r, c
        return None

    def find_all(self, ch):
        """
        Find all occurrences of a character in the grid.

        Parameters:
            ch (str): The character to search for.

        Returns:
            list of tuples: A list of tuples representing the row and column indices of all occurrences of the character in the grid.
        """
        return [(r, c) for r, row in enumerate(self._grid)
                for c, val in enumerate(row) if val == ch]

    def rotate(self):
        """
        Rotate the grid clockwise.

        This function rotates the grid clockwise by reversing the order of the rows and then transposing the columns.
        It does not take any parameters.

        Returns:
        - None
        """
        self._grid = list(map(list, zip(*self._grid[::-1])))
        # return FixedGrid(list(map(list, zip(*self._grid[::-1]))))
