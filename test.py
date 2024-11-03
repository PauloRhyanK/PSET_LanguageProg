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
#


# Imports
import os
import pset1
import unittest

# Diretório
TEST_DIRECTORY = os.path.dirname(__file__)


# Classe para os testes de imagem:
class TestImagem(unittest.TestCase):
    def test_carregar(self):
        resultado = pset1.Imagem.carregar('test_images/centered_pixel.png')
        esperado = pset1.Imagem(11, 11,
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(resultado, esperado)


# Classe para os testes de inversão:
class TestInvertida(unittest.TestCase):
    def test_invertida_1(self):
        im = pset1.Imagem.carregar('test_images/centered_pixel.png')
        resultado = im.invertida()
        esperado = pset1.Imagem(11, 11,
                                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                                 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                                 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                                 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                                 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                                 255, 255, 255, 255, 255, 0, 255, 255, 255, 255, 255,
                                 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                                 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                                 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                                 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                                 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255])
        self.assertEqual(resultado,  esperado)

    def test_invertida_2(self):
        imTeste = pset1.Imagem(4, 1, [29, 89, 136, 200])
        resultado = imTeste.invertida()
        esperado = pset1.Imagem(4, 1, [226, 166, 119, 55])
        self.assertEqual(resultado, esperado)

    def test_imagens_invertidas(self):
        for nome_arquivo in ('mushroom', 'twocats', 'chess'):
            with self.subTest(f=nome_arquivo):
                arquivo_entrada = os.path.join(TEST_DIRECTORY, 'test_images', '%s.png' % nome_arquivo)
                arquivo_saida = os.path.join(TEST_DIRECTORY, 'test_results', '%s_invert.png' % nome_arquivo)
                resultado = pset1.Imagem.carregar(arquivo_entrada).invertida()
                esperado = pset1.Imagem.carregar(arquivo_saida)
                self.assertEqual(resultado,  esperado)

    def test_invertida_peixe(self):
        arquivo_entrada = os.path.join(TEST_DIRECTORY, 'test_images', 'bluegill.png')  # Caminho do peixe
        arquivo_saida = os.path.join(TEST_DIRECTORY, 'test_results', 'bluegill_invertida.png')  # Caminho do resultado do peixe invertido

        imagem = pset1.Imagem.carregar(arquivo_entrada  ) # Carrega o peixe
        imagem_invertida = imagem.invertida()  # Inverte o peixe
        imagem_invertida.salvar(arquivo_saida) # Salva o peixe invertido


        imagem_carregada = pset1.Imagem.carregar(arquivo_saida) # Carrega o peixe invertido
        self.assertEqual(imagem_invertida,imagem_carregada) # Compara o peixe invertido com o peixe invertido carregado


# Classe para os testes dos filtros:
class TestFiltros(unittest.TestCase):


    def test_filtroKernel(self):
        im = pset1.Imagem.carregar('test_images/pigbird.png')
        arquivo_saida = os.path.join(TEST_DIRECTORY, 'test_results', 'pigbirdKernel.png')

        kernel =[
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        resultado = im.correlacao(kernel)

        resultado.salvar(arquivo_saida)

        



    def test_borrada(self):
        for tamanho_kernel in (1, 3, 7):
            for nome_arquivo in ('mushroom', 'twocats', 'chess'):
                with self.subTest(k=tamanho_kernel, f=nome_arquivo):
                    arquivo_entrada = os.path.join(TEST_DIRECTORY, 'test_images', '%s.png' % nome_arquivo)
                    arquivo_saida = os.path.join(TEST_DIRECTORY, 'test_results',
                                                 '%s_blur_%02d.png' % (nome_arquivo, tamanho_kernel))
                    imagem_entrada = pset1.Imagem.carregar(arquivo_entrada)
                    imagem_entrada_copia = pset1.Imagem(imagem_entrada.largura, imagem_entrada.altura,
                                                        imagem_entrada.pixels)
                    resultado = imagem_entrada.borrada(tamanho_kernel)
                    esperado = pset1.Imagem.carregar(arquivo_saida)
                    self.assertEqual(imagem_entrada, imagem_entrada_copia,
                                     "Cuidado para não modificar a imagem original!")
                    self.assertEqual(resultado,  esperado)

    def test_focada(self):
        for tamanho_kernel in (1, 3, 9):
            for nome_arquivo in ('mushroom', 'twocats', 'chess'):
                with self.subTest(k=tamanho_kernel, f=nome_arquivo):
                    arquivo_entrada = os.path.join(TEST_DIRECTORY, 'test_images', '%s.png' % nome_arquivo)
                    arquivo_saida = os.path.join(TEST_DIRECTORY, 'test_results',
                                                 '%s_sharp_%02d.png' % (nome_arquivo, tamanho_kernel))
                    imagem_entrada = pset1.Imagem.carregar(arquivo_entrada)
                    imagem_entrada_copia = pset1.Imagem(imagem_entrada.largura, imagem_entrada.altura,
                                                        imagem_entrada.pixels)
                    resultado = imagem_entrada.focada(tamanho_kernel)
                    esperado = pset1.Imagem.carregar(arquivo_saida)
                    self.assertEqual(imagem_entrada, imagem_entrada_copia,
                                     "Cuidado para não modificar a imagem original!")
                    self.assertEqual(resultado,  esperado)

    def test_bordas(self):
        for nome_arquivo in ('mushroom', 'twocats', 'chess'):
            with self.subTest(f=nome_arquivo):
                arquivo_entrada = os.path.join(TEST_DIRECTORY, 'test_images', '%s.png' % nome_arquivo)
                arquivo_saida = os.path.join(TEST_DIRECTORY, 'test_results', '%s_edges.png' % nome_arquivo)
                imagem_entrada = pset1.Imagem.carregar(arquivo_entrada)
                imagem_entrada_copia = pset1.Imagem(imagem_entrada.largura, imagem_entrada.altura,
                                                    imagem_entrada.pixels)
                resultado = imagem_entrada.bordas()
                esperado = pset1.Imagem.carregar(arquivo_saida)
                self.assertEqual(imagem_entrada, imagem_entrada_copia,
                                 "Cuidado para não modificar a imagem original!")
                self.assertEqual(resultado,  esperado)


if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)

