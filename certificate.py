from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

class GeradorCertificado:
    """ Classe utilitária para a criação de certificados """
    DIR_IMAGEM_BASE = "./modelo.png"
    FONT_SMALL      = ImageFont.truetype('./fonts/Roboto-Light.ttf', 15)
    FONT_DEFAULT    = ImageFont.truetype('./fonts/Roboto-Light.ttf', 30)
    FONT_NOME       = ImageFont.truetype('./fonts/Roboto-Light.ttf', 60)

    def __init__(
        self,
        nome:str,
        conteudo:str,
        horas:str,
        minutos:str,
        data:str,
        codigo:str
    ):
        self.nome     = nome
        self.conteudo = conteudo
        self.horas    = horas
        self.minutos  = minutos
        self.data     = data
        self.codigo   = codigo
    
    def get_largura(self, font:ImageFont, text):
        return font.getsize(text)[0]
    
    def __preencher_imagem(self, img):
        certificado_draw = ImageDraw.Draw(img)
        IMAGE_WIDTH, _  = certificado_draw.im.size

        # Escreve tutor
        largura_tutor = self.get_largura(self.FONT_NOME, self.nome)
        certificado_draw.text(
            ((IMAGE_WIDTH-largura_tutor)/2, 450),
            self.nome,
            font=self.FONT_NOME,
            fill="black")
        
        # Escreve conteúdo
        largura_conteudo = self.get_largura(self.FONT_DEFAULT, self.conteudo)
        certificado_draw.text(
            ((IMAGE_WIDTH-largura_conteudo)/2, 680),
            self.conteudo,
            font=self.FONT_DEFAULT,
            fill="black")
        
        # Escreve horas
        largura_horas = self.get_largura(self.FONT_DEFAULT, self.horas)
        certificado_draw.text(
            ((IMAGE_WIDTH-largura_horas-205)/2, 730),
            self.horas,
            font=self.FONT_DEFAULT,
            fill="black")
        
        # Escreve minutos
        largura_minutos = self.get_largura(self.FONT_DEFAULT, self.minutos)
        certificado_draw.text(
            ((IMAGE_WIDTH-largura_minutos+480)/2, 730),
            self.minutos,
            font=self.FONT_DEFAULT,
            fill="black")
        
        # Escreve data
        largura_data = self.get_largura(self.FONT_DEFAULT, self.data)
        certificado_draw.text(
            ((IMAGE_WIDTH-largura_data+120)/2, 785),
            self.data,
            font=self.FONT_DEFAULT,
            fill="black")
        
        # Escreve código
        certificado_draw.text(
            (1220, 970),
            self.codigo,
            font=self.FONT_SMALL,
            fill="black")
            
    def show(self):
        with Image.open(self.DIR_IMAGEM_BASE) as img:
            self.__preencher_imagem(img)
            img.show()
    
    def to_bytes(self) -> BytesIO:
        with Image.open(self.DIR_IMAGEM_BASE) as img:
            self.__preencher_imagem(img)
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            return buffer