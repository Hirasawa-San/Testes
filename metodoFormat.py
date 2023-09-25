yui = "Yui"

mio = "Mio"

mugi = "mugi"

formatada = ''

string = "Hirasawa {guitah}, Akiyama {elizabeth} e Kotobuki Tsu{mugi}"  # as chaves são utilizada para (a principio) utilizar o metodo .format

formatada = string.format(guitah=yui, elizabeth=mio, mugi=mugi)         # Isso se chama parâmetro nomeado, que básicamente facilita a utilização
                                                                        # Eles não precisam necessáriamente serem nomeados, porém, dessa forma-
                                                                        # (sem nomea-los) você só utilizaria eles só com o as duas chaves '{}'
                                                                        # porém eles só poderiam se utilizados na ordem em que estão e uma unica
                                                                        # vez.
print(formatada)                                                        # Quando uma função está dentro de um obj ela é chamada de metodo