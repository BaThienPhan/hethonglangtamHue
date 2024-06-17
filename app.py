import streamlit as st

# Tiêu đề trang
st.title('Giới thiệu các lăng tẩm ở Huế')

# Mục lục các lăng tẩm
st.sidebar.title('Danh sách các lăng tẩm')
tomb_list = [
    "Lăng Gia Long",
    "Lăng Minh Mạng",
    "Lăng Thiệu Trị",
    "Lăng Tự Đức",
    "Lăng Dục Đức",
    "Lăng Đồng Khánh",
    "Lăng Khải Định"
]
selected_tomb = st.sidebar.radio("", tomb_list)

# Thông tin chi tiết về các lăng
if selected_tomb == "Lăng Gia Long":
    st.header("Lăng Gia Long")
    # st.image("https://link_to_image_of_lăng_gia_long", caption="Lăng Gia Long")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Lăng tẩm ở Huế/lang-gia-long-1.png",
                 caption="", use_column_width=True)
    st.write("""
    Tầng Lớp Nghĩa Trang Hoàng Gia
    """)
    st.write("""
    Lăng Gia Long là tầng lớp nghĩa trang hoàng gia, được xây dựng để an táng Vua Gia Long - vị vua đầu tiên của triều Nguyễn. 
    Lăng mang phong cách kiến trúc độc đáo, với những đặc trưng riêng của văn hóa Huế.
    """)
    with col2:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Lăng tẩm ở Huế/lang-gia-long-2.png",
                 caption="", use_column_width=True)
    st.write("""
    Kiến Trúc Tinh Xảo
    """)
    st.write("""
    Lăng Gia Long được thiết kế với sự pha trộn giữa kiến trúc cung đình và ngũ hành, 
    tạo nên một công trình hoàng gia mang phong cách riêng biệt. Mỗi chi tiết trong lăng đều được chạm trổ tỉ mỉ, thể
    hiện sự tinh xảo của nghệ nhân thời bấy giờ. 
    """)
    with col3:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Lăng tẩm ở Huế/lang-gia-long-3.png",
                 caption="", use_column_width=True)
    st.write("""
    Cảnh Quan Tĩnh Lặng
    """)
    st.write("""
    Nằm bên dòng Hương Giang thơ mộng, lăng 
    Gia Long được bao quanh bởi cảnh quan thiên nhiên tĩnh lặng, tạo cảm giác an yên và trang nghiêm cho
    du khách khi đến tham quan. 
    """)

elif selected_tomb == "Lăng Minh Mạng":
    st.header("Lăng Minh Mạng")
    # st.image("https://link_to_image_of_lăng_minh_mạng", caption="Lăng Minh Mạng")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Lăng tẩm ở Huế/lang-minh-mang-1.png",
                 caption="", use_column_width=True)
    st.write("""
    Nội Cung Lăng Minh Mạng
    """)
    st.write("""
    Nội cung của lăng Minh Mạng được xây dựng với kiến trúc tráng lệ, sử dụng những vật liệu quý hiếm như đá và gỗ tếch. 
    Các trang trí phức tạp và tinh xảo tôn vinh sự uy nghi của vua Minh Mạng
    """)
    with col2:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Lăng tẩm ở Huế/lang-minh-mang-2.png",
                 caption="", use_column_width=True)
    st.write("""
    Cổng Tam Quan Lăng Minh Mạng
    """)
    st.write("""
    Cổng tam quan lăng Minh Mạng là một kiệt tác kiến trúc, với các họa tiết và trang trí đậm chất Huế. 
    Nó đánh dấu sự uy nghi và quyền lực của vị vua đã an nghỉ tại đây.
    """)
    with col3:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Lăng tẩm ở Huế/lang-minh-mang-3.png",
                 caption="", use_column_width=True)
    st.write("""
    Cảnh Quan Xung Quanh Lăng
    """)
    st.write("""
    Lăng Minh Mạng nằm giữa những cây cổ thụ và rừng xanh mát, tạo nên một bối cảnh tĩnh lặng và linh thiêng. 
    Đây là nơi hòa quyện giữa thiên nhiên và di sản văn hóa Huế.
    """)

