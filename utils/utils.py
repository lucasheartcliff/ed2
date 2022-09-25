import csv

def read_matrix_from_csv(filename):
    matrix = []
    rows_size = -1
    with open(filename, "r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            matrix_row = []
            for cell in row:
                value = None
                if cell == "1":
                    value = True
                if cell == "0":
                    value = False

                if value == None:
                    continue
                matrix_row.append(value)
            if len(matrix_row) != rows_size and rows_size != -1:
                raise Exception(
                    "Invalid matrix in file, the matrix rows should have the same size."
                )
            else:
                rows_size = len(matrix_row)
                matrix.append(matrix_row)

    if len(matrix) != rows_size:
        raise Exception(
            "Invalid matrix in file, the matrix should have the same size of the rows."
        )

    return matrix
