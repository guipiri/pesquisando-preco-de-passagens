# Script que pesquisa passagens no site 123Milhas
<p>O script, feito em python, realiza oito consultas nos site da 123Milhas (variando datas e destinos, com a partida sempre em 'SAO', que é São Paulo) e escreve nos arquivos .CSV que estão no projeto.</p>
<p>Para rodar o projeto localmente, certifique-se que tenha o Python 3.10.4 e o virtualenv instalados.</p>
<p>Sequência de comandos (Windows)</p>
<ol>
  <li>git clone https://github.com/guipiri/pesquisando-preco-de-passagens.git</li>
  <li>Entre na pasta do projeto</li>
  <li>virtualenv .env</li>
  <li>source .env/Scripts/activate</li>
  <li>pip install -r requirements.txt</li>
</ol>

<p>Além disso, você deve baixar a versão do chromedriver compatível com sua versão do Chrome. Aqui nesse link: https://www.chromedriver.chromium.org/downloads . E depoi colocá-lo na pasta .env/Scripts.</p>
<p>Finalmente, rode "python main.py" no diretório do projeto e veja a mágica acontecer. Depois confira se mais um linha foi criada em cada um dos arquivos .csv.<p/>

## Nomenclatura dos arquivos csv
<p>"milhas123{abreviação do destino}{data de ida}{data de volta}"</p>
