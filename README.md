코렙에서 한글 폰트 설치하기

# 1. 코렙에서 한글 폰트 설치하기
!sudo apt-get install -y fonts-nanum

!sudo fc-cache -fv

!rm ~/.cache/matplotlib -rf

# 2. 설치가 다 되면 메뉴-런타임-런타임 다시시작


# 3. 한글폰트 적용하기

import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic' # 나눔바른고딕 적용하기

# 4. 한글폰트 확인하기

plt.plot([1, 2, 3], [1, 2, 3])

plt.title('한글')

===============================================================================================================================================
