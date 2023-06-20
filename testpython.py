import streamlit as st
j=[] #Tạo một danh sách rỗng để lưu kết quả
for i in range(2000, 3201): #Duyệt qua tất cả các số trong đoạn từ 2000 đến 3200
    if (i%7==0) and (i%5!=0): #Kiểm tra xem số i có chia hết cho 7 và không phải là bội số của 5 không
        j.append(str(i)) #Nếu đúng, thì thêm số i vào danh sách result
st.write(','.join(j)) #In ra màn hình danh sách result, các phần tử cách nhau bằng dấu phẩy
print('test python')
st.write('tetst Python')
print('khong test duoc')
st.write('test bang Write')
menu=["test1","test 2","test 3","test 4"]
choice = st.sidebar.selectbox('Danh mục tính năng', menu)
import datetime

print("Mời bạn vui lòng nhập ngày tháng năm sinh để tính tuổi")
birth_day = int(input("Ngày sinh:"))
birth_month = int(input("Tháng sinh:"))
birth_year = int(input("Năm sinh:"))

current_year = datetime.date.today().year
current_month = datetime.date.today().month
current_day = datetime.date.today().day

age_year = current_year - birth_year
age_month = abs(current_month-birth_month)
age_day = abs(current_day-birth_day)

print("### Tuổi của bạn chính xác là:### \n", age_year, " tuổi ", age_month, " tháng và ", age_day, " ngày")
