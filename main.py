from flask import Flask, render_template, flash, redirect, url_for, session, logging, request, jsonify, Response  # install edilecek
import firebase_admin  # install edilecek
from firebase_admin import credentials, firestore, initialize_app




@app.route("/")
def anasayfa():
    return render_template("index.html")


@app.route("/kayit",  methods=['GET', 'POST'])
def kayit():
    if request.method == "POST":
        arızakodu = request.form['arızakodu']
        baslik = request.form['baslik']
        aciklama = request.form['aciklama']
        oncelik = request.form['oncelik']
        anlam = request.form['editor1']
        neden = request.form['editor2']
        oneri = request.form['editor3']
        yeni_kod = {"arızakodu": arızakodu, "baslik":baslik, "aciklama": aciklama, "anlam": anlam,'neden':neden,
                       "oneri": oneri, "oncelik":oncelik}

        dbkodlar.insert_one(yeni_kod)
        return render_template("index.html")
    else:
        return render_template("index.html")
    return render_template("index.html")


@app.route("/oku",  methods=['GET', 'POST'])
def oku():
    sonuc = dbkodlar.find()
    sonuc = [
        {
            'arızakodu': kod['arızakodu']
        } for kod in sonuc]
    json = jsonify(sonuc)
    return json

if __name__ == "__main__":
    app.run(debug=True)

