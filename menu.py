import random

# 1. 기본 데이터베이스
menu_db = {
    "한식": {
        "밥": ["비빔밥", "김치볶음밥", "제육덮밥", "국밥"],
        "면": ["잔치국수", "칼국수", "냉면"]
    },
    "양식": {
        "밥": ["리조또", "오므라이스", "필라프"],
        "면": ["까르보나라", "알리오올리오", "토마토 파스타"]
    }
    # (일식, 중식도 동일한 구조로 추가 가능합니다)
}

print("--- 🌦️ 날씨와 취향을 고려한 무한 추천기 ---")

# 2. 날씨 및 취향 입력
weather = input("오늘 날씨가 어떤가요? (맑음, 비): ")
category = input("음식 종류 (한식, 양식): ")
food_type = input("밥 vs 면: ")

# 선택한 카테고리의 리스트 가져오기 (원본 보존을 위해 복사본 생성)
options = list(menu_db[category][food_type])
rejected_items = []  # 거절한 메뉴를 모아둘 바구니

# 3. 날씨에 따른 메뉴 추가 (조건문 + 리스트 추가)
if weather == "비":
    extra = "파전" if food_type == "밥" else "짬뽕"
    print(f"☔ 비가 오니까 특별히 '{extra}'을(를) 후보에 추가할게요!")
    options.append(extra)

# 4. 추천 루프
while True:
    # 메뉴가 다 떨어졌을 때의 처리 (재시작 로직)
    if not options:
        print("\n🤔 모든 후보를 거절하셨네요. 거절했던 메뉴들로 다시 골라볼까요?")
        options = list(rejected_items) # 거절했던 메뉴들을 다시 후보로 복구
        rejected_items = []            # 거절 바구니 비우기
        continue # 루프의 처음으로 돌아가기

    pick = random.choice(options)
    print(f"\n💡 추천 메뉴: [{pick}]")
    ans = input("마음에 드시나요? (y/n): ").lower()

    if ans == 'y':
        print(f"🎉 드디어 결정! [{pick}] 맛있게 드세요!")
        break
    else:
        print(f"❌ '{pick}' 제외.")
        rejected_items.append(pick) # 거절한 메뉴 보관
        options.remove(pick)        # 현재 후보에서 삭제
    