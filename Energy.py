import requests
from datetime import datetime


# ✅ 1. 기본 에너지 분석 클래스
class EnergyGuard2026:
    def __init__(self, my_usage):
        self.my_usage = my_usage
        self.date = datetime.now().strftime("%Y-%m-%d")
        
        self.service_key = "YOUR_API_KEY_HERE"
        
        self.base_rates = [910, 1600, 7300]
        self.unit_rates = [125.5, 220.3, 315.8]
        self.climate_fee = 10.5
        self.fuel_adj_fee = 5.0

    def get_solar_data(self):
        url = "https://apis.data.go.kr/B552115/PvAmountByPwrGen/getPvAmountByPwrGen"
        params = {
            'serviceKey': self.service_key,
            'pageNo': '1',
            'numOfRows': '5',
            'dataType': 'JSON',
            'date': datetime.now().strftime("%Y%m%d")
        }
        try:
            res = requests.get(url, params=params, timeout=3)
            items = res.json()['response']['body']['items']['item']
            return float(items[0]['amount'] if isinstance(items, list) else items['amount'])
        except:
            return 350.0

    def get_market_data(self):
        url = "https://dataopen.kospo.co.kr/openApi/Trade/EteMarketOperList"
        params = {
            'serviceKey': self.service_key,
            'pageNo': '1',
            'numOfRows': '1',
            'type': 'json'
        }
        try:
            res = requests.get(url, params=params, timeout=3)
            return float(res.json()['data'][0]['tradeVol'])
        except:
            return 75000.0

    def calculate_carbon_score(self):
        solar = self.get_solar_data()
        market = self.get_market_data()

        ratio = (solar / market) * 1000
        score = min(100, max(10, ratio * 20))
        return round(score, 1)

    def calculate_bill(self, kwh):
        if kwh <= 200:
            base = self.base_rates[0]
            energy = kwh * self.unit_rates[0]

        elif kwh <= 400:
            base = self.base_rates[1]
            energy = (200 * self.unit_rates[0]) + ((kwh - 200) * self.unit_rates[1])

        else:
            base = self.base_rates[2]
            energy = (200 * self.unit_rates[0]) + \
                     (200 * self.unit_rates[1]) + \
                     ((kwh - 400) * self.unit_rates[2])

        extra = kwh * (self.climate_fee + self.fuel_adj_fee)
        total = (base + energy + extra) * 1.137

        return int(total)

    def calculate_carbon_score(self):
        solar = self.get_solar_data()
        market = self.get_market_data()

        ratio = (solar / market) * 1000
        score = min(100, max(10, ratio * 20))
        return round(score, 1)

    def analyze(self):
        carbon_score = self.calculate_carbon_score()
        my_bill = self.calculate_bill(self.my_usage)
        
        print("\n" + "="*50)
        print(f"📊 2026 에너지 리포트 ({self.date})")
        print("="*50)
        print(f"🏠 전력 사용량 : {self.my_usage} kWh")
        print(f"💰 예상 전기 요금 : {my_bill:,} 원")
        print(f"🌿 탄소 점수 : {carbon_score} / 100")
        print("="*50)


# ✅ 2. 확장 클래스 (자취생 + 스마트 기능)
class JachuiEnergyManager(EnergyGuard2026):
    def __init__(self, my_usage, rent):
        super().__init__(my_usage)
        self.rent = rent

    # 🔥 추가 기능 1: 누진구간 경고
    def progressive_warning(self):
        if self.my_usage < 200:
            return f"🚨 200kWh까지 {200 - self.my_usage:.1f}kWh 남음"
        elif self.my_usage < 400:
            return f"🚨 400kWh까지 {400 - self.my_usage:.1f}kWh 남음"
        else:
            return "⚠️ 이미 최고 요금 구간입니다!"

    # 🔥 추가 기능 2: 요금 예측
    def predict_next_bill(self, growth_rate=0.1):
        predicted_usage = self.my_usage * (1 + growth_rate)
        return self.calculate_bill(predicted_usage)

    # 🔥 추가 기능 3: 효율 점수
    def efficiency_score(self):
        if self.my_usage < 200:
            return 90
        elif self.my_usage < 350:
            return 70
        else:
            return 40

    # 🔥 추가 기능 4: 절약 팁
    def saving_tip(self):
        if self.my_usage > 400:
            return "🔥 에어컨/난방 사용 줄이고 대기전력 차단!"
        elif self.my_usage > 250:
            return "⚡ 누진구간 진입 주의!"
        else:
            return "🌿 현재 사용량 매우 효율적!"

    # 🔥 추가 기능 5: 총 생활비
    def total_living_cost(self):
        return self.rent + self.calculate_bill(self.my_usage)

    # 🔥 최종 분석 (오버라이딩)
    def analyze(self):
        super().analyze()

        print("\n📊 추가 분석")
        print("-"*50)

        print("⚠️ 구간 경고:", self.progressive_warning())

        predicted = self.predict_next_bill(0.1)
        print(f"📈 다음 달 예상 요금: {int(predicted):,} 원")

        print(f"🏆 에너지 효율 점수: {self.efficiency_score()}점")

        print(f"💡 절약 팁: {self.saving_tip()}")

        print(f"🏠 월세 + 전기요금: {self.total_living_cost():,} 원")

        print("="*50 + "\n")


# ✅ 3. 실행
if __name__ == "__main__":
    try:
        usage = float(input("전력 사용량(kWh): "))
        rent = int(input("월세(원): "))

        manager = JachuiEnergyManager(usage, rent)
        manager.analyze()

    except ValueError:
        print("❌ 숫자로 입력해주세요")
