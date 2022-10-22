# 061

price = ['20180728', 100, 130, 140, 150, 160, 170]

print(price[1:])

# 062

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(nums[::2])

# 063

print(nums[1::2])

# 064

nums = [1, 2, 3, 4, 5]

print(nums[::-1])

# 065

interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

# 066

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest)) # list의 join 함수는 리스트 안의 객체를 문자열로 합칠 수 있게 해 준다. 구분자도 입력 가능

# 067

print("/".join(interest))

# 068

print("\n".join(interest))

# 069

string = "삼성전자/LG전자/Naver"
# string1 = string.replace("/", " ")

# print(string1.split())

print(string.split("/")) # split 함수는 문자열을 구분자 기준으로 나누어 리스트에 담아 출력해주는 함수

# 070

data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data) # sort 함수는 숫자는 오름차순으로, 알파벳은 abcd 순으로 정렬해주는 함수.