import random

# 1. 맛집 데이터
menu_data = {
    "기쁨": ["스테이크", "파스타", "초밥", "피자", "당근케이크"],
    "슬픔": ["떡볶이", "불닭볶음면", "짬뽕", "김치찜", "초콜릿"],
    "피곤": ["삼겹살", "국밥", "장어덮밥", "아메리카노", "곰탕"],
    "보통": ["치킨", "햄버거", "백반", "돈가스", "샌드위치"]
}

print("--- 👋 안녕하세요! 만족할 때까지 찾아주는 메뉴 추천기입니다 ---")
user_name = input("이름이 무엇인가요? ")
user_feel = input("현재 기분이 어떠신가요? (기쁨, 슬픔, 피곤, 보통): ")

# 기분이 데이터에 없는 경우 처리
if user_feel not in menu_data:
    print(f"죄송해요, {user_feel} 기분 데이터는 없어서 '보통' 기분으로 추천해 드릴게요.")
    user_feel = "보통"

# 2. 반복문 시작: 사용자가 만족할 때까지!
while True:
    # 해당 기분 리스트에서 무작위 하나 선택
    pick = random.choice(menu_data[user_feel])
    
    print(f"\n🤖 추천 메뉴: [{pick}] 어떠신가요?")
    answer = input("마음에 드시나요? (응 / 아니 / 다른거): ")

    # 3. 사용자 대답에 따른 조건 분기
    if answer == "응" or answer == "좋아":
        print(f"🎉 탁월한 선택입니다! {user_name}님, 맛있는 식사 되세요!")
        break  # 루프를 탈출하여 프로그램 종료
    
    elif answer == "아니" or answer == "다른거":
        print("🔄 다른 메뉴를 찾아볼게요...")
        # 이 루프는 break를 만나지 않았으므로 다시 위로 올라가서 random.choice를 실행합니다.
    
    else:
        print("❓ '응' 또는 '아니'로 대답해 주세요!")
    