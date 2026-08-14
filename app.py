from flask import Flask, render_template, abort
import os

<<<<<<< HEAD
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

# pastas explícitas: funciona rodando de qualquer diretório (python "caminho/app.py")
app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)
# recarrega o HTML a cada request (sem precisar reiniciar o servidor ao editar uma LP)
app.config["TEMPLATES_AUTO_RELOAD"] = True
=======
app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
>>>>>>> 28eb8a73d835c2e95a2196e7f3778d0eebdbe6fc

@app.route("/lp/<slug>")
@app.route("/<slug>")
def lp(slug):
<<<<<<< HEAD
    path = os.path.join(TEMPLATES_DIR, f"{slug}.html")
=======
    path = os.path.join(BASE_DIR, "templates", f"{slug}.html")
>>>>>>> 28eb8a73d835c2e95a2196e7f3778d0eebdbe6fc
    if not os.path.exists(path):
        abort(404)
    return render_template(f"{slug}.html")

@app.route("/lp/help")
def list_slugs():
=======
    templates_dir = os.path.join(BASE_DIR, "templates")
    slug_list = [f for f in os.listdir(templates_dir) if f.endswith(".html")]
    return {str(i): f.replace(".html", "") for i, f in enumerate(slug_list)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=False)
>>>>>>> 28eb8a73d835c2e95a2196e7f3778d0eebdbe6fc
