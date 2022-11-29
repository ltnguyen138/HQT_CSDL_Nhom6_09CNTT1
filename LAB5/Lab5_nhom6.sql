--Cau 1:
-- In ra dong 'Xin chào' +@ten với @ten là tham số đầu vào là tên TIếng Việt có dấu của
--bạn. Gợi ý:
--o sử dụng UniKey để gõ Tiếng Việt ♦
--o chuỗi unicode phải bắt đầu bởi N (vd: N’Tiếng Việt’) ♦
--o dùng hàm cast (<biểuThức> as <kiểu>) để đổi thành kiểu <kiểu> của<biểuThức>.1
go
CREATE PROCEDURE XINCHAO @ten nvarchar(50)
as
	begin
	print 'Xin Chào: '+@ten
	end
go
go
exec XINCHAO N'Tiếng Việt'
go

--Nhập vào 2 số @s1,@s2. In ra câu ‘Tổng là : @tg’ với @tg=@s1+@s2.
go
CREATE PROCEDURE TINHTONG @s1 int,@s2 int
as
	begin
	declare @tg int
	set @tg=@s1+@s2
	print N'Tổng là: '+ cast(@tg as varchar(12))
	end
go
go
exec TINHTONG 4,6
go

--Nhập vào số nguyên @n. In ra tổng các số chẵn từ 1 đến @n.
go
CREATE PROCEDURE Tong_cac_so_chan @n int
as
	begin

	declare @tg int=0,@i int =2
	while @i<=@n
		begin
		set @tg=@tg+@i
		set @i=@i+2
		end
	print N'Tổng số chan từ 1 đến '+cast(@n as varchar(20))+N' la: '+cast(@tg as varchar(20)) 
	end
go
go
exec Tong_cac_so_chan 5
go

--➢ Nhập vào 2 số. In ra ước chung lớn nhất của chúng theo gợi ý dưới đây:
go
CREATE PROCEDURE Tim_uoc_chung_lon_nhat @a int,@b int
as
	begin

	while(@a!=@b)
		begin
		if @a>@b
			set @a=@a-@b
		else
			set @b=@b-@a
		end
	
	print N'Ước chung lớn nhất: '+cast(@a as varchar(20)) 
	end
go
go
exec Tim_uoc_chung_lon_nhat 40,20
go

--Câu 2:
-- ➢ Nhập vào @Manv, xuất thông tin các nhân viên theo @Manv.
go
CREATE PROCEDURE BAI2_1 @MaNV varchar(3)
as
	begin
	SELECT * FROM NHANVIEN WHERE MANV=@MaNV
	end
go
go
exec BAI2_1'004'
go

--➢ Nhập vào @MaDa (mã đề án), cho biết số lượng nhân viên tham gia đề án đó
go
CREATE PROCEDURE BAI2_2 @MaDA varchar(3)
as
	begin
	select count(MANV) as 'so luong', MADA from NHANVIEN
	INNER JOIN PHONGBAN ON NHANVIEN.PHG=PHONGBAN.MAPHG
	INNER JOIN DEAN ON DEAN.PHONG=PHONGBAN.MAPHG
	WHERE MADA=@MaDA
	group by MADA
	end
go
go
exec BAI2_2 10
go	

--➢ Nhập vào @MaDa và @Ddiem_DA (địa điểm đề án), cho biết số lượng nhân viên tham
--gia đề án có mã đề án là @MaDa và địa điểm đề án là @Ddiem_DA

go
CREATE PROCEDURE BAI2_3 @MaDA varchar(3),@Ddiem_DA nvarchar(50)
as
	begin
	select count(MANV) as 'so luong', MADA,DDIEM_DA from NHANVIEN
	INNER JOIN PHONGBAN ON NHANVIEN.PHG=PHONGBAN.MAPHG
	INNER JOIN DEAN ON DEAN.PHONG=PHONGBAN.MAPHG
	WHERE MADA=@MaDA and DDIEM_DA=@Ddiem_DA
	group by MADA,DDIEM_DA
	end
