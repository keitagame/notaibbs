from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
surez = [["爆誕","/a"],["ニュース","/b"]]

class BBS(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        # ルーティング
        if path == "/":
            html = """
            <!DOCTYPE html>
<html lang="ja">
<head>
<title>いた</title>
<style>
 

</style>
</head>
<body>
<div style="text-align:center; background:white">
<h3>深テ掲示板へようこそ</h3>
<p>ここは深夜テンションの猫が集まる<br>
スレ立て系掲示板です。<br>
バグったらkeitaへ報告ください</p>
<h3 style="padding:12px; border-bottom:1px solid black;">アクティブなスレ一覧</h3>
            """
            +
            for i in range(surez.length):
                """<a href="""+surez[i][1]+""">"""+surez[i][0]+"""</a>"""
            """
            </div>
            </body>
            </html>

            """

        elif path == "/about":
            html = """
            <h1>Aboutページ</h1>
            <a href="/">戻る</a>
            """

        elif path == "/user":
            query = parse_qs(parsed_path.query)
            name = query.get("name", ["ゲスト"])[0]

            html = f"""
            <h1>ユーザー: {name}</h1>
            <a href="/">戻る</a>
            """

        else:
            self.send_response(404)
            html = "<h1>404 Not Found</h1>"

        self.wfile.write(html.encode("utf-8"))

server = HTTPServer(("0.0.0.0", 8000), BBS)
print("http://localhost:8000 で起動")
server.serve_forever()
