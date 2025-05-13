import streamlit as st

# CSS Styles for header and footer
header_style = """
    <style>
    .header {
        position: fixed;
        left: 0;
        top: 0;
        width: 100%;
        padding: 15px;
        background-color: #333;
        color: #FFD700;
        text-align: center;
        font-size: 26px;
        font-family: 'Arial', sans-serif;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        z-index: 1000;
    }
    .header span {
        font-style: italic;
    }
    .content {
        margin-top: 100px;  /* Adjust this value based on header height */
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #333;
        color: white;
        text-align: center;
        padding: 10px;
        z-index: 1000;
    }
    </style>
    <div class="header">
        <span>HỆ THỐNG HỖ TRỢ QUYẾT ĐỊNH</span>
    </div>
    <div class="footer">
        <span>&copy; 2024 Đồ án môn học</span>
    </div>
    <div class="content">
    """



st.markdown("<h1 style='text-align: center; color: #bb55b6;'>ĐỒ ÁN MÔN HỌC</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #2ECC40;'>Hỗ trợ lựa chọn bạn bè phù hợp theo yêu cầu </h2>", unsafe_allow_html=True)
st.markdown(header_style, unsafe_allow_html=True)


st.markdown('<h1 style="color:purple;">I. Lý thuyết</h1>',unsafe_allow_html=True)
st.write("""
AHP (Analytic Hierarchy Process) là một phương pháp ra quyết định đa tiêu chí, được phát triển bởi Thomas L. Saaty vào những năm 1970. AHP giúp người ra quyết định xác định và ưu tiên các yếu tố, tiêu chí liên quan trong một quyết định phức tạp. Phương pháp này đặc biệt hữu ích khi các yếu tố cần xem xét không đồng nhất và khó so sánh trực tiếp.

Dưới đây là các bước cơ bản trong AHP:

1. **Xác định mục tiêu và tiêu chí**: Xác định mục tiêu chính của quyết định và các tiêu chí phụ cần xem xét để đạt được mục tiêu đó.

2. **Xây dựng cấu trúc phân cấp**: Tạo một mô hình phân cấp, bắt đầu từ mục tiêu chính ở đỉnh, sau đó là các tiêu chí, và cuối cùng là các lựa chọn hoặc phương án.

3. **So sánh cặp đôi**: Thực hiện so sánh cặp đôi giữa các tiêu chí, đánh giá mức độ quan trọng của từng tiêu chí so với tiêu chí khác. Thang điểm thường sử dụng từ 1 (quan trọng như nhau) đến 9 (quan trọng hơn nhiều).

4. **Tính toán trọng số**: Sử dụng các so sánh cặp đôi để tính toán trọng số cho từng tiêu chí. Các trọng số này phản ánh mức độ quan trọng tương đối của từng tiêu chí đối với mục tiêu chung.

5. **Đánh giá các lựa chọn**: So sánh các lựa chọn dựa trên từng tiêu chí và tính toán điểm số cho mỗi lựa chọn.

6. **Tổng hợp kết quả**: Kết hợp các điểm số của từng lựa chọn dựa trên trọng số của các tiêu chí để đưa ra quyết định cuối cùng.

AHP có thể được sử dụng trong nhiều lĩnh vực khác nhau như quản lý dự án, quy hoạch đô thị, lựa chọn nhà cung cấp, và nhiều lĩnh vực khác nơi các quyết định phức tạp cần được đưa ra.
""")

st.markdown('<h1 style="color:purple;">II. Mục tiêu đề tài </h1>',unsafe_allow_html=True)
st.write("""
- Biết được cách thức xây dựng một hệ thống AHP bằng python
- Tạo ra một hệ thống giúp kết nối cộng đồng
""")

st.markdown('<h1 style="color:purple;">III. Kết quả </h1>',unsafe_allow_html=True)
st.write("""
- Lựa chọn được một phương án phù hợp trong danh sách những người bạn đã đề ra.
""")

# Closing the content div
st.markdown("</div>", unsafe_allow_html=True)