elif selected_tomb == "Lăng Thiệu Trị":
    st.header("Lăng Thiệu Trị")
    # st.image("https://link_to_image_of_lăng_thiệu_trị", caption="Lăng Thiệu Trị")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Lăng tẩm ở Huế/lang-trieu-tri-1.png",
                 caption="", use_column_width=True)
    st.write("""
    Kiến trúc độc đáo
    """)
    st.write("""
    Lăng Thiệu Trị được xây dựng theo phong cách kiến trúc Á Đông với những họa tiết tinh xảo, kết hợp hài hòa giữa truyền thống và hiện đại. 
    Nơi đây là minh chứng cho sự phát triển của nghệ thuật kiến trúc thời Nguyễn.
    """)
    with col2:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Lăng tẩm ở Huế/lang-trieu-tri-2.png",
                 caption="", use_column_width=True)
    st.write("""
    Cổng Tam Quan
    """)
    st.write("""
    Cổng Tam Quan là điểm nhấn ấn tượng của Lăng Thiệu Trị. 
    Được xây dựng theo kiến trúc cổ, cổng là biểu tượng cho sự uy nghi và tôn nghiêm của lăng mộ.
    """)
    with col3:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Lăng tẩm ở Huế/lang-trieu-tri-3.png",
                 caption="", use_column_width=True)
    st.write("""
    Khu mộ
    """)
    st.write("""
    Khu mộ của Thiệu Trị được thiết kế theo hình chữ "nhất", thể hiện sự tôn kính và tưởng nhớ vị vua. 
    Nơi đây được bao phủ bởi những cây cổ thụ, mang đến một không gian yên tĩnh và thanh bình.
    """)

elif selected_tomb == "Lăng Tự Đức":
    st.header("Lăng Tự Đức")
    # st.image("https://link_to_image_of_lăng_tự_đức", caption="Lăng Tự Đức")
    st.write("""
    Lăng Tự Đức (Khiêm Lăng) là nơi an nghỉ của vua Tự Đức, vị vua thứ tư của triều Nguyễn. Lăng được xây dựng từ năm 1864 đến 1867.
    Lăng có kiến trúc phong phú và đa dạng, nằm trong một khuôn viên rộng lớn với hồ nước và cây xanh, tạo nên một không gian yên bình và thơ mộng.
    """)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Lăng tẩm ở Huế/lang-tu-duc-1.png",
                 caption="", use_column_width=True)
    st.write("""
    Vẻ Đẹp Kiến Trúc
    """)
    st.write("""
    Lăng Tự Đức được xây dựng với lối kiến trúc cung đình độc đáo, kết hợp độc đáo phong cách Việt và 
    phong cách Trung Quốc, tạo nên vẻ đẹp tráng lệ và tinh tế.
    """)
    with col2:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Lăng tẩm ở Huế/lang-tu-duc-2.png",
                 caption="", use_column_width=True)
    st.write("""
    Cổng Tam Quan Ấn Tượng
    """)
    st.write("""
    Cổng tam quan của lăng Tự Đức là một kiệt tác kiến trúc với bốn cột đá khổng lồ, 
    khắc họa tinh tế các hoa văn truyền thống, tạo ấn tượng mạnh mẽ cho du khách.
    """)
    with col3:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Lăng tẩm ở Huế/lang-tu-duc-3.png",
                 caption="", use_column_width=True)
    st.write("""
    Hồ Tiên Như Huyền Bí
    """)
    st.write("""
    Hồ Tiên Như nằm trong khuôn viên lăng Tự Đức, với sự phối hợp của nước, 
    núi và cây cối, tạo nên một khung cảnh yên bình và huyền ảo.
    """)

elif selected_tomb == "Lăng Dục Đức":
    st.header("Lăng Dục Đức")
    # st.image("https://link_to_image_of_lăng_dục_đức", caption="Lăng Dục Đức")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Lăng tẩm ở Huế/lang-duc-duc-1.png",
                 caption="", use_column_width=True)
    st.write("""
    Vẻ Đẹp Kiến Trúc
    """)
    st.write("""
    Lăng Dục Đức là một trong những lăng tẩm quan trọng của triều Nguyễn, được xây dựng vào thời kỳ 
    vua Dục Đức trị vì từ năm 1883 đến 1884. Lăng tọa lạc tại núi Thiên An, Huế với kiến trúc độc đáo và tinh xảo.
    """)
    with col2:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Lăng tẩm ở Huế/lang-duc-duc-2.png",
                 caption="", use_column_width=True)
    st.write("""
    Cổng tam quan
    """)
    st.write("""
    Cổng tam quan là một trong những kiến trúc nổi bật của Lăng Dục Đức, 
    được xây dựng theo phong cách kiến trúc truyền thống với những hoa văn tinh xảo và sắc màu trang nhã
    """)
    with col3:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Lăng tẩm ở Huế/lang-duc-duc-3.png",
                 caption="", use_column_width=True)
    st.write("""
    Hồ An Lạc
    """)
    st.write("""
    Nằm bên trong lăng tẩm, hồ An Lạc là một điểm nhấn đẹp mắt, tạo không gian yên bình và thư giãn cho du khách tham quan.
    """)

elif selected_tomb == "Lăng Đồng Khánh":
    st.header("Lăng Đồng Khánh")
    # st.image("https://link_to_image_of_lăng_đồng_khánh", caption="Lăng Đồng Khánh")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Lăng tẩm ở Huế/lang-dong-khanh-1.png",
                 caption="", use_column_width=True)
    st.write("""
    """)
    st.write("""
    Lăng Đồng Khánh là một trong những lăng tẩm hoành tráng của triều Nguyễn, được xây dựng vào thời vua Đồng Khánh (1885-1889). 
    Ngự lăng này nằm yên lặng giữa rừng cây xanh mát, toát lên vẻ thiêng liêng và bình yên.
    """)
    with col2:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Lăng tẩm ở Huế/lang-dong-khanh-2.png",
                 caption="", use_column_width=True)
    st.write("""
    Kiến Trúc Độc Đáo
    """)
    st.write("""
    Lăng Đồng Khánh sở hữu kiến trúc cổ kính, với hệ thống cung đường, lầu đài, tượng đá và vườn hoa đẹp mắt. 
    Các họa tiết cùng hệ thống cửa vòm và mái ngói cong độc đáo tạo nên vẻ đẹp hài hòa và khí vị riêng.
    """)
    with col3:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Lăng tẩm ở Huế/lang-dong-khanh-3.png",
                 caption="", use_column_width=True)
    st.write("""
    Không Gian Linh Thiêng
    """)
    st.write("""
    Bước vào lăng Đồng Khánh, du khách sẽ cảm nhận được một không gian trang nghiêm, cổ kính và sâu lắng. 
    Những đình đài, lầu các cùng các tích hùng vĩ của triều đại Nguyễn khiến nơi đây trở thành một địa danh văn hóa quan trọng tại Huế.
    """)

elif selected_tomb == "Lăng Khải Định":
    st.header("Lăng Khải Định")
    # st.image("https://link_to_image_of_lăng_khải_định", caption="Lăng Khải Định")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Lăng tẩm ở Huế/lang-khai-dinh-1.png",
                 caption="", use_column_width=True)
    st.write("""
    Vẻ đẹp kiến trúc lăng Khải Định
    """)
    st.write("""
    Lăng Khải Định được xem là một trong những kiệt tác kiến trúc đẹp nhất của vương triều nhà Nguyễn. 
    Với sự pha trộn tinh tế giữa phong cách Đông và Tây, lăng Khải Định mang vẻ đẹp độc đáo, đậm chất hoàng gia.
    """)
    with col2:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Lăng tẩm ở Huế/lang-khai-dinh-2.png",
                 caption="", use_column_width=True)
    st.write("""
    Nội thất lăng Khải Định
    """)
    st.write("""
    Bên trong lăng Khải Định, du khách sẽ được chiêm ngưỡng những tác phẩm 
    nghệ thuật tuyệt vời, từ mái ngói, cột chống đến ván gỗ, tất cả đều được chạm trổ tinh xảo.
    """)
    with col3:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Lăng tẩm ở Huế/lang-khai-dinh-3.png",
                 caption="", use_column_width=True)
    st.write("""
    Vị trí lăng Khải Định
    """)
    st.write("""
    Lăng Khải Định nằm trên núi Châu Ê, thuộc địa phận phường Vĩ Dạ, thành phố Huế. 
    Với vị trí đắc địa này, du khách có thể chiêm ngưỡng toàn cảnh thành phố Huế từ trên cao.
    """)
elif selected_tomb == "Kết luận":
    st.header("Tầm quan trọng của hệ thống lăng tẩm đối với di sản văn hóa Huế")
    st.write("""
    Hệ thống lăng tẩm ở Huế là một phần không thể thiếu của di sản văn hóa Việt Nam. 
    Nó phản ánh sự kết hợp tinh tế giữa kiến trúc, nghệ thuật và tâm linh trong văn hóa Huế.
    """)
    st.write("""
    Các lăng tẩm không chỉ là nơi an nghỉ của các vị vua, mà còn là biểu tượng của sự 
    tôn nghiêm, quyền lực và sự kế thừa triều đại. Chúng đóng vai trò quan trọng trong việc bảo tồn và truyền thống quý giá của Huế.
    """)
