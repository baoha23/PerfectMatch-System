import streamlit as st
import pandas as pd
import numpy as np


def create_empty_matrix(size):
    matrix = np.identity(size)
    return matrix


def input_matrix(matrix, row_labels, col_labels, matrix_key):
    for i in range(len(row_labels)):
        for j in range(i + 1, len(col_labels)):
            key = f"{matrix_key}_{i}_{j}"
            value = st.number_input(f"Nhập giá trị [{row_labels[i]}, {col_labels[j]}]: ", min_value=0.0, max_value=9.0, step=0.1, format="%.2f", key=key)
            matrix[i][j] = round(value, 2)
            matrix[j][i] = round(1 / value, 2) if value != 0 else 0
    return matrix

def calculate_weights(matrix):
    normalized_matrix = matrix / matrix.sum(axis=0)
    weights = normalized_matrix.mean(axis=1)
    return weights

def calculate_lambda_max(matrix, weights):
    weighted_sum = matrix.dot(weights)
    lambda_max = np.mean(weighted_sum / weights)
    return round(lambda_max, 4)

# Tính CR
# def calculate_consistency_ratio(matrix, weights):
#     lambda_max = calculate_lambda_max(matrix, weights)
#     n = matrix.shape[0]
#     CI = (lambda_max - n) / (n - 1)
#     RI_dict = {1: 0.00, 2: 0.00, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
#     RI = RI_dict.get(n, 1.49)
#     CR = CI / RI
#     return round(CR * 100, 2)  # Chuyển đổi CR thành phần trăm và làm tròn đến 2 chữ số thập phân
def calculate_consistency_ratio(matrix, weights):
    lambda_max = calculate_lambda_max(matrix, weights)
    n = matrix.shape[0]
    CI = (lambda_max - n) / (n - 1)
    RI_dict = {1: 0.00, 2: 0.00, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
    RI = RI_dict.get(n, 1.49)
    CR = CI / RI
    return round(CR, 4)

def rank_criteria(weights):
    sorted_indices = sorted(range(len(weights)), key=lambda i: weights[i], reverse=True)
    ranks = {i: rank + 1 for rank, i in enumerate(sorted_indices)}
    return ranks

def calculate_PA(matrix, weights):
    PAs = []
    for row in matrix:
        PA = sum(row[i] * weights[i] for i in range(len(row)))
        PAs.append(PA)
    return PAs
