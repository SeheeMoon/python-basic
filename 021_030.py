# 021

letters = 'python'
print(letters[0], letters[2])

# 022

license_plate = "24가 2210"
print(license_plate[-4:])

# 023

string = "홀짝홀짝홀짝"
print(string[::2]) # 맨 마지막 오프셋은 (숫자) 갯수마다 하나씩 출력

# 024

string = "PYTHON"

print(string[::-1]) # 맨 마지막 오프셋에 음수를 넣으면 거꾸로 뒤집어 출력된다.

# 025

phone_number = "010-1111-2222"

print(phone_number.replace("-", " "))

# 026

phone_number = "010-1111-2222"

print(phone_number.replace("-", ""))

# 027

url = "http://sharebook.naver.com"

domain = url.replace("http://sharebook.", "")
print(domain)

url_split = url.split(".")
print(url_split[-1])

# 028

# lang = "python"
# lang[0] = 'P'
# print(lang) # 문자열은 수정할 수 없다.

# 029

string = 'abcdfe2a354a32a'
string1 = string.replace('a', 'A')
print(string1)

# 030

string = 'abcd'
string.replace('b', 'B')
print(string) # abcd가 그대로 출력됩니다. 왜냐하면 문자열은 변경할 수 없는 자료형이기 때문입니다. replace 메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해줍니다.
# 즉 replace함수를 사용한 문자열을 새로운 변수로 지정해주어야 함.