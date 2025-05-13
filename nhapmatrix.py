def create_matrix(size):
    matrix = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(0)
        matrix.append(row)
    return matrix

def input_matrix(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if i == j:
                matrix[i][j] = 1
            elif j < i:
                matrix[i][j] = round(1 / matrix[j][i], 4)
            else:
                valid_input = False
                while not valid_input:
                    value = input(f"Nhập giá trị phần tử [{i + 1}, {j + 1}] (từ 0 đến 9 hoặc số thực): ")
                    try:
                        if '/' in value:
                            numerator, denominator = value.split('/')
                            value = float(numerator) / float(denominator)
                        else:
                            value = float(value)
                        if 0 <= value <= 9:
                            matrix[i][j] = round(value, 4)
                            valid_input = True
                        else:
                            print("Giá trị không hợp lệ. Vui lòng nhập lại.")
                    except ValueError:
                        print("Giá trị không hợp lệ. Vui lòng nhập lại.")
                        
def print_matrix(matrix):
    for row in matrix:
        print(row)

def column_sums(matrix):
    size = len(matrix)
    sums = [0] * size
    for i in range(size):
        for j in range(size):
            sums[j] += matrix[i][j]
    return sums

def create_pairwise_matrix(matrix):
    size = len(matrix)
    pairwise_matrix = [[0] * size for _ in range(size)]
    column_sums_result = column_sums(matrix)
    for i in range(size):
        for j in range(size):
            pairwise_matrix[i][j] = round(matrix[i][j] / column_sums_result[j], 4)
    return pairwise_matrix

def calculate_cw(pairwise_matrix):
    size = len(pairwise_matrix)
    cw = []
    for i in range(size):
        cw.append(sum(pairwise_matrix[i][j] for j in range(size)) / size)
    return cw

def print_pairwise_matrix(pairwise_matrix):
    for row in pairwise_matrix:
        print(row)

def print_cw(cw):
    print("Trọng số của các tiêu chí:")
    for i, weight in enumerate(cw):
        print(f"Tiêu chí {i + 1}: {weight:.5f}")

def calculate_consistency_ratio(matrix, cw):
    size = len(matrix)
    weighted_sum = [0] * size

    for i in range(size):
        for j in range(size):
            weighted_sum[i] += matrix[i][j] * cw[j]

    lambda_max = sum(weighted_sum[i] / cw[i] for i in range(size)) / size
    consistency_index = (lambda_max - size) / (size - 1)
    

    cr_table = {1: 0, 2: 0, 3: 0.58, 4: 0.9, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49,
11: 1.51, 12: 1.48, 13: 1.56, 14: 1.57, 15: 1.59}

    consistency_ratio = consistency_index / cr_table[size]

    return consistency_ratio, consistency_index, lambda_max

def rank_criteria(cw):
    sorted_indices = sorted(range(len(cw)), key=lambda i: cw[i], reverse=True)
    ranks = {sorted_indices[i]: i+1 for i in range(len(sorted_indices))}
    return ranks

def nhap_ma_tran_so_sanh_cap(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if i == j:
                matrix[i][j] = 1
            elif j < i:
                matrix[i][j] = round(1 / matrix[j][i], 4)
            else:
                valid_input = False
                while not valid_input:
                    value = input(f"Nhập giá trị phần tử [{i + 1}, {j + 1}] (từ 0 đến 9 hoặc số thực): ")
                    try:
                        if '/' in value:
                            numerator, denominator = value.split('/')
                            value = float(numerator) / float(denominator)
                        else:
                            value = float(value)
                        if 0 <= value <= 9:
                            matrix[i][j] = round(value, 4)
                            valid_input = True
                        else:
                            print("Giá trị không hợp lệ. Vui lòng nhập lại.")
                    except ValueError:
                        print("Giá trị không hợp lệ. Vui lòng nhập lại.")

# def calculate_comparison_matrix(matrix, cw):
#     comparison_matrix = []
#     for i in range(len(matrix)):
#         row = []
#         for j in range(len(matrix[i])):
#             row.append(matrix[i][j] * cw[j])
#         comparison_matrix.append(row)
#     return comparison_matrix


# def create_weight_matrix(cw):
#     """
#     Tạo ma trận gom trọng số từ ma trận cw.

#     Parameters:
#     cw (list): Ma trận nhị phân chứa giá trị của λmax và các hệ số ri cho mỗi cặp so sánh cặp.

#     Returns:
#     list: Ma trận gom trọng số của các bảng, mỗi hàng chứa một trọng số.
#     """
#     num_tables = len(cw)
#     weight_matrix = [[0] * num_tables for _ in range(num_tables)]

#     for i in range(num_tables):
#         # Tính tổng của các giá trị trọng số của bảng
#         total_weight = sum(cw[i][j] for j in range(num_tables))

#         # Gán giá trị trọng số cho từng bảng
#         for j in range(num_tables):
#             weight_matrix[j][i] = cw[i][j] / total_weight

#     return weight_matrix

def calculate_PA(matrix, weights):
    PAs = []

    for row in matrix:
        PA = sum(row[i] * weights[i] for i in range(len(row)))
        PAs.append(PA)

    return PAs