from PIL import Image
import os

# Caminho da pasta com as imagens
caminho = fr'D:\Projetos\converter_png_to_webp\fotos_png'

# Cria pasta de saída (opcional)
saida = fr'D:\Projetos\converter_png_to_webp\fotos_webp'
os.makedirs(saida, exist_ok=True)

# Tipos de arquivos aceitos
extensoes = ['.jpg', '.jpeg', '.png']

# Percorre os arquivos da pasta
for nome_arquivo in os.listdir(caminho):
    nome, ext = os.path.splitext(nome_arquivo)
    if ext.lower() in extensoes:
        caminho_img = os.path.join(caminho, nome_arquivo)
        imagem = Image.open(caminho_img).convert("RGB")

        caminho_saida = os.path.join(saida, f'{nome}.webp')
        imagem.save(caminho_saida, 'webp', quality=80)  # Você pode ajustar a qualidade (0 a 100)

        print(f'Convertido: {nome_arquivo} → {nome}.webp')
