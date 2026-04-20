from flask import Flask, request
import random

app = Flask(__name__)

# Rotas
@app.route('/')
def homepage():
    return """
    bem-vindo à homepage, digite "/jogar" para começar. <br
    <h2>Bem-Vindo ao Jogo!</h2>
    <p>Escolha o modo:</p>
    <a href="/jogar?modo=5">Jogar de 1 a 5</a><br>
    <a href="/jogar?modo=10">Jogar de 1 a 10</a><br>
    <a href="/jogar?modo=100">Jogar de 1 a 100</a>
    """

@app.route('/jogar')
def jogar():
    modo = request.args.get('modo')
    palpite = request.args.get('palpite')
    
    if modo not in ['5', '10', '100']:
        return 'Modo inválido. Escolha 5, 10 ou 100. <a href="/">Voltar</a>'
    
    modo_int = int(modo)
    
    if not palpite:
        return f'''
        <h3>Modo: 1 a {modo}</h3>
        <form action="/jogar" method="get">
            <input type="hidden" name="modo" value="{modo}">
            Digite um número: <input type="number" name="palpite" min="1" max="{modo}" required>
            <button type="submit">Chutar</button>
        </form>
        <a href="/">Mudar modo</a>
        '''
    
    try:
        sua = int(palpite)
    except ValueError:
        return f'Número inválido. <a href="/jogar?modo={modo}">Tentar de novo</a>'
    
    rand = random.randint(1, modo_int)
    
    if sua == rand:
        resultado = 'Números iguais! Você acertou!'
    else:
        resultado = 'Números diferentes. Errou!'
    
    return f'''
    <h3>Resultado</h3>
    <p>{resultado}</p>
    <p>Seu número: {sua} | Sorteado: {rand}</p>
    <br>
    <a href="/jogar?modo={modo}">Jogar de novo</a><br>
    <a href="/">Mudar modo</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)
