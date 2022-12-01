from flask import Flask, request, jsonify
from app.Rejerstr_kont import RejestrKont
from app.Konto import Konto

app = Flask(__name__)


@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
    RejestrKont.addUser(konto)
    return jsonify("Konto stworzone"), 201


@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    return jsonify(RejestrKont.howManyUsers()), 201


@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    user = RejestrKont.searchUser(pesel)
    return jsonify(imie=user.imie, nazwisko=user.nazwisko, pesel=user.pesel, saldo=user.saldo), 200
