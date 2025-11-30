import itertools
import re


class FixedGrid:
    """Fixed-size 2D grid utility for Advent of Code puzzles.

    Coordinate Convention
    ---------------------
    All coordinates are expressed as (r, c) tuples where:
    - r is the row index (0 to height-1)
    - c is the column index (0 to width-1)

    Internal storage is a list-of-rows (self._grid) so indexing is
    self._grid[r][c]. All methods follow this (r, c) convention.
    """
    def __init__(self, grid):
        """Create a FixedGrid from a list-of-rows.

        Args:
            grid (list[list[Any]]): A non-empty list of rows. Each row must be
                a list with the same length (rectangular grid required).

        Raises:
            TypeError: If grid is not a list or any row is not a list.
            ValueError: If grid is empty, any row is empty, or rows have
                unequal lengths.
        """
        # Validate input: must be a non-empty rectangular sequence of rows
        if not isinstance(grid, list):
            raise TypeError("grid must be a list of rows")
        if len(grid) == 0:
            raise ValueError("grid must contain at least one row")
        row0 = grid[0]
        if not isinstance(row0, list):
            raise TypeError("each row in grid must be a list")
        width = len(row0)
        if width == 0:
            raise ValueError("grid rows must contain at least one column")
        for i, row in enumerate(grid):
            if not isinstance(row, list):
                raise TypeError(f"row {i} is not a list")
            if len(row) != width:
                raise ValueError("all rows in grid must have the same length")

        self._grid = grid
        self._height = len(self._grid)
        self._width = width
        # cached columns (invalidated on mutation)
        self._columns_cache = None

    @staticmethod
    def parse(s, linesplit_fn=None, line_separator='\n', value_fn=None):
        """Parse a string into a FixedGrid.

        Args:
            s (str): The string to parse.
            linesplit_fn (callable, optional): Function to split each line into
                values. If None, each character becomes a cell.
                Example: str.split or lambda line: line.split(',').
            line_separator (str): String used to split lines. Defaults to '\\n'.
            value_fn (callable, optional): Function to transform each parsed
                value. Example: int to convert strings to integers.

        Returns:
            FixedGrid: The parsed grid.

        Raises:
            See __init__ for validation errors on empty or non-rectangular grids.

        Example:
            >>> G = FixedGrid.parse("abc\\ndef")
            >>> G[0, 1]
            'b'
            >>> G2 = FixedGrid.parse("1,2\\n3,4", linesplit_fn=lambda x: x.split(','), value_fn=int)
            >>> G2[1, 0]
            3
        """
        grid = []
        for line in s.split(line_separator):
            if linesplit_fn is not None:
                parts = linesplit_fn(line)
            else:
                parts = list(line)
            if value_fn is None:
                grid.append(list(parts))
            else:
                grid.append(list(map(value_fn, parts)))
        return FixedGrid(grid)

    @staticmethod
    def from_dict(d, missing=None):
        """Converts a coordinate->value dictionary to a FixedGrid.

        Accepts mappings where keys are (r, c) tuples (row, column). The
        grid returned will cover the minimal bounding rectangle of the keys
        (i.e. from min row/min column to max row/max column). Missing
        coordinates are filled with the provided missing value.

        Args:
            d (dict): Mapping from (r, c) -> value.
            missing: Value to use for coordinates not present in the dictionary.
                Defaults to None.

        Returns:
            FixedGrid: Grid spanning the bounding rectangle of provided keys.

        Raises:
            ValueError: If d is empty.

        Example:
            >>> d = {(0, 0): 'a', (0, 2): 'c', (1, 1): 'x'}
            >>> G = FixedGrid.from_dict(d, missing='.')
            >>> G.as_str('')
            'a.c\\n.x.'
        """
        if not d:
            raise ValueError("from_dict requires a non-empty dictionary")

        low_r = min(r for r, c in d.keys())
        high_r = max(r for r, c in d.keys())
        low_c = min(c for r, c in d.keys())
        high_c = max(c for r, c in d.keys())

        rows = []
        for r in range(low_r, high_r + 1):
            row = [d.get((r, c), missing) for c in range(low_c, high_c + 1)]
            rows.append(row)

        return FixedGrid(rows)

    @staticmethod
    def default_fill(width, height, value):
        """
        Create a FixedGrid of specified dimensions filled with a default value.

        Args:
            width (int): The number of columns in the grid.
            height (int): The number of rows in the grid.
            value: The default value to fill in each cell of the grid.

        Returns:
            FixedGrid: A grid where each cell is filled with the specified default value.
        """
        return FixedGrid([[value for _ in range(width)] for _ in range(height)])

    def to_dict(self):
        """
        Convert the grid to a coordinate->value dictionary.

        Returns:
            dict: A dictionary from (r,c) coordinates to the value at that
                coordinate in the grid.
        """
        return {(r,c): val
                for r,row in enumerate(self._grid)
                for c,val in enumerate(row)}

    def transpose(self):
        """
        Transpose the grid.

        Returns:
            FixedGrid: A new FixedGrid instance with rows and columns swapped.
        """
        # return FixedGrid([[self._grid[r][c]
        #                   for c in range(self._width)]
        #                    for r in range(self._height)])
        return FixedGrid(list(map(list, zip(*self._grid))))

    @property
    def width(self):
        """
        Retrieve the width of the grid.

        Returns:
            int: The width of the grid.
        """
        return self._width

    @property
    def height(self):
        """
        Retrieve the height of the grid.

        Returns:
            int: The height of the grid.
        """
        return self._height

    @property
    def rows(self):
        """
        Retrieve the rows of the grid.

        Returns:
            list: A list of lists, where each inner list contains the elements of a row in the grid.
        """
        return self._grid

    @property
    def columns(self):
        """
        Retrieve the columns of the grid.

        Returns:
            list: A list of tuples, where each tuple contains the elements of a column in the grid.
        """
        # cache columns to avoid recomputing on every access; invalidate on mutations
        if self._columns_cache is None:
            # convert to tuples to keep the columns immutable-like
            self._columns_cache = [tuple(col) for col in zip(*self._grid)]
        return self._columns_cache

    @property
    def area(self):
        """
        Calculate the area of the grid.

        Returns:
            int: The area of the grid, calculated as the product of its width and height.
        """
        return self._width * self._height

    def __contains__(self, coord):
        """
        Check if a coordinate is contained within the grid.

        Parameters:
        - coord (tuple): A tuple representing the (row, column) coordinate.

        Returns:
        - bool: True if the coordinate is within the grid bounds, False otherwise.
        """
        r, c = coord
        return 0 <= r < self._height and 0 <= c < self._width

    def __getitem__(self, coord):
        """Retrieve the value at a specific coordinate in the grid.

        Args:
            coord (tuple[int, int]): The (row, column) coordinate.

        Returns:
            Any: The value at the specified coordinate.

        Raises:
            AssertionError: If the coordinate is out of bounds.

        Example:
            >>> G = FixedGrid([['a', 'b'], ['c', 'd']])
            >>> G[0, 1]
            'b'
        """
        r, c = coord
        assert(0 <= r < self._height and 0 <= c < self._width)
        return self._grid[r][c]

    def __setitem__(self, coord, val):
        """Set the value at a specific coordinate in the grid.

        Args:
            coord (tuple[int, int]): The (row, column) coordinate.
            val (Any): The value to set at the specified coordinate.

        Raises:
            AssertionError: If the coordinate is out of bounds.

        Note:
            This method mutates the grid and invalidates the cached columns.
        """
        r, c = coord
        assert(0 <= r < self._height and 0 <= c < self._width)
        self._grid[r][c] = val
        # mutation invalidates cached columns
        self._columns_cache = None

    def items(self, column_first=False):
        """Generate all (coordinate, value) pairs in the grid.

        Args:
            column_first (bool): If True, iterate column-major order (all cells
                in column 0, then column 1, etc.). If False (default), iterate
                row-major order (all cells in row 0, then row 1, etc.).

        Yields:
            tuple[tuple[int, int], Any]: Yields ((r, c), value) pairs.

        Example:
            >>> G = FixedGrid([['a', 'b'], ['c', 'd']])
            >>> list(G.items())
            [((0, 0), 'a'), ((0, 1), 'b'), ((1, 0), 'c'), ((1, 1), 'd')]
        """
        if column_first:
            for c in range(self._width):
                for r, row in enumerate(self._grid):
                    yield (r, c), row[c]
        else:
            for r, row in enumerate(self._grid):
                for c, val in enumerate(row):
                    yield (r, c), val

    def adj(self, r, c, diagonals=False, ignore_bounds=False):
        """Yield adjacent coordinates to (r, c).

        Args:
            r (int): Row index of the cell.
            c (int): Column index of the cell.
            diagonals (bool): If True, include diagonal neighbors (8 total).
                If False (default), only cardinal directions (4 total: up, down,
                left, right).
            ignore_bounds (bool): If True, yield coordinates even if they fall
                outside the grid. If False (default), only yield valid in-bounds
                coordinates.

        Yields:
            tuple[int, int]: Adjacent (row, column) coordinates.

        Raises:
            AssertionError: If (r, c) is out of bounds and ignore_bounds is False.

        Example:
            >>> G = FixedGrid([['a', 'b', 'c'], ['d', 'e', 'f']])
            >>> list(G.adj(0, 1))  # middle of top row
            [(0, 0), (0, 2), (1, 1)]
            >>> list(G.adj(0, 1, diagonals=True))
            [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)]

        Usage:
            for nr, nc in G.adj(r, c)
        """
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
        """
        Print the grid to the console.

        Args:
            line_spacing (str): The string to insert between elements of a row when printing.
        """
        print(self.as_str(line_spacing))

    def as_str(self, line_spacing=' '):
        """
        Convert the grid to a string representation.

        Args:
            line_spacing (str): The string to insert between elements of a row.

        Returns:
            str: A string representation of the grid, where each row is joined by the specified line_spacing
                and rows are separated by newlines.
        """
        return "\n".join(line_spacing.join(map(str, row)) for row in self._grid)

    def find(self, ch):
        """Find the first occurrence of a value in the grid.

        Args:
            ch: The value to search for (compared using ==).

        Returns:
            tuple[int, int] | None: The (row, column) coordinate of the first
                occurrence, or None if not found. Scans row-major order.

        Example:
            >>> G = FixedGrid([['a', 'b'], ['c', 'b']])
            >>> G.find('b')
            (0, 1)
            >>> G.find('z') is None
            True
        """
        for r, row in enumerate(self._grid):
            for c, val in enumerate(row):
                if val == ch:
                    return r, c
        return None

    def findr(self, regex):
        """Find the first occurrence of a value matching a regex pattern.

        Args:
            regex (str | re.Pattern): Regular expression pattern to match.
                Uses re.match, so pattern must match from the start of the value.

        Returns:
            tuple[int, int] | None: The (row, column) coordinate of the first
                match, or None if no match is found. Scans row-major order.

        Example:
            >>> G = FixedGrid([['a1', 'b2'], ['c3', 'd4']])
            >>> G.findr(r'[cd]\\d')
            (1, 0)
            >>> G.findr(r'z.*') is None
            True
        """
        for r, row in enumerate(self._grid):
            for c, val in enumerate(row):
                if re.match(regex, val):
                    return r, c
        return None

    def find_all(self, ch):
        """Find all positions where a value equals the given character.

        Args:
            ch (str): The character to search for.

        Returns:
            list[tuple[int, int]]: List of (row, column) coordinates for all
                occurrences of ch. Returns empty list if not found.

        Example:
            >>> G = FixedGrid([['a', 'b'], ['a', 'd']])
            >>> G.find_all('a')
            [(0, 0), (1, 0)]
            >>> G.find_all('z')
            []
        """
        return [(r, c) for r, row in enumerate(self._grid)
                for c, val in enumerate(row) if val == ch]

    def find_allr(self, regex):
        """Find all positions where a value matches the given regex.

        Uses re.match(), so the pattern must match from the start of the string.

        Args:
            regex (str): The regular expression pattern to search for.

        Returns:
            list[tuple[int, int]]: List of (row, column) coordinates for all
                matches. Returns empty list if no matches found.

        Example:
            >>> G = FixedGrid([['a1', 'b2'], ['c3', 'a4']])
            >>> G.find_allr(r'a\\d')
            [(0, 0), (1, 1)]
            >>> G.find_allr(r'z.*')
            []
        """
        return [
            (r, c)
            for r, row in enumerate(self._grid)
            for c, val in enumerate(row)
            if re.match(regex, val)
        ]

    def rotate(self):
        """Rotate the grid 90 degrees clockwise IN-PLACE.

        This method mutates the grid directly. The width and height are updated,
        and cached properties (like columns) are invalidated.

        Returns:
            None

        Note:
            If you need a rotated copy without mutating the original, use
            G.quick_copy().rotate() or manually build a new grid.

        Example:
            >>> G = FixedGrid([['a', 'b'], ['c', 'd']])
            >>> G.rotate()
            >>> G.as_str('')
            'ca\\ndb'
        """
        self._grid = list(map(list, zip(*self._grid[::-1])))
        # update cached dimensions and invalidate derived caches
        self._height = len(self._grid)
        self._width = len(self._grid[0]) if self._grid and self._grid[0] else 0
        self._columns_cache = None
        # Note: this method mutates the grid in-place. Use `transpose()` if you need a new FixedGrid.

    def quick_copy(self):
        """
        Create a quick copy of the grid.

        This is a convenience function for creating a copy of the grid. It is
        implemented by serializing the grid to a string and then parsing it back into
        a new grid.

        Returns:
            FixedGrid: A new FixedGrid object with the same values as the original
        """
        # shallow-copy rows to preserve element types while avoiding shared lists
        return FixedGrid([row[:] for row in self._grid])
