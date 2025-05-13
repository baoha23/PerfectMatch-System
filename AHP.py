import streamlit as st
import pandas as pd
import numpy as np
from ham import create_empty_matrix, input_matrix, calculate_weights, calculate_lambda_max, calculate_consistency_ratio, rank_criteria, calculate_PA

def main():
    st.set_page_config(page_title="Hỗ trợ lựa chọn một người bạn phù hợp", page_icon=":bar_chart:")

    # Sử dụng CSS để làm đẹp tiêu đề
    st.markdown("""
        <style>
        .title {
            text-align: center;
            color: #2ECC40;
            font-size: 30px;
            font-weight: bold;
        }
        .header {
            color: #2ECC40;
            font-size: 24px;
            font-weight: bold;
            margin-top: 20px;
        }
        .subheader {
            color: #1F618D;
            font-size: 20px;
            font-weight: bold;
            margin-top: 20px;
        }
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #272525;
            color: white;
            text-align: center;
            padding: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown("<h2 class='title'>Hỗ trợ lựa chọn bạn bè phù hợp theo yêu cầu</h2>", unsafe_allow_html=True)

    st.sidebar.title("Chọn cách thức hoạt động")
    data_source = st.sidebar.radio("Chọn nguồn dữ liệu", ["Nhập trực tiếp dữ liệu", "Nhập bằng file Excel"])

    criterias = []
    alternatives = []

    if data_source == "Nhập trực tiếp dữ liệu":
        cri = st.sidebar.text_input("Nhập tiêu chí đã đề ra", "Tuổi, Giới tính, Công việc, MQHMT, Sở thích, Khoảng cách")
        alt = st.sidebar.text_input("Nhập các phương án", "Võ Thị Thúy Nhân, Lý thị quế trân, Trần Quốc Khánh, Nguyễn Tiến Phát, Phạm Lê Hoàng Phúc, Nguyễn Thành Đạt, Phạm Nguyễn Kim Hoa, Huỳnh Tấn Đạt ")
        criterias = [x.strip() for x in cri.split(",")]
        alternatives = [x.strip() for x in alt.split(",")]
    else:
        uploaded_file = st.sidebar.file_uploader("Tải lên file Excel", type=["xlsx"])
        if uploaded_file:
            try:
                df_criterias = pd.read_excel(uploaded_file, sheet_name="Criteria")
                df_alternatives = pd.read_excel(uploaded_file, sheet_name="Alternatives")
                df_matrix = pd.read_excel(uploaded_file, sheet_name="Criteria_Matrix")
                criterias = df_criterias.iloc[:, 0].tolist()
                alternatives = df_alternatives.iloc[:, 0].tolist()
            except Exception as e:
                st.error(f"Lỗi khi đọc file Excel: {e}")

    if criterias and alternatives:
        st.markdown("<h2 class='header'>Thông tin chung</h2>", unsafe_allow_html=True)
        st.write("Số lượng tiêu chí:", len(criterias))
        st.write("Số lượng phương án:", len(alternatives))

        if len(criterias) > 1 and len(alternatives) > 0:
            st.markdown("<h2 class='header'>Nhập ma trận so sánh cặp cho các tiêu chí</h2>", unsafe_allow_html=True)

            if data_source == "Nhập trực tiếp dữ liệu":
                matrix = create_empty_matrix(len(criterias))
                st.write("Ma trận so sánh cặp cho các tiêu chí")
                matrix = input_matrix(matrix, criterias, criterias, "criteria")
            else:
                matrix = df_matrix.values

            df = pd.DataFrame(matrix, index=criterias, columns=criterias)
            st.markdown("<h2 class='header'>AHP</h2>", unsafe_allow_html=True)
            st.table(df)

            weights = calculate_weights(matrix)

            ranked_criteria = rank_criteria(weights)

            st.markdown("<h2 class='header'>Trọng số tiêu chí</h2>", unsafe_allow_html=True)
            weight_df = pd.DataFrame(weights, index=criterias, columns=["Trọng số"])
            st.table(weight_df)

            st.markdown("<h2 class='header'>Xếp hạng</h2>", unsafe_allow_html=True)
            ranked_criteria_df = pd.DataFrame(list(ranked_criteria.items()), columns=["Tiêu chí", "Xếp hạng"])
            ranked_criteria_df['Tiêu chí'] = ranked_criteria_df['Tiêu chí'].apply(lambda x: criterias[x])
            st.table(ranked_criteria_df)
            st.dataframe(ranked_criteria_df.style.background_gradient(cmap='Purples'))


            lambda_max = calculate_lambda_max(matrix, weights)
            CR = calculate_consistency_ratio(matrix, weights) * 100

            st.write("Giá trị lambda_max:", lambda_max)
            st.write("Tỷ số nhất quán CR:", f"{CR:.2f}%")

            if CR < 10:
                st.success("Ma trận nhất quán")
                if st.button("Nhập ma trận so sánh cặp"):
                    st.session_state['show_alternative_matrices'] = True
            else:
                st.error("Ma trận không nhất quán, vui lòng nhập lại cho phù hợp")
                st.session_state['show_alternative_matrices'] = False

            if st.session_state.get('show_alternative_matrices', False):
                alternative_weights = []
                for i, criterion in enumerate(criterias):
                    st.markdown(f"<h2 class='subheader'>Nhập ma trận so sánh cặp cho các phương án theo tiêu chí: {criterion}</h2>", unsafe_allow_html=True)

                    if data_source == "Nhập trực tiếp dữ liệu":
                        alt_matrix = create_empty_matrix(len(alternatives))
                        st.write(f"Ma trận so sánh cặp theo tiêu chí {criterion}")
                        alt_matrix = input_matrix(alt_matrix, alternatives, alternatives, f"alternative_{i}")
                    else:
                        sheet_name = f"Alternative_{i+1}"
                        try:
                            alt_matrix = pd.read_excel(uploaded_file, sheet_name=sheet_name).values
                        except Exception as e:
                            st.error(f"Lỗi khi đọc sheet {sheet_name}: {e}")
                            continue

                    df_alt = pd.DataFrame(alt_matrix, index=alternatives, columns=alternatives)
                    st.write(f"Ma trận so sánh cặp theo tiêu chí {criterion}:")
                    st.table(df_alt)

                    alt_weights = calculate_weights(alt_matrix)
                    alternative_weights.append(alt_weights)

                    st.write(f"Trọng số các phương án theo tiêu chí {criterion}:")
                    alt_weight_df = pd.DataFrame(alt_weights, index=alternatives, columns=["Trọng số"])
                    st.table(alt_weight_df)

                    lambda_max_alt = calculate_lambda_max(alt_matrix, alt_weights)
                    CR_alt = calculate_consistency_ratio(alt_matrix, alt_weights) * 100

                    st.write(f"Giá trị lambda_max cho tiêu chí {criterion}: {lambda_max_alt}")
                    st.write(f"Tỷ số nhất quán CR cho tiêu chí {criterion}: {CR_alt:.2f}%")

                    if CR_alt < 10:
                        st.success(f"Ma trận theo tiêu chí {criterion} nhất quán")
                    else:
                        st.error(f"Ma trận theo tiêu chí {criterion} không nhất quán, vui lòng nhập lại")

                final_scores = np.zeros(len(alternatives))
                for i in range(len(alternatives)):
                    for j in range(len(criterias)):
                        final_scores[i] += alternative_weights[j][i] * weights[j]

                sorted_final_scores = sorted(enumerate(final_scores), key=lambda x: x[1], reverse=True)
                st.markdown("<h2 class='header'>Phương án tốt nhất (từ cao đến thấp):</h2>", unsafe_allow_html=True)
                st.dataframe(ranked_criteria_df.style.background_gradient(cmap='Purples'))

                for index, score in sorted_final_scores:
                    st.write(f"Phương án {alternatives[index]} - Điểm số PA: {score:.2f}%")
        else:
            st.error("Thêm file dữ liệu vào")
    else:
        st.error("Thêm file dữ liệu vào")
    
    # Footer
    footer = """
        <div class="footer">
            <p>© 2024 Hỗ trợ lựa chọn bạn bè phù hợp. All rights reserved.</p>
        </div>
        """
    st.markdown(footer, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
