# Stock Admin

Flask で動作する株価分析管理画面のサンプルアプリです。ダミーデータで動作するため、外部 API への接続は不要です。

## 機能

- **ダッシュボード** (`/`)
  - 対象銘柄数 / 上昇・下落銘柄数 / 平均騰落率のサマリーカード
  - 日経平均風の指数推移チャート (Chart.js)
  - 値上がり率 / 値下がり率 / 出来高ランキング
- **銘柄一覧** (`/stocks`)
  - 12銘柄（トヨタ、ソニー、任天堂 など）を表示
  - 銘柄コード / 銘柄名でのフリーワード検索
  - セクターでの絞り込み
- **銘柄詳細** (`/stocks/<code>`)
  - 株価・出来高チャート
  - 期間切り替え（1ヶ月 / 3ヶ月 / 6ヶ月 / 1年）
  - 銘柄情報（コード・名称・セクター・市場区分）
- **JSON API**
  - `GET /api/stocks/<code>/history?days=<n>` — 指定銘柄の株価・出来高履歴
  - `GET /api/index/history?days=<n>` — 指数推移

## 必要要件

- Python 3.10+
- Flask 3.x

## セットアップ

```bash
# 仮想環境を作成
python3 -m venv venv

# 仮想環境を有効化
source venv/bin/activate          # macOS / Linux
# venv\Scripts\activate           # Windows (PowerShell)

# 依存パッケージをインストール
pip install -r requirements.txt
```

## 起動方法

```bash
python app.py
```

起動後、ブラウザで以下にアクセスします:

```
http://127.0.0.1:5000/
```

デフォルトでは `0.0.0.0:5000` で待ち受け、デバッグモードが有効になっています。

## ディレクトリ構成

```
stock-app/
├── app.py              # Flask ルーティング
├── dummy_data.py       # ダミーデータ生成ロジック (seed 固定で再現性あり)
├── requirements.txt    # 依存パッケージ
├── static/
│   └── style.css       # 画面スタイル
└── templates/
    ├── base.html       # 共通レイアウト
    ├── dashboard.html  # ダッシュボード
    ├── stocks.html     # 銘柄一覧
    └── detail.html     # 銘柄詳細
```

## ダミーデータについて

`dummy_data.py` 内で銘柄コードをシードとして乱数を生成しているため、起動するたびに値が変わることはありません。銘柄を追加したい場合は `STOCKS` リストに辞書を追加してください。

```python
STOCKS = [
    {"code": "7203", "name": "トヨタ自動車", "sector": "輸送用機器", "market": "プライム"},
    # ここに追加
]
```

## ライセンス

サンプル用途の実装です。自由に改変してご利用ください。
