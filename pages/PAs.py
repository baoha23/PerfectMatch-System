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

st.markdown("<h1 style='text-align: center; color: #bb55b6;'>GIỚI THIỆU CÁC PHƯƠNG ÁN</h1>", unsafe_allow_html=True)

# Danh sách bạn bè với mô tả ngắn gọn
friends = [
    {"name": "1. Võ Thị Thúy Nhân", "description": "Thúy Nhân là một người bạn thân thiện và luôn sẵn sàng giúp đỡ."},
    {"name": "2. Lý Thị Quế Trân", "description": "Quế Trân yêu thích nghệ thuật và có khiếu vẽ tranh rất đẹp."},
    {"name": "3. Trần Quốc Khánh", "description": "Quốc Khánh là một người đam mê công nghệ và luôn cập nhật những xu hướng mới."},
    {"name": "4. Nguyễn Tiến Phát", "description": "Tiến Phát là một người vui vẻ và luôn mang lại tiếng cười cho mọi người."},
    {"name": "5. Phạm Lê Hoàng Phúc", "description": "Hoàng Phúc có tính cách trầm lắng nhưng rất thông minh và sáng tạo."},
    {"name": "6. Nguyễn Thành Đạt", "description": "Thành Đạt là một người bạn trung thành và rất chân thành."},
    {"name": "7. Phạm Nguyễn Kim Hoa", "description": "Kim Hoa thích thể thao và có lối sống lành mạnh."},
    {"name": "8. Huỳnh Tấn Đạt", "description": "Tấn Đạt rất đam mê âm nhạc và chơi guitar rất hay."}
]

for friend in friends:
    st.markdown(f"### {friend['name']}", unsafe_allow_html=True)
    st.write(friend["description"])

# Closing the content div
st.markdown("</div>", unsafe_allow_html=True)
