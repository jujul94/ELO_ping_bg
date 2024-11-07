from flask import Flask, render_template

app = Flask(__name__)

# Route pour la page d'accueil
@app.route('/')
def home():
    return render_template('index.html')  # Charge le fichier HTML

# Lancer l'application en mode développement
if __name__ == '__main__':
    app.run(debug=True)