go
go
exec BAI2_3 10,N'Hà Nội'
go	

--➢ Nhập vào @Trphg (mã trưởng phòng), xuất thông tin các nhân viên có trưởng phòng là
--@Trphg và các nhân viên này không có thân nhân.
go
CREATE PROCEDURE BAI2_4 @Trphg varchar(5)
as
	begin
	select HONV, TENNV,TENPHG,NHANVIEN.MANV,THANNHAN.*
	FROM NHANVIEN
	INNER JOIN PHONGBAN ON PHONGBAN.MAPHG=NHANVIEN.PHG
	LEFT OUTER JOIN THANNHAN ON THANNHAN.MA_NVIEN=NHANVIEN.MANV
	WHERE THANNHAN.MA_NVIEN IS NULL AND TRPHG=@Trphg

	end
go
go
exec BAI2_4 '006'
go	


--➢ Nhập vào @Manv và @Mapb, kiểm tra nhân viên có mã @Manv có thuộc phòng ban có
--mã @Mapb hay không
go
CREATE PROCEDURE BAI2_5 @Manv varchar(3),@Mapb int
as
	begin
	if exists (select * from NHANVIEN where MANV=@Manv AND PHG=@Mapb)
	print 'Nhan vien ' +@Manv+ ' co trong phong ban'
	else
	print 'Nhan vien '+@Manv+ ' khong co trong phong ban'
	end
go
go
exec BAI2_5 '006',1 
go	

--BAI 3
go
create proc ThemPhongBanMoi
	@TenPhg nvarchar(20),@MaPhg int,@TrPhg nvarchar(10), @Ng_NhanChuc date
as
begin
	if exists(select * from PHONGBAN where MAPHG = @MAPHG)
	begin
		print('Mã phòng ban đã tồn tại');
		return;
	end

	Insert into [dbo].[PHONGBAN]
		([TENPHG],[MAPHG],[TRPHG],[NG_NHANCHUC])
	Values
		(@TenPhg,@MaPhg,@TenPhg,@Ng_NhanChuc);
end
go
go
exec ThemPhongBanMoi 'IT','11','005','2022-11-29'
go
-------
go
create proc sp_CapNhatPhongBan
	@OldTenPHG nvarchar(15),
	@TenPHG nvarchar(15),
	@MaPHG int,
	@TRPHG nvarchar(10),
	@NG_NHANCHUC date
as
begin
	UPDATE [dbo].[PHONGBAN]
	SET 
		[TENPHG] =@TENPHG,
		[MAPHG] = @MAPHG,
		[TRPHG] = @TRPHG,
		[NG_NHANCHUC]=@NG_NHANCHUC
		where TENPHG = @OldTenPHG;
end
go
go
exec [dbo].[sp_CapNhatPhongBan] 'CNTT','IT','10','005','1-1-2020'
go
---------------------------------------------
go
create PROCEDURE sp_insertNV @Ho nvarchar(15),@tenNV nvarchar(15),@MaNV nvarchar(9),@NgaySinh datetime,@diachi nvarchar(30),@phai nvarchar(3),@luong float,@Ma_NQL nvarchar(9),@PHG int
as
begin
	if not exists(select * from PHONGBAN where TENPHG like 'IT')
	begin
		print 'NHAN VIEN phai la phong IT'
	return
end
if @luong < 25000
set @Ma_NQL='009'
else
begin
set @Ma_NQL = '005'
end
declare @age int = datediff(YEAR,@ngaySinh,getDate())
if(@phai like 'nam' and @age > 65 and @age <18)
begin
print 'nam phai tu 18 - 65 '
return 
end
else if(@phai like N'Nữ' and @age > 60 and @age < 18)
begin
print 'nu phai tu 18-60'
return 
end
insert into NHANVIEN(HONV,TENLOT,TENNV,MANV,NGSINH,DCHI,PHAI,LUONG,MA_NQL,PHG)
values(@Ho,@tenNV,@MaNV,@NgaySinh,@diachi,@phai,@luong,@Ma_NQL,@PHG)
end
go