import requests
import time
from datetime import datetime, timezone, timedelta

# ==========================================
# 🔑 OpenWeather API 키 입력
# ==========================================
WEATHER_API_KEY = "키 입력하세요"
# ==========================================


def get_traffic_status(weather_main, humidity):
    """퇴근요정 전용 교통 분석"""
    now_hour = datetime.now(timezone(timedelta(hours=9))).hour  # KST 적용

    is_rush_hour = (17 <= now_hour <= 20)
    is_bad_weather = weather_main in ["Rain", "Snow", "Drizzle", "Thunderstorm"] or humidity > 90

    if is_rush_hour and is_bad_weather:
        return "🛑 지옥 퇴근길", "오늘은 진짜 헬입니다… 가능하면 늦게 이동하세요 😇"
    elif is_rush_hour:
        return "⚠️ 빡센 퇴근길", "차 막히는 시간입니다! 여유를 가지세요 🎵"
    elif is_bad_weather:
        return "🌧️ 위험한 도로", "노면이 미끄럽습니다! 안전거리 확보 🚗"
    else:
        return "✅ 평화로운 귀가", "쾌적한 퇴근길입니다 😎"


def main():
    print("=" * 60)
    print("   ✨ 퇴근요정 v1.3 (KST 적용 + 디버깅 포함) ✨   ")
    print("=" * 60)

    city = input("📍 도시 입력 (영문: Seoul, Busan, Jeju 등): ").strip().capitalize()

    print(f"\n🧚‍♀️ {city} 상황 분석 중...")
    print("-" * 60)

    while True:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city},KR&appid={WEATHER_API_KEY}&units=metric&lang=kr"

        try:
            response = requests.get(url, timeout=5)

            # 🔍 디버깅 정보 출력
            print(f"[DEBUG] 상태코드: {response.status_code}")

            if response.status_code != 200:
                print("❌ 서버 응답 오류")
                print(f"[DEBUG] 응답 내용: {response.text}")
                time.sleep(5)
                continue

            data = response.json()

            if data.get("cod") == 200:
                # 🇰🇷 KST 시간 적용
                kst = timezone(timedelta(hours=9))
                now_time = datetime.now(kst).strftime('%H:%M:%S')

                temp = data['main']['temp']
                humidity = data['main']['humidity']
                desc = data['weather'][0]['description']
                main_weather = data['weather'][0]['main']

                traffic_title, advice = get_traffic_status(main_weather, humidity)

                print(f"\n[{now_time}] 🌆 {city}")
                print(f"🌡️ 날씨: {desc} ({temp}°C / 습도 {humidity}%)")
                print(f"🚗 퇴근 난이도: {traffic_title}")
                print(f"💬 퇴근요정: {advice}")
                print("-" * 60)

            else:
                print(f"❌ 오류: {data.get('message')}")
                break

        except requests.exceptions.Timeout:
            print("⏱️ 요청 시간 초과 (네트워크 확인)")
        except Exception as e:
            print(f"❌ 오류 발생: {e}")

        time.sleep(30)


if __name__ == "__main__":
    main() 