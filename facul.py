if 0 and 1:
    print(True and 1)




questa = 'a) O tempo de uso do Whatsapp pelos funcionários da empresa é uma variável. Classifique-as.'

questb = 'b) Calcule a média de minutos de uso de Whatsapp dos funcionários da empresa.'

questc = 'c) Obtenha a variância referente ao tempo gasto com Whatsapp pelos funcionários da empresa.'

questd = 'd) Obtenha o desvio padrão referente ao tempo gasto com Whatsapp pelos funcionários da empresa.'

queste = 'e) Qual é a probabilidade do Luciano ter ganho um dos smartfones?'

questf = 'f) Qual é a probabilidade de Raul ter acertado exatamente duas das 5 questões sobre a empresa?'


alesia = {'temp':13, 'gen': 'fem'}
antonio = {'temp':17, 'gen': 'mas'}
amanda = {'temp':14, 'gen': 'fem'}
ayla = {'temp':14, 'gen': 'fem'}
beatriz = {'temp':20, 'gen': 'fem'}
carlos = {'temp':16, 'gen': 'mas'}
camila = {'temp':18, 'gen': 'fem'}
claudio = {'temp':20, 'gen': 'mas'}
darcio = {'temp':25, 'gen': 'mas'}
denis = {'temp':15, 'gen': 'mas'}
erica = {'temp':17, 'gen': 'fem'}
erivelton = {'temp':20, 'gen': 'mas'}
fabiana = {'temp':15, 'gen': 'fem'}
fabio = {'temp':14, 'gen': 'mas'}
fabricio = {'temp':16, 'gen': 'mas'}
luciano = {'temp':13, 'gen': 'mas'}
maria = {'temp':12, 'gen': 'fem'}
raul = {'temp':22, 'gen': 'mas'}
sandra = {'temp':14, 'gen': 'fem'}
vanessa =  {'temp':15, 'gen': 'fem'}

names = (alesia, antonio, amanda, ayla, beatriz, carlos, camila, claudio, darcio, denis, erica,
         erivelton, fabiana, fabio, fabricio, luciano, maria, raul, sandra, vanessa)  



media = (alesia['temp'] + antonio['temp'] + amanda['temp'] + ayla['temp'] + antonio['temp'] + 
      beatriz['temp'] + carlos['temp'] + camila['temp'] + claudio['temp'] + darcio['temp'] + 
      denis['temp'] + erica['temp'] + erivelton['temp'] + fabiana['temp'] + fabio['temp'] + 
      fabricio['temp'] + luciano['temp'] + maria['temp'] + raul['temp'] + sandra['temp'] + vanessa['temp']) 

md = 0
for name in names:
    md += 1
    
print(questa, 'São todas variáveis quantitativas continuas pois resultam de um numero infinito de valores'
      'que podem ser associados a pontos em uma escala continua.')

print('')

print(questb, media/md, end="\t")

print(questc, )