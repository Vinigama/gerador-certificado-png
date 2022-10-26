# Overview

Classe simples desenvolvida para a criação de certificados de conclusão para um projeto pessoal.

Utiliza imagem png como base e faz a escrita utilizando a biblioteca Pillow.

# Como utilizar

- Instalar pacotes utilizando: `pip install -r requirements.txt`
- Utilizar como no exemplo: 
```
from certificate import GeradorCertificado

gerador = GeradorCertificado(
    "Pessoa certificada", # Nome da pessoa certificada
    "Conteúdo postado", # Nome do conteúdo postado
    "2",  # carga de horas
    "30", # carga de minutos
    "12/12/2022", # data de conclusão
    "dasdfasfasfasf" # código para verificação
    )
certificado_io = gerador.to_bytes()

with open("minha_imagem.png", "wb") as f:
    f.write(certificado_io.getbuffer())
    certificado_io.close()
```