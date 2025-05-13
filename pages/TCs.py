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

st.markdown(header_style, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #bb55b6;'>GIỚI THIỆU CÁC TIÊU CHÍ</h1>", unsafe_allow_html=True)

# Danh sách tiêu chí với mô tả ngắn gọn
criterias = [
    {"name": "Tuổi", "description": "Tuổi tác có thể ảnh hưởng đến sự phù hợp của một người bạn trong các tình huống khác nhau."},
    {"name": "Giới tính", "description": "Giới tính có thể là một yếu tố quan trọng trong việc xác định sự phù hợp trong một số trường hợp nhất định."},
    {"name": "Công việc", "description": "Công việc và sự nghiệp của một người có thể ảnh hưởng đến khả năng kết nối và hợp tác."},
    {"name": "Mối quan muốn tìm", "description": "Đây là yêu cầu được đề ra của người sử dụng chương trình"},
    {"name": "Sở thích", "description": "Sở thích chung có thể tạo ra sự kết nối và sự hiểu biết tốt hơn giữa các cá nhân."},
    {"name": "Khoảng cách", "description": "Khoảng cách địa lý có thể ảnh hưởng đến khả năng gặp gỡ và duy trì mối quan hệ."}
]

for criteria in criterias:
    st.markdown(f"### {criteria['name']}", unsafe_allow_html=True)
    st.write(criteria["description"])

# Closing the content div
st.markdown("</div>", unsafe_allow_html=True)
