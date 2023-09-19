# 입력한 사용자간의 유클리드 점수를 계산하는 함수
# 사용자가 데이터셋에 없으면 에러
import numpy as np
import json

def euclidean_score(dataset, user1,user2):
  if user1 not in dataset:
    raise TypeError(f"Cannot find {user1} in the dataset")
  if user2 not in dataset:
    raise TypeError(f"Cannot find {user2} in the dataset")    
  # 두 사용자가 평가한 영화를 추적하는 변수를 정의
  # 사용자1과 사용자2가 평가한 영화
  common_movies = {}
  # 두 사용자가 평가한 영화를 추출
  for item in dataset[user1]:
    if item in dataset[user2]:
      common_movies[item] = 1
  # 두 사용자간의 공통된 영화가 없으면 유사성 점수는 0
  if len(common_movies) ==0:
    return 0
  # 두 평점간의 제곱차이를 계사니하고, 이를 사용해 유클리드 점수를 계산
  squared_diff = []
  for item in dataset[user1]:
    if item in dataset[user2]:
      squared_diff.append(np.square(dataset[user1][item] - dataset[user2][item]))
  return 1 / (1+ np.sqrt(np.sum(squared_diff)))  # 1 / (1+sqrt(평점  차이 제곱의 합))

# 피어슨 상관관계 점수 계산
def pearson_score(dataset,user1,user2):
  if user1 not in dataset:
    raise TypeError(f"Cannot find {user1} in the dataset")
  if user2 not in dataset:
    raise TypeError(f"Cannot find {user2} in the dataset")    
  # 사용자1과 사용자2가 평가한 영화
  common_movies = {}
  # 두 사용자가 평가한 영화를 추출
  for item in dataset[user1]:
    if item in dataset[user2]:
      common_movies[item] = 1
  # 두 사용자간의 공통된 영화가 없으면 상관관계를 못구함
  if len(common_movies) ==0:
    return 0
  
  # 두 사용자가 모두 평가한 모든 영화의 평점의 합을 계산
  user1_sum = np.sum(  dataset[user1][item] for item in common_movies  )
  user2_sum = np.sum(  dataset[user2][item] for item in common_movies  )
  
  # 두 사용자가 모두 평가한 모든 영화의 평점제곱의 합을 계산
  user1_squared_sum = np.sum(  np.square( dataset[user1][item]) for item in common_movies  )
  user2_squared_sum = np.sum(  np.square( dataset[user2][item]) for item in common_movies  )

  # 두 사용자가 모두 평가한 모든 영화의 평점의 곱의 합
  sum_of_products = np.sum( np.sum( dataset[user1][item]*dataset[user2][item] ) for item in common_movies  )

  num_rations = len(common_movies)

  #피어슨 상관관계 점수 계산
  Sxy =  sum_of_products - (user1_sum*user2_sum / num_rations)  # 공분산
  Sxx = user1_squared_sum - np.square(user1_sum) / num_rations  # user1의 분산
  Syy = user2_squared_sum - np.square(user2_sum) / num_rations  # user2의 분산

  # 편차가 없으면 점수는 0
  if Sxx * Syy == 0:
    return 0

  return Sxy / np.sqrt(Sxx * Syy)