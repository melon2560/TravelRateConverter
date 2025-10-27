import requests

def convert_currency(amount, from_currency, to_currency, api_key):
    """
    ExchangeRate-APIを使用して、指定された通貨間で金額を換算します。

    Args:
        amount (float): 換算する金額。
        from_currency (str): 換算元の通貨コード (例: "JPY")。
        to_currency (str): 換算先の通貨コード (例: "KRW")。
        api_key (str): ExchangeRate-APIのAPIキー。

    Returns:
        str: 換算結果の文字列。エラーが発生した場合はエラーメッセージを返す。
    """
    # APIエンドポイントのURLを構築
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}/{amount}"

    try:
        # APIにリクエストを送信
        response = requests.get(url)
        response.raise_for_status()  # ステータスコードが200番台以外の場合は例外を発生

        # レスポンスをJSON形式で解析
        data = response.json()

        # APIからのレスポンスが成功だったかを確認
        if data.get("result") == "success":
            conversion_result = data.get("conversion_result")
            # 整形した結果文字列を返す
            return f"{amount:,} {from_currency} = {conversion_result:,.2f} {to_currency}"
        else:
            # APIがエラーを返した場合
            error_type = data.get("error-type", "Unknown error")
            return f"APIエラー: {error_type}"

    except requests.exceptions.RequestException as e:
        # ネットワークエラーなど、リクエスト自体に失敗した場合
        return f"リクエストエラー: {e}"
    except Exception as e:
        # その他の予期せぬエラー
        return f"予期せぬエラーが発生しました: {e}"
