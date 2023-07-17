from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
port = 1456


class Server(BaseHTTPRequestHandler):

    def _get_html(self):
        return """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Homework 1</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css">
</head>

<style>
    .block {
        position: relative;
        display: inline-block;
        width: 200px;
        height: 800px;
        background-color: gray;
        color: white;
        border: 1px solid darkblue;
        text-align: right;
        padding-bottom: 40px;
    }

    .btn-cont {
        width: 100%;
        height: 100px;
        position: absolute;
        bottom: 0;
        left: 0;
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>

<body>
<div class="container">
    <div class="row mt-5">
        <div class="col-2">
            <div class="block">
                <div class="card-body text-white">
                    <p> Меню</p>
                    <a href='/?page=Главная' type="button"
                       class="btn text-white btn-outline-white form-control bi-house-door">Главная</a>
                    <a href='/?page=Каталог' type="button"
                       class="btn text-white btn-outline-white form-control bi-speedometer"> Каталог</a>
                    <a href='/?page=Категории' type="button"
                       class="btn text-white btn-outline-white form-control bi-grid-3x3-gap">
                    Категории</a>
                    <a href='/?page=Контакты' type="button"
                       class="btn text-white btn-outline-white form-control bi-person-lines-fill"> Контакты</a>
                    <div class="btn-cont">
                        <div class="dropdown">
                            <a class="btn btn-secondary dropdown-toggle " href="#" role="button"
                               data-bs-toggle="dropdown" aria-expanded="false">Пользователь</a>
                            <ul class="dropdown-menu">
                                <li><a class="dropdown-item" href="#">Профиль</a></li>
                                <li><a class="dropdown-item" href="#">Выход</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col">
            <div class="container text-center">
                <div class="row">
                    <div class="col">
                        <h2 class="title">Контакты</h2>

                    </div>
                </div>

                <form>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1">
  </div>
  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
                  <div class="input-group">
  <span class="input-group-text">With textarea</span>
  <textarea class="form-control" aria-label="With textarea"></textarea>
</div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
                </div>
</div>


</body>
</html>"""

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(self._get_html(), "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, port), Server)
    print("Server started http://%s:%s" % (hostName, port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

