# Island Perimeter Interview Challenge

## Objective

Create a function `def island_perimeter(grid):` that calculates and returns the perimeter of the island described in the grid.

## Description

- **Grid Representation**:
	- The grid is a list of lists of integers.
	- `0` represents water.
	- `1` represents land.
	- Each cell in the grid is square with a side length of 1.
	- Cells are connected horizontally or vertically (not diagonally).

- **Constraints**:
	- The grid is rectangular, with its width and height not exceeding 100.
	- The grid is completely surrounded by water.
	- There is only one island or no island at all.
	- The island does not contain any lakes (water inside that isn’t connected to the water surrounding the island).

## Function Signature

```python
def island_perimeter(grid):
		# Your code here
```

## Example

Given the following grid:

```
[
	[0, 1, 0, 0],
	[1, 1, 1, 0],
	[0, 1, 0, 0],
	[1, 1, 0, 0]
]
```

The function should return `16` as the perimeter of the island.

## Explanation

In the example grid:
- The island cells are connected horizontally and vertically.
- The perimeter is calculated by counting the edges of the land cells that are adjacent to water or the grid boundary.

## Usage

To use the `island_perimeter` function, pass a grid as an argument:

```python
grid = [
	[0, 1, 0, 0],
	[1, 1, 1, 0],
	[0, 1, 0, 0],
	[1, 1, 0, 0]
]

print(island_perimeter(grid))  # Output: 16
```

This will output the perimeter of the island in the given grid.
