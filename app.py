from flask import Flask, render_template, jsonify, abort, request

from dummy_data import (
    get_stock_list,
    get_stock_detail,
    get_price_history,
    get_market_summary,
    get_index_history,
)

app = Flask(__name__)


@app.route("/")
def dashboard():
    summary = get_market_summary()
    return render_template("dashboard.html", summary=summary)


@app.route("/stocks")
def stocks():
    q = request.args.get("q", "").strip()
    sector = request.args.get("sector", "").strip()
    stocks = get_stock_list()
    if q:
        stocks = [s for s in stocks if q in s["name"] or q in s["code"]]
    if sector:
        stocks = [s for s in stocks if s["sector"] == sector]
    sectors = sorted({s["sector"] for s in get_stock_list()})
    return render_template("stocks.html", stocks=stocks, sectors=sectors, q=q, sector=sector)


@app.route("/stocks/<code>")
def stock_detail(code):
    stock = get_stock_detail(code)
    if not stock:
        abort(404)
    return render_template("detail.html", stock=stock)


@app.route("/api/stocks/<code>/history")
def api_stock_history(code):
    days = int(request.args.get("days", 90))
    history = get_price_history(code, days=days)
    return jsonify(history)


@app.route("/api/index/history")
def api_index_history():
    days = int(request.args.get("days", 90))
    return jsonify(get_index_history(days=days))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
