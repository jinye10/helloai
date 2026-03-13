print("안녕하세요! 파이썬 공부를 시작합니다.")
import random  # 랜덤 기능을 가져와요

# 1. 컴퓨터가 1에서 20 사이의 비밀 숫자를 정합니다
secret_number = random.randint(1, 20)
attempts = 0

print("어서오세요! 1부터 20 사이의 숫자를 맞춰보세요.")

# 2. 맞출 때까지 무한 반복!
while True:
    guess = int(input("숫자를 입력하세요: ")) # 사용자 입력을 숫자로 변환
    attempts += 1
    
    # 3. 조건문으로 정답 비교하기
    if guess < secret_number:
        print("UP! 더 큰 숫자를 생각해보세요.")
    elif guess > secret_number:
        print("DOWN! 더 작은 숫자를 생각해보세요.")
    else:
        print(f"정답입니다! {attempts}번 만에 맞추셨네요! 🎉")
        break # 반복문을 빠져나갑니다