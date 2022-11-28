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