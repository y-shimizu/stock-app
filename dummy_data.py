import random
from datetime import datetime, timedelta


STOCKS = [
    {"code": "7203", "name": "トヨタ自動車", "sector": "輸送用機器", "market": "プライム"},
    {"code": "6758", "name": "ソニーグループ", "sector": "電気機器", "market": "プライム"},
    {"code": "9984", "name": "ソフトバンクグループ", "sector": "情報・通信", "market": "プライム"},
    {"code": "6861", "name": "キーエンス", "sector": "電気機器", "market": "プライム"},
    {"code": "8306", "name": "三菱UFJフィナンシャル・グループ", "sector": "銀行業", "market": "プライム"},
    {"code": "9432", "name": "日本電信電話", "sector": "情報・通信", "market": "プライム"},
    {"code": "9433", "name": "KDDI", "sector": "情報・通信", "market": "プライム"},
    {"code": "4063", "name": "信越化学工業", "sector": "化学", "market": "プライム"},
    {"code": "8035", "name": "東京エレクトロン", "sector": "電気機器", "market": "プライム"},
    {"code": "7974", "name": "任天堂", "sector": "その他製品", "market": "プライム"},
    {"code": "6098", "name": "リクルートホールディングス", "sector": "サービス業", "market": "プライム"},
    {"code": "6501", "name": "日立製作所", "sector": "電気機器", "market": "プライム"},
]


def _seeded_random(seed_key: str) -> random.Random:
    rng = random.Random()
    rng.seed(seed_key)
    return rng


def get_stock_list():
    """銘柄一覧と現在のスナップショット情報を返す"""
    stocks = []
    for s in STOCKS:
        rng = _seeded_random(s["code"])
        base_price = rng.randint(1000, 30000)
        change = round(rng.uniform(-5.0, 5.0), 2)
        current_price = round(base_price * (1 + change / 100), 1)
        volume = rng.randint(500_000, 30_000_000)
        market_cap = current_price * rng.randint(100_000_000, 5_000_000_000) / 1_000_000_000_000
        stocks.append({
            **s,
            "price": current_price,
            "change": change,
            "volume": volume,
            "market_cap": round(market_cap, 2),
        })
    return stocks


def get_stock_detail(code: str):
    for s in get_stock_list():
        if s["code"] == code:
            return s
    return None


def get_price_history(code: str, days: int = 90):
    """指定銘柄の過去 days 日分の終値推移を返す"""
    rng = _seeded_random(f"{code}-history")
    base = rng.randint(1000, 30000)
    today = datetime.now().date()
    prices = []
    price = float(base)
    for i in range(days, 0, -1):
        date = today - timedelta(days=i)
        drift = rng.uniform(-0.025, 0.027)
        price = max(100.0, price * (1 + drift))
        prices.append({
            "date": date.isoformat(),
            "price": round(price, 1),
            "volume": rng.randint(500_000, 30_000_000),
        })
    return prices


def get_market_summary():
    """市場全体のサマリー"""
    stocks = get_stock_list()
    gainers = sorted([s for s in stocks if s["change"] > 0], key=lambda x: -x["change"])[:5]
    losers = sorted([s for s in stocks if s["change"] < 0], key=lambda x: x["change"])[:5]
    actives = sorted(stocks, key=lambda x: -x["volume"])[:5]
    avg_change = round(sum(s["change"] for s in stocks) / len(stocks), 2)
    return {
        "total": len(stocks),
        "gainers_count": sum(1 for s in stocks if s["change"] > 0),
        "losers_count": sum(1 for s in stocks if s["change"] < 0),
        "avg_change": avg_change,
        "top_gainers": gainers,
        "top_losers": losers,
        "most_active": actives,
    }


def get_index_history(days: int = 90):
    """日経平均風のダミー指数推移"""
    rng = _seeded_random("nikkei-index")
    today = datetime.now().date()
    price = 38000.0
    history = []
    for i in range(days, 0, -1):
        date = today - timedelta(days=i)
        drift = rng.uniform(-0.018, 0.02)
        price = max(20000.0, price * (1 + drift))
        history.append({"date": date.isoformat(), "price": round(price, 1)})
    return history
