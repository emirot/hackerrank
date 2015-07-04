

class ConnectedCellInGrid():

    def __init__(self,arr, nb_row, nb_column):
        self.arr = arr
        self.nb_row = nb_row
        self.nb_column = nb_column
        self.max = 0
        self.count = 0
        self.stack = []


    def look_Down(self, current_y, current_x):
        i = 0
        if current_y + 1 < nb_row and arr[current_y+1][current_x] == 1:
            self.stack.append([current_y+1, current_x])
            self.arr[current_y+1][current_x] = 'X'
            self.count +=1

    def look_up(self, current_y, current_x):
        i = 0
        if current_y - 1 > 0 and arr[current_y - 1][current_x] == 1:
            self.stack.append([current_y - 1, current_x])
            self.arr[current_y - 1][current_x] = 'X'
            self.count +=1



    def look_right(self, current_y, current_x):
        i = 0
        if current_x + 1 < nb_column and arr[current_y][current_x + 1] == 1:
            self.stack.append([current_y, current_x + 1])
            self.arr[current_y][current_x+1] = 'X'
            self.count +=1


    def look_diag(self, current_y, current_x):
        i = 0
        if current_x + 1 < nb_column and current_y + 1 < nb_row  and arr[current_y+1][current_x + 1] == 1:
            self.stack.append([current_y+1, current_x + 1])
            self.arr[current_y+1][current_x+1] = 'X'
            self.count +=1

        if current_x - 1 >= 0 and current_y + 1 < nb_row  and arr[current_y + 1][current_x - 1] == 1:
            self.stack.append([current_y + 1, current_x - 1])
            self.arr[current_y + 1][current_x - 1] = 'X'
            self.count +=1

        if current_x - 1 >= 0 and current_y - 1 >= 0  and arr[current_y - 1][current_x - 1] == 1:
            self.stack.append([current_y - 1, current_x - 1])
            self.arr[current_y - 1][current_x - 1] = 'X'
            self.count +=1

        if current_x + 1 < nb_column and current_y - 1 >= 0  and arr[current_y - 1][current_x + 1] == 1:
            self.stack.append([current_y - 1, current_x + 1])
            self.arr[current_y - 1][current_x + 1] = 'X'
            self.count +=1


    def look_left(self, current_y, current_x):
        i = 0
        if current_x - 1 >= 0 and arr[current_y][current_x - 1] == 1:
            self.stack.append([current_y, current_x - 1])
            self.arr[current_y][current_x-1] = 'X'
            self.count +=1


    def nice_print(self):
        for i in range(nb_row):
            j = 0
            for j in range(nb_column):
                print(self.arr[i][j], end=' ')
            print()


    def look_every_where(self,i,j):
        self.look_Down(i, j)
        self.look_right(i, j)
        self.look_left(i, j)
        self.look_up(i, j)
        self.look_diag(i,j)

    def find_connected_cell(self):
        for i in range(nb_row):
            j = 0
            for j in range(nb_column):
                if self.arr[i][j] == 1:
                    self.count += 1
                    self.arr[i][j] = 'X'
                    self.look_every_where(i, j)
                    while len(self.stack) != 0:
                        a = self.stack.pop(0)
                        self.look_every_where(a[0], a[1])
                    if self.count > self.max:
                        self.max = self.count
                    self.count = 0
        print(self.max)


if __name__ == '__main__':
    nb_row = int(input())
    nb_column = int(input())
    arr = []
    for i in range(nb_row):
        line = input()
        a = list(map(int, line.split()))
        arr.append(a)
    c = ConnectedCellInGrid(arr, nb_row, nb_column)
    c.find_connected_cell()
