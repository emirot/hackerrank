def search(grid, pattern):
   for i, grid_row in enumerate(grid):
      for pattern_row in pattern:
         if i >= len(grid): break
         grid_row = grid[i]
         if pattern_row not in grid_row: break
         # print(i)
         i += 1
      else:
         return 'YES'
   return 'NO'


test_cases = int(input())
for n in range(0, test_cases):
   grid_height, grid_width = tuple(map(int, input().split(' ')))
   grid = []
   for i in range(0, grid_height):
      grid.append(input())

   #print(grid)
   pattern_height, pattern_width = tuple(map(int, input().split(' ')))
   pattern = []
   for i in range(0, pattern_height):
      pattern.append(input())
  # print(pattern)
   print(search(grid, pattern))