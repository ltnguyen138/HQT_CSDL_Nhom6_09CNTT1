I. Các bước thực hiện

Các bước thực hiện so sánh sql server và mongoDB bằng Jmeter:

- Tải file apache-jmeter-5.5 và giải nén
- Mở ứng dụng Apache jmeter , chọn Open  Mở file Test PlanMSSQL.jmx(Khi thực hiện test SQL Server) hoặc Test PlanMongo.jmx(Khi thực hiện test MongoDB)

![image](https://user-images.githubusercontent.com/118526250/205496633-31c7db8b-d50d-4387-b7d2-1c7561fc192e.png)


- Chọn số user thực hiện test ở phần theard group

![image](https://user-images.githubusercontent.com/118526250/205496646-80e5fbf7-6c1b-48a8-811e-4ec6c03d3d5b.png)


- Cấu hình kết nối ở JDBC Connection Configuration, Các thao tác truy vấn, update ở JDBC Request

![image](https://user-images.githubusercontent.com/118526250/205496651-de9061aa-9da6-4256-8dd5-3be845ee2e11.png)
![image](https://user-images.githubusercontent.com/118526250/205496658-8e2c4db3-68ef-4c72-b2e3-9e7694594120.png)


- Chọn Start và xem thống kê ở Summary Report

![image](https://user-images.githubusercontent.com/118526250/205496668-614db664-3c9a-441d-aa48-e33c98773a57.png)
  

