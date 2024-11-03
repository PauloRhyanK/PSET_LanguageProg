# IDENTIFICAÇÃO DO ESTUDANTE:
# Preencha seus dados e leia a declaração de honestidade abaixo. NÃO APAGUE
# nenhuma linha deste comentário de seu código!
#
#    Nome completo: Paulo Rhyan Kuster
#    Matrícula: 202299971
#    Turma: CC6N
#    Email: paulorhyank@gmail.com
#
# DECLARAÇÃO DE HONESTIDADE ACADÊMICA:
# Eu afirmo que o código abaixo foi de minha autoria. Também afirmo que não
# pratiquei nenhuma forma de "cola" ou "plágio" na elaboração do programa,
# e que não violei nenhuma das normas de integridade acadêmica da disciplina.
# Estou ciente de que todo código enviado será verificado automaticamente
# contra plágio e que caso eu tenha praticado qualquer atividade proibida
# conforme as normas da disciplina, estou sujeito à penalidades conforme
# definidas pelo professor da disciplina e/ou instituição.


# Imports permitidos (não utilize nenhum outro import!):
import sys
import math
import base64
import tkinter
from io import BytesIO
from PIL import Image as PILImage


# Classe Imagem:
class Imagem:
    def __init__(self, largura, altura, pixels):
        self.largura = largura
        self.altura = altura
        self.pixels = pixels

    def get_pixel(self, x, y):
        # Aqui estamos tratando os pixels que estão fora da imagem, usando a versão estendida.
        if x < 0:
            x = 0
        elif x >= self.largura:
            x = self.largura - 1
        
        if y < 0:
            y = 0
        elif y >= self.altura:
            y = self.altura - 1 

        return self.pixels[y * self.largura + x] # Ele quer uma indice unidemensional.
    

    def set_pixel(self, x, y, c):
        self.pixels[y * self.largura + x] = c # Ele selecione o pixel de acordo com o indice fornecido e seta com o valor c fornecido.

    def aplicar_por_pixel(self, func):
        # Aqui alteramos ordem errada, tiramos declarações desncesessárias e aplicarmos a função correta.
        resultado = Imagem.nova(self.largura, self.altura)
        for x in range(resultado.largura):
            for y in range(resultado.altura):
                cor = self.get_pixel(x, y)
                nova_cor = func(cor)
                resultado.set_pixel(x, y, nova_cor)
        return resultado

    def invertida(self):
        return self.aplicar_por_pixel(lambda c: 255 - c) # 256 => 255
    

    # Verificando se o valor dos pixels no de imagens ultrapassa os limites.
    def verificar_pixels(self):
        for x in range(self.largura):
            for y in range(self.altura):
                pixel = self.get_pixel(x, y)  # Pegando o pixel

                # Verificando o pixel
                if pixel > 255:
                    pixel = 255
                elif pixel < 0:
                    pixel = 0
                if isinstance(pixel, float):
                    pixel = round(pixel)  # Corrigido para arredondar o valor do pixel

                # Alterando o pixel dentro do limite
                self.set_pixel(x, y, pixel)

    def correlacao(self, filtro):
        resultado = Imagem.nova(self.largura, self.altura)
        pontocentral = len(filtro) // 2 # Criando o ponto central que sera usado para achar os elementos adjacentes

        # Percorrendo a imagem
        for x in range(self.largura): 
            for y in range(self.altura):
                soma = 0 # Variavel que vai armazenar o novo valor no pixel

                # Percorrendo o kernel
                for i in range(len(filtro)):
                    for j in range(len(filtro)):
                        # Pegando o pixel adjacente
                        ix = x + i - pontocentral
                        jy = y + j - pontocentral

                        # Somando o pixel adjacente com o pixel do kernel
                        soma += self.get_pixel(ix, jy) * filtro[i][j]

                # Aqui estamos aplicando o novo valor do pixel na imagem    
                resultado.set_pixel(x,y, soma)

        

        return resultado
    
    def kernel_borrada(self, n):
        valor = 1 / (n * n) # Calculando o valor do kernel e garantindo que a soma dos elementos seja 1
        kernel = [[valor for _ in range(n)] for _ in range(n)]  # Criando o kernel de largura e altura n
        return kernel

    def borrada(self, n):
        # Aplicando a correlação com o kernel borrada, a função de tratar limite ja esta aplciada em correlação
        resultado = self.correlacao(self.kernel_borrada(n))  # n define a intensidade do filtro
        resultado.verificar_pixels()  # Verificando se o valor dos pixels no de imagens ultrapassa os limites
        return resultado

    def focada(self, n):
        imgBorrada = self.borrada(n) # Criando versão borrada da imagem

        for x in range(self.largura):
            for y in range(self.altura):
                nPixel = (self.get_pixel(x,y) * 2) - imgBorrada.get_pixel(x,y)
                self.set_pixel(x,y, nPixel)

        self.verificar_pixels() # Verificando se o valor dos pixels no de imagens ultrapassa os limites
        return self

    def bordas(self):
        raise NotImplementedError

    # Abaixo deste ponto estão utilitários para carregar, salvar e mostrar
    # as imagens, bem como para a realização de testes. Você deve ler as funções
    # abaixo para entendê-las e verificar como funcionam, mas você não deve
    # alterar nada abaixo deste comentário.
    #
    # ATENÇÃO: NÃO ALTERE NADA A PARTIR DESTE PONTO!!! Você pode, no final
    # deste arquivo, acrescentar códigos dentro da condicional
    #
    #                 if __name__ == '__main__'
    #
    # para executar testes e experiências enquanto você estiver executando o
    # arquivo diretamente, mas que não serão executados quando este arquivo
    # for importado pela suíte de teste e avaliação.
    def __eq__(self, other):
        return all(getattr(self, i) == getattr(other, i)
                   for i in ('altura', 'largura', 'pixels'))

    def __repr__(self):
        return "Imagem(%s, %s, %s)" % (self.largura, self.altura, self.pixels)

    @classmethod
    def carregar(cls, nome_arquivo):
        """
        Carrega uma imagem do arquivo fornecido e retorna uma instância dessa
        classe representando essa imagem. Também realiza a conversão para tons
        de cinza.

        Invocado como, por exemplo:
           i = Imagem.carregar('test_images/cat.png')
        """
        with open(nome_arquivo, 'rb') as guia_para_imagem:
            img = PILImage.open(guia_para_imagem)
            img_data = img.getdata()
            if img.mode.startswith('RGB'):
                pixels = [round(.299 * p[0] + .587 * p[1] + .114 * p[2]) for p in img_data]
            elif img.mode == 'LA':
                pixels = [p[0] for p in img_data]
            elif img.mode == 'L':
                pixels = list(img_data)
            else:
                raise ValueError('Modo de imagem não suportado: %r' % img.mode)
            l, a = img.size
            return cls(l, a, pixels)

    @classmethod
    def nova(cls, largura, altura):
        """
        Cria imagens em branco (tudo 0) com a altura e largura fornecidas.

        Invocado como, por exemplo:
            i = Imagem.nova(640, 480)
        """
        return cls(largura, altura, [0 for i in range(largura * altura)])

    def salvar(self, nome_arquivo, modo='PNG'):
        """
        Salva a imagem fornecida no disco ou em um objeto semelhante a um arquivo.
        Se o nome_arquivo for fornecido como uma string, o tipo de arquivo será
        inferido a partir do nome fornecido. Se nome_arquivo for fornecido como
        um objeto semelhante a um arquivo, o tipo de arquivo será determinado
        pelo parâmetro 'modo'.
        """
        saida = PILImage.new(mode='L', size=(self.largura, self.altura))
        saida.putdata(self.pixels)
        if isinstance(nome_arquivo, str):
            saida.save(nome_arquivo)
        else:
            saida.save(nome_arquivo, modo)
        saida.close()

    def gif_data(self):
        """
        Retorna uma string codificada em base 64, contendo a imagem
        fornecida, como uma imagem GIF.

        Função utilitária para tornar show_image um pouco mais limpo.
        """
        buffer = BytesIO()
        self.salvar(buffer, modo='GIF')
        return base64.b64encode(buffer.getvalue())

    def mostrar(self):
        """
        Mostra uma imagem em uma nova janela Tk.
        """
        global WINDOWS_OPENED
        if tk_root is None:
            # Se Tk não foi inicializado corretamente, não faz mais nada.
            return
        WINDOWS_OPENED = True
        toplevel = tkinter.Toplevel()
        # O highlightthickness=0 é um hack para evitar que o redimensionamento da janela
        # dispare outro evento de redimensionamento (causing um loop infinito de
        # redimensionamento). Para maiores informações, ver:
        # https://stackoverflow.com/questions/22838255/tkinter-canvas-resizing-automatically
        tela = tkinter.Canvas(toplevel, height=self.altura,
                              width=self.largura, highlightthickness=0)
        tela.pack()
        tela.img = tkinter.PhotoImage(data=self.gif_data())
        tela.create_image(0, 0, image=tela.img, anchor=tkinter.NW)

        def ao_redimensionar(event):
            # Lida com o redimensionamento da imagem quando a tela é redimensionada.
            # O procedimento é:
            #  * converter para uma imagem PIL
            #  * redimensionar aquela imagem
            #  * obter os dados GIF codificados em base 64 (base64-encoded GIF data)
            #    a partir da imagem redimensionada
            #  * colocar isso em um label tkinter
            #  * mostrar a imagem na tela
            nova_imagem = PILImage.new(mode='L', size=(self.largura, self.altura))
            nova_imagem.putdata(self.pixels)
            nova_imagem = nova_imagem.resize((event.width, event.height), PILImage.NEAREST)
            buffer = BytesIO()
            nova_imagem.save(buffer, 'GIF')
            tela.img = tkinter.PhotoImage(data=base64.b64encode(buffer.getvalue()))
            tela.configure(height=event.height, width=event.width)
            tela.create_image(0, 0, image=tela.img, anchor=tkinter.NW)

        # Por fim, faz o bind da função para que ela seja chamada quando a tela
        # for redimensionada:
        tela.bind('<Configure>', ao_redimensionar)
        toplevel.bind('<Configure>', lambda e: tela.configure(height=e.height, width=e.width))

        # Quando a tela é fechada, o programa deve parar
        toplevel.protocol('WM_DELETE_WINDOW', tk_root.destroy)


# Não altere o comentário abaixo:
# noinspection PyBroadException
try:
    tk_root = tkinter.Tk()
    tk_root.withdraw()
    tcl = tkinter.Tcl()


    def refaz_apos():
        tcl.after(500, refaz_apos)


    tcl.after(500, refaz_apos)
except:
    tk_root = None

WINDOWS_OPENED = False

if __name__ == '__main__':
    # O código neste bloco só será executado quando você executar
    # explicitamente seu script e não quando os testes estiverem
    # sendo executados. Este é um bom lugar para gerar imagens, etc.
    pass

    # O código a seguir fará com que as janelas de Imagem.mostrar
    # sejam exibidas corretamente, quer estejamos executando
    # interativamente ou não:
    if WINDOWS_OPENED and not sys.flags.interactive:
        tk_root.mainloop()
