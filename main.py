from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from currency_converter import convert_currency

# .envファイルから環境変数を読み込む
load_dotenv()

app = Flask(__name__)

# APIキーを環境変数から取得
api_key = os.getenv("EXCHANGERATE_API_KEY")

@app.route('/')
def index():
    """
    トップページをレンダリングします。
    """
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    """
    フォームから送信されたデータを受け取り、通貨換算を実行して結果を返す。
    """
    amount = float(request.form['amount'])
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']

    # currency_converter.pyの関数を呼び出す
    result = convert_currency(amount, from_currency, to_currency, api_key)

    # 結果をindex.htmlに渡して再表示する
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)