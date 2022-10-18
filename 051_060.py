# 051

movie_rake = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rake)

#052

movie_rake.append("배트맨")
print(movie_rake)

# 053

movie_rake.insert(1, "슈퍼맨")
print(movie_rake) # insert 함수를 사용하면 리스트에서 특정 순서에 원하는 값을 추가할 수 있다.

# 054

# movie_rake.remove("럭키")
# print(movie_rake)

movie_rake = ["닥터 스트레인지", "슈퍼맨", "스플릿", "럭키", "배트맨"]
del movie_rake[3]
print(movie_rake) # del을 사용하면 index로 값을 삭제할 수 있다.


# 055 

del movie_rake[1:3]
print(movie_rake)

# 056

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs) # 리스트는 덧셈연산 가능

# 057

nums = [1, 2, 3, 4, 5 ,6, 7]
print(min(nums))
print(max(nums))

# 058

nums = [1, 2, 3, 4, 5]
sumis = sum(nums)
print(sumis)

# 059

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]

print(len(cook))

# 060

nums = [1, 2, 3, 4, 5]

result = sum(nums)
print(f'average : {result / len(nums)}')