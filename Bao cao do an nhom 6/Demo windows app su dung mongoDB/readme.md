DEMO TẠO ỨNG DỤNG WINDOWS  ĐƠN GIẢN VỚI CSDL MONGODB Atlas

I. Giới thiệu MongoDB Atlas

Một trong những điểm nổi của cơ sở dữ  liệu NoSQL là tùy thuộc vào yêu cầu và chiến lược kinh doanh, nhà cung cấp cơ sơ dữ liệu có thể cung cấp dịch vụ đám mây kèm với bất kì loại cơ sở dữ liệu NOSQL nào.
MongoDB Atlas là dịch vụ cơ sở dữ liệu trên đám mây của cơ sở dữ liệu MongoDB mang đến nhiều lợi ích nổi bật như:
- Năng suất của nhà phát triển: MongoDB Atlas là một cơ sở dữ liệu NoSQL sử dụng mô hình dữ liệu tài liệu dựa trên JSON. Các tài liệu MongoDB ánh xạ một cách tự nhiên đến một mô hình lập trình hướng đối tượng, điều này làm cho nó trở nên trực quan và dễ làm việc với việc sử dụng bất kỳ ngôn ngữ hướng đối tượng nào.
- Khả năng mở rộng: MongoDB Atlas cho phép triển khai các ứng dụng có kích thước phù hợp; nó mở rộng quy mô lên hoặc xuống ngay lập tức và theo yêu cầu, mà không làm ứng dụng ngừng hoạt động.
- Tính khả dụng và thời gian hoạt động: Chạy một ứng dụng trong đám mây công cộng thường cung cấp tính khả dụng tốt hơn ngay từ đầu so với môi trường tại chỗ khi MongoDB Atlas triển khai mọi cụm cơ sở dữ liệu dưới dạng một tập hợp bản sao tự phục hồi khi bị lỗi

II. Demo
Nhận thấy những lợi ích của cơ sở dữ liệu NoSQL- MongoDB Atlas nhóm 6 đã thực hiện demo ứng dụng windows sử dụng cở sở dữ liệu này.
a. Công nghệ sử dụng:
	- CSDL: MongoDB
	- Ngôn ngữ lập trình: Python
- MongoDBDriver: Pymongo
b. Mô hình dữ liệu

![image](https://user-images.githubusercontent.com/118526250/205499300-85968405-cbf6-4e73-a8b3-2729a6d9f655.png)






c. Kết quả Demo

- Ứng dụng thống kê các đánh giá của khách hàng đối với các nhà hàng
- Chức năng:
+ Hiển thị thông tin nhà hàng: id, tên nhà hàng, món ăn, địa chỉ(thành phố, đường,..), tổng các đánh giá loại A, B, C , điểm trung bình

![image](https://user-images.githubusercontent.com/118526250/205499310-51d81bf5-39aa-4798-8c0e-5ec4d236b2b1.png)


+ Thêm, xóa các nhà hàng, sửa thông tin nhà hàng, hiển thị chi tiết đánh giá
VD: Cập nhật: “nha hang 1” thanh “RESTAURANT1”, thành phố từ “ho” thành “Ho Chi Minh”

![image](https://user-images.githubusercontent.com/118526250/205499339-15454a55-5351-4fe8-97da-3ec4a4ae22fb.png)


VD: Xem chi tiết các đánh giá nhà hàng “May May Kitchen”

![image](https://user-images.githubusercontent.com/118526250/205499353-5daced26-d439-4e87-8138-3d306fc72695.png)


+ Tìm kiếm theo id nhà hàng, tên nhà hàng, món ăn, thành phố
VD: Tìm kiếm nhà hàng trong tên có chữ foods


![image](https://user-images.githubusercontent.com/118526250/205499368-6d91fa62-0c66-46d8-b468-c50fe6685996.png)




+Thực hiện một số truy vấn như:  Thống kê các nhà hàng trong toàn CSDL hay từng thành phố theo các tiêu chí như: Có nhiều đánh giá A nhất, nhiều đánh giá C nhất, điểm trung bình cao nhất,…

VD: Thống kê top 6 nhà hàng có điểm trung bình cao nhất thành phố “Bronx”

![image](https://user-images.githubusercontent.com/118526250/205499378-8566733f-965e-4dd3-a974-b5b4f8ecccc0.png)


+ Hiển thị các thống kê các nhà hàng trong toàn CSDL hay từng thành phố theo các tiêu chí như: Có nhiều đánh giá A nhất, nhiều đánh giá C nhất, điểm trung bình cao nhất dưới dạng biểu đồ
- VD: Hiển thị thống kê top 6 nhà hàng có điểm trung bình cao nhất thành phố “Bronx” dưới dạng biểu đồ
![image](https://user-images.githubusercontent.com/118526250/205848086-bf8d5ccb-7725-474d-92f2-dda88fcb0f21.png)




