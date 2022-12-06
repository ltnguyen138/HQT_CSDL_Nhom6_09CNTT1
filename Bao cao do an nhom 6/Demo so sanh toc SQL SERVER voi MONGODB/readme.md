Demo được thực hiện dựa trên tool Jmeter. Bằng cách kết nối Jmeter với MongoDB và Sql Server sau đó chạy Jmeter với các trường hợp có 100, 500,1000,1500,2000,3000,5000 user cùng thực hiện các thao tác inser, update, truy vấn sau đó thu thập, tổng hợp số liệu tốc độ trung bình cho từng trường hợp và vẽ biểu đồ so sánh

1. Các bước tiến hành

- Tải và giải nén Jmeter
- Tải driver để kết nối SQL Server và MongoDB: groovy-2.4.4, mongo-java-driver-3.8.0, mssql-jdbc-7.0.0.jre8 
- Mở Jmeter
- Click chuột phải Test Plan  thears Thears group

![image](https://user-images.githubusercontent.com/118526250/205847384-a710f00e-4d00-40ab-b14c-a6b5c3c301d1.png)


- Cấu hình số lượng user thực hiện ở Thread group

![image](https://user-images.githubusercontent.com/118526250/205847433-d3e05763-5a0e-4a96-b5e9-52d705763bf4.png)



- Click chuột phải Thread group  add  Config element  JDBC Connection Configuration


![image](https://user-images.githubusercontent.com/118526250/205847459-166d136e-824f-4f08-9a0e-0d94ffc22ba4.png)







- Cấu hình kết nối ở JDBC ở Connection Configuration

![image](https://user-images.githubusercontent.com/118526250/205847492-12a9d75f-9a4e-48b1-8424-20a90a086cd4.png)



- Click chuột phải Thread group  add  Sampler  JDBC Request
- Cấu hình các thao tác, insert,update, truy vấn ở JDBC Request

![image](https://user-images.githubusercontent.com/118526250/205847586-5184e8de-8e27-4b93-ba93-289a71cb4104.png)



- Click chuột phải Thread group  add  Listener  Summary Report
- Chọn Start và xem thống kê ở Summary Report
 
![image](https://user-images.githubusercontent.com/118526250/205847630-91c984a6-6bc1-4ec2-86fd-e7a5c4f57e85.png)

