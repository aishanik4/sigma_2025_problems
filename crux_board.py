#class definition
class Solution:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):  
        return (f"X: {self.x}, Y: {self.y}")
    def __lt__(self, other):
        return self.x < other.x
    def __repr__(self):
        return f"Solution(x='{self.x}', y={self.y})"

#initialize variables
board_structure = []
rows_from_file = []
solutions = []

#read the input file and process records
with open("crux-input.txt","r") as file: 
    first_line_processed = False
    for line in file:
        line = line.strip()
        if first_line_processed == False:
            words = line.split()
            rows = int(words[0])
            cols = int(words[1])
            print('row:', rows,', clols: ', cols)

            board_structure = [[0 for _ in range(cols)] for _ in range(rows)]    
            first_line_processed = True
        else:
            rows_from_file.append(line)

# check min rows and columns
if rows <3 or cols < 3:
    print("Error: not many rows/columns in the supplied data file")
    exit()

#print('initial:', board_structure)

#Populate each row with tiles and empty spots
for top_index, record_row in enumerate(rows_from_file):
    for inner_index, char in enumerate(list(record_row)):
        board_structure[top_index][inner_index] = char

#print('updated:', board_structure)

# logic to go through each row and apply the crux logic
for row_index, row_data in enumerate(board_structure):
    #print('print each row data:', row_index, row_data)

    if (row_index > len(board_structure)-3): #Skip the last two rows as diamond shape require 3 rows
        continue
    else: #log for all remaining rows
        # Exclude the first and last spots for all the rows
        emptySpot = {}
        for column_index, each_spot_val in enumerate(row_data):
            total_tiles_in_this_iteration = 0
            
            if(column_index==0 or column_index == len(row_data)-1): #skip the first spot and the last spot
                continue
            
            if(each_spot_val=='X'): #current row check
                total_tiles_in_this_iteration = total_tiles_in_this_iteration+1
            else:
                emptySpot = Solution(row_index, column_index)

            #check for next two row values to form the diamond shape

            #check values in index+1 row and create Solution, if it is empty spot
            n_plus_1_row = board_structure[row_index+1]
            if n_plus_1_row[column_index-1] == 'X':
                total_tiles_in_this_iteration = total_tiles_in_this_iteration+1
            else:
                emptySpot = Solution(row_index+1, column_index-1)

            if n_plus_1_row[column_index] == 'X':
                total_tiles_in_this_iteration = total_tiles_in_this_iteration+1
            else:
                emptySpot = Solution(row_index+1, column_index)

            if n_plus_1_row[column_index+1] == 'X':
                total_tiles_in_this_iteration = total_tiles_in_this_iteration+1
            else:
                emptySpot = Solution(row_index+1, column_index+1)
                        
            #check values in index+2 row and create Solution, if it is empty spot
            n_plus_2_row = board_structure[row_index+2]
            if n_plus_2_row[column_index] == 'X':
                total_tiles_in_this_iteration = total_tiles_in_this_iteration+1
            else:
                emptySpot = Solution(row_index+2, column_index)

            print('total tiles in this iteration: ', total_tiles_in_this_iteration)
            
            #the solution is valid only if the total tiles in the current diamond structure is 4
            if(total_tiles_in_this_iteration == 4):
                solutions.append(emptySpot)

print('ALL POSSIBLE SOLUTIONS:')
for sol in solutions:
    print(sol)

str_write = {}
if len(solutions) == 0:
    str_write = "NONE"
    print('NO SOLUTION:')
else:
    print('BEST SOLUTION:')
    str_write = f"{solutions[0].x} {solutions[0].y}"

file = open("crux-output.txt","w")
file.write(f"{str_write}")
file.close()
exit()