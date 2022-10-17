# 041

tiker = "btc_krw"
tiker1 = tiker.upper()

print(tiker1)

# 042

tiker2 = tiker1.lower()
print(tiker2)

# 043

string = 'hello'
string1 = string.capitalize()

print(string1) # capitalize 함수는 문자열의 첫 문자를 대문자로 바꾸어 준다.

# 044

file_name = "보고서.xlsx"
print(file_name.endswith('xlsx')) # endwith 메서드는 문자열이 특정 문자로 끝나는 지 boolean 형태로 변환하여 준다.

# 045

print(file_name.endswith('xlsx' or 'xls'))

# 046

file_name = "2020_보고서.xlsx"
print(file_name.startswith('2020'))

# 047

a = "hello world"
# print(a, sep = " ")

a.split()
print(a)

# 048

ticker = "btc_krw"

ticker = ticker.split('_')
print(ticker)

# 049

date = "2020-05-01"
date1 = date.split('-')

print(date1)

# 050 

data = "039490      "
data1 = data.rstrip()
print(data1) # rstrip() 메서드를 사용하면 오른쪽 공백이 제거된 새로운 문자열 객체가 반환됩니다. 그 값을 data라는 변수가 새로 바인딩합니다. 기존의 공백이 포함된 문자열은 메모리에서 자동으로 삭제됩니다.

