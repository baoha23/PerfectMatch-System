import nhapmatrix

def print_header(text):
    print(f"\033[95m\033[1m{text}\033[0m")

def print_subheader(text):
    print(f"\033[94m\033[1m{text}\033[0m")

def main():
    print_header("CHƯƠNG TRÌNH HỖ TRỢ LỰA CHỌN TIÊU CHÍ")
    matrix_size = int(input("Nhập kích thước của ma trận ban đầu: "))
    initial_matrix = nhapmatrix.create_matrix(matrix_size)

    print_subheader("Nhập giá trị cho ma trận ban đầu (từ trên xuống dưới, từ trái sang phải):")
    nhapmatrix.input_matrix(initial_matrix)

    print_subheader("Ma trận AHP ban đầu:")
    nhapmatrix.print_matrix(initial_matrix)

    initial_column_sums = nhapmatrix.column_sums(initial_matrix)
    print_subheader("Tổng của từng cột trong ma trận ban đầu (Sum):")
    print(initial_column_sums)
    
    initial_pairwise_matrix = nhapmatrix.create_pairwise_matrix(initial_matrix)
    print_subheader("Ma trận Pair-wise ban đầu:")
    nhapmatrix.print_matrix(initial_pairwise_matrix)
    
    initial_cw = nhapmatrix.calculate_cw(initial_pairwise_matrix)
    print_subheader("CW của ma trận ban đầu:")
    nhapmatrix.print_cw(initial_cw)
    
    consistency_ratio, consistency_index, lambda_max = nhapmatrix.calculate_consistency_ratio(initial_matrix, initial_cw)
    print_subheader(f"Consistency Index (CI) của ma trận ban đầu: {consistency_index:.5f}")
    print(f"Lambda max (λmax) của ma trận ban đầu: {lambda_max:.5f}")
    print(f"Consistency Ratio (CR) của ma trận ban đầu: {consistency_ratio:.5f}")

    if consistency_ratio > 0.1:
        print("\033[91mConsistency Ratio của ma trận ban đầu vượt quá 10%. Vui lòng nhập lại các tiêu chí.\033[0m")
        main()
    else:
        initial_ranks = nhapmatrix.rank_criteria(initial_cw)
        print_subheader("Hạng của các tiêu chí của ma trận ban đầu (từ cao đến thấp):")
        for criterion, rank in initial_ranks.items():
            print(f"Tiêu chí {criterion + 1}: Hạng {rank}")
        
    num_new_matrices = int(input("\nNhập số lượng ma trận mới cần tính toán: "))
    cw_new_matrices = []
    for i in range(num_new_matrices):
        print_header(f"\nMa trận mới thứ {i+1}:")
        new_matrix = nhapmatrix.create_matrix(matrix_size)
        print_subheader("Nhập giá trị cho ma trận mới (từ trên xuống dưới, từ trái sang phải):")
        nhapmatrix.input_matrix(new_matrix)

        print_subheader("Ma trận theo từng tiêu chí:")
        nhapmatrix.print_matrix(new_matrix)

        new_column_sums = nhapmatrix.column_sums(new_matrix)
        print_subheader("Tổng của từng cột trong ma trận mới (Sum):")
        print(new_column_sums)
        
        new_pairwise_matrix = nhapmatrix.create_pairwise_matrix(new_matrix)
        print_subheader("Ma trận Pair-wise mới:")
        nhapmatrix.print_matrix(new_pairwise_matrix)
        
        new_cw = nhapmatrix.calculate_cw(new_pairwise_matrix)
        cw_new_matrices.append(new_cw)
        print_subheader("CW của ma trận mới:")
        nhapmatrix.print_cw(new_cw)
        
        consistency_ratio_new, consistency_index_new, lambda_max_new = nhapmatrix.calculate_consistency_ratio(new_matrix, new_cw)
        print_subheader(f"Consistency Index (CI) của ma trận mới: {consistency_index_new:.5f}")
        print(f"Lambda max (λmax) của ma trận mới: {lambda_max_new:.5f}")
        print(f"Consistency Ratio (CR) của ma trận mới: {consistency_ratio_new:.5f}")

        if consistency_ratio_new > 0.1:
            print("\033[91mConsistency Ratio của ma trận mới vượt quá 10%. Vui lòng nhập lại các tiêu chí.\033[0m")
        else:
            new_ranks = nhapmatrix.rank_criteria(new_cw)
            print_subheader("Hạng của các tiêu chí của ma trận mới (từ cao đến thấp):")
            for criterion, rank in new_ranks.items():
                print(f"Tiêu chí {criterion + 1}: Hạng {rank}")
                
    final_scores = [0] * num_new_matrices
    for alt_cw, crit_cw in zip(cw_new_matrices, initial_cw):
        for i in range(num_new_matrices):
            final_scores[i] += alt_cw[i] * crit_cw
            
    sorted_final_scores = sorted(enumerate(final_scores), key=lambda x: x[1], reverse=True)
    print_header("Phương án tốt nhất (từ cao đến thấp):")
    for index, score in sorted_final_scores:
        print(f"Phương án {index + 1}: {score:.5f}")

if __name__ == "__main__":
    main()
