# Travel Rate Converter

日本円、韓国ウォン、シンガポールドル間の通貨を換算するためのWebアプリケーションです。

## 実行方法

1.  リポジトリをクローンします。
2.  必要なライブラリをインストールします。
    ```bash
    pip install -r requirements.txt
    ```
3.  `.env.template` ファイルをコピーして `.env` ファイルを作成します。
4.  `.env` ファイルに記載されている手順に従い、[ExchangeRate-API](https://www.exchangerate-api.com/) で取得したAPIキーを設定します。
5.  アプリケーションを実行します。
    ```bash
    flask --app main run
    ```
6.  Webブラウザで `http://127.0.0.1:5000` にアクセスします。

## APIキーの設定

本アプリケーションは、為替レートの取得に [ExchangeRate-API](https://www.exchangerate-api.com/) を利用しています。
利用にはAPIキーが必要です。アカウントを登録し、取得したAPIキーを設定してください。

### 方法1: .envファイルを使用する（開発者向け推奨）

`.env.template` ファイルをコピーして `.env` ファイルを作成し、APIキーを記載します。

```
EXCHANGERATE_API_KEY=ここに取得したAPIキーを貼り付け
```

### 方法2: 環境変数を直接設定する

システムの環境変数として設定することも可能です。本番環境ではこちらの方法が推奨されます。

#### Windows (コマンドプロンプト)

```bash
# 現在のセッションでのみ有効
set EXCHANGERATE_API_KEY=YOUR_API_KEY

# 永続的に設定
setx EXCHANGERATE_API_KEY "YOUR_API_KEY"
```
`setx`を使用した場合、新しいコマンドプロンプトを開いてから設定が反映されます。

#### Windows (PowerShell)

```powershell
# 現在のセッションでのみ有効
$env:EXCHANGERATE_API_KEY="YOUR_API_KEY"

# 永続的に設定（ユーザー環境変数）
[System.Environment]::SetEnvironmentVariable('EXCHANGERATE_API_KEY', 'YOUR_API_KEY', 'User')
```

#### macOS / Linux (bash, zshなど)

```bash
# 現在のセッションでのみ有効
export EXCHANGERATE_API_KEY="YOUR_API_KEY"
```

設定を永続化するには、お使いのシェルの設定ファイル（`~/.bashrc`, `~/.zshrc`など）に上記の`export`コマンドを追記してください。

