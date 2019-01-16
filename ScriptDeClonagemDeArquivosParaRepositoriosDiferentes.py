import io
import os

#lista de sistemas (ex: acma/paeu/pari etc)
listaSistema = os.listdir('\\Users\\jessica.andrade\\Desktop\\acmaORIGEM\\')

#1° for para percorrer a lista de sistemas.
for sistema in listaSistema:

    #lista de telas do sistema escolhido(ex: RAberturaos)
    listaTela = os.listdir('\\Users\\jessica.andrade\\Desktop\\acmaORIGEM\\'+sistema+'\\reports\\')

    #2° for para a percorrer a lista de telas
    for lingSis in listaTela:

      #Lista de localizações do sistema e da tela pre-definido.   
        listaLinguagem = os.listdir('\\Users\\jessica.andrade\\Desktop\\acmaORIGEM\\'+sistema+'\\reports\\'+lingSis)
        
        #3° for para a percorrer a lista de localizações (es.properties)
        for ling in listaLinguagem:
            
            #if para validação de localização diferente de pt_br
            if ling != "pt_BR.properties":
                arquivoOrigem = io.open('\\Users\\jessica.andrade\\Desktop\\acmaORIGEM\\'+sistema+'\\reports\\'+lingSis+'\\'+ling, 'r', encoding="utf8")
                textoOrigem = arquivoOrigem.readlines()

                arquivoDestino = io.open('\\Users\\jessica.andrade\\Desktop\\acmaDESTINO\\'+sistema+'\\reports\\'+lingSis+'\\localization\\revision\\'+ling, 'r', encoding="utf8")
                textoDestino = arquivoDestino.readlines()

                lista=[]

            #4° for para preencher uma lista com os campos separados no texto de origem.   
            for x in textoOrigem:
                lista.append(x.split("="))

            #5° para percorrer a lista de destino e validar os campos após o sinal de igual, unindo chave a valor.
            for x in range(len(textoDestino)):
                for y in lista:
                    if y[0] in textoDestino[x]:
                        #textoDestino[x] = y[0]+"="+y[1]
                        i = "="
                        seq = (y[0], y[1])
                        textoDestino[x] = i.join(seq)

                    #Para a sobrescrita das localizações de destino.
                    with open('\\Users\\jessica.andrade\\Desktop\\acmaDESTINO\\'+sistema+'\\reports\\'+lingSis+'\\localization\\revision\\' +ling, 'w', encoding="utf8") as file:
                        file.writelines(textoDestino)