import pygame


class Botao:
    def __init__(self, imagem, largura, altura, x, y):
        self.imagem = pygame.image.load(imagem)
        self.imagem = pygame.transform.scale(self.imagem, (largura, altura))
        self.rect = self.imagem.get_rect(center=(x, y))

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)


class Texto:
    def __init__(self, texto, fonte, tamanho, cor, x, y):
        self.fonte = pygame.font.Font(fonte, tamanho)
        self.texto = self.fonte.render(texto, True, cor)
        self.rect = self.texto.get_rect(center=(x, y))

    def desenhar(self, tela):
        tela.blit(self.texto, self.rect)


class App:
    def __init__(self, largura, altura, titulo):
        self.largura = largura
        self.altura = altura
        self.tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption(titulo)

        self.botao1 = Botao("sprites/menu/buttons/button.png", 150, 70, largura // 2, altura // 2)
        self.botao2 = Botao("sprites/menu/buttons/button.png", 150, 70, largura // 2, altura // 2 + 100)

        self.texto1 = Texto("Botão 1", "font/font.otf", 30, (0, 0, 0),
                            self.botao1.rect.centerx, self.botao1.rect.centery)
        self.texto2 = Texto("Botão 2", "font/font.otf", 30, (0, 0, 0),
                            self.botao2.rect.centerx, self.botao2.rect.centery)

    def executar(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.botao1.rect.collidepoint(evento.pos):
                        print("Botão 1 clicado!")
                    elif self.botao2.rect.collidepoint(evento.pos):
                        print("Botão 2 clicado!")

            self.tela.fill((255, 255, 255))
            self.botao1.desenhar(self.tela)
            self.botao2.desenhar(self.tela)
            self.texto1.desenhar(self.tela)
            self.texto2.desenhar(self.tela)

            pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    app = App(800, 600, "Exemplo de Botões Pygame")
    app.executar()
