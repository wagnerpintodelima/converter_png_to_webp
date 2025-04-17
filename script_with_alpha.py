from PIL import Image
import os

# Caminho da pasta com as imagens
caminho = fr'D:\Projetos\ImagensWebp\fotos_png'

# Cria pasta de saída (opcional)
saida = fr'D:\Projetos\ImagensWebp\fotos_webp'
os.makedirs(saida, exist_ok=True)

extensoes = ['.png', '.jpg', '.jpeg']

for nome_arquivo in os.listdir(caminho):
    nome, ext = os.path.splitext(nome_arquivo)
    if ext.lower() in extensoes:
        caminho_img = os.path.join(caminho, nome_arquivo)
        imagem = Image.open(caminho_img)

        # Se a imagem tiver transparência, mantém RGBA
        if imagem.mode in ("RGBA", "LA"):
            imagem = imagem.convert("RGBA")
        else:
            imagem = imagem.convert("RGB")

        caminho_saida = os.path.join(saida, f'{nome}.webp')
        imagem.save(caminho_saida, 'webp', quality=80, lossless=True)

        print(f'Convertido: {nome_arquivo} → {nome}.webp')
