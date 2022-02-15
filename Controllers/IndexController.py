from Service.DataHendler import DataHendler
from server.instance import server

app = server.app


class IndexController():
    @app.route("/")
    def start():
        return "Desafio Python"

    @app.route("/showData", methods=["GET"])
    def show_data():
        dh = DataHendler()
        return str(dh.get_numbers_from_api(
            "http://challenge.dienekes.com.br/api/numbers?page="
        ))
