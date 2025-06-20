from flask import Flask, render_template, request, redirect
from scripts.cget_descarga import ejecutar_descarga

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/descargar", methods=["GET", "POST"])
def descargar():
    if request.method == "GET":
        return redirect("/")

    # Si es POST, procesar normalmente
    url = request.form.get("url")
    ruta = request.form.get("ruta")

    try:
        ejecutar_descarga(url, ruta)
        mensaje = "✅ Archivos descargados correctamente."
    except Exception as e:
        mensaje = f"❌ Error durante la descarga: {str(e)}"

    return f"<h2>Resultado</h2><p>{mensaje}</p><a href='/'>← Volver</a>"

if __name__ == "__main__":
    app.run(debug=True)