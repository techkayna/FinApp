from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'chave-secreta'  # Necessária para exibir mensagens flash e usar sessão

# Simulação de "banco de dados" em memória
usuarios = {}

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in usuarios and usuarios[username] == password:
        session['usuario'] = username
        flash('Login realizado com sucesso!')
        return redirect(url_for('dashboard'))
    else:
        flash('Usuário ou senha inválidos.')
        return redirect(url_for('index'))

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in usuarios:
        flash('Usuário já cadastrado.')
        return redirect(url_for('cadastro'))

    usuarios[username] = password
    flash('Cadastro realizado com sucesso!')
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'usuario' in session:
        return render_template('dashboard.html', usuario=session['usuario'])
    else:
        flash('Você precisa fazer login primeiro.')
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Logout realizado com sucesso.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
