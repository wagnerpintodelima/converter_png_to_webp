# 🖼️ Conversor de Imagens para WebP

Este script simples e eficiente converte imagens nos formatos `.jpg`, `.jpeg` e `.png` para o formato `.webp`, ideal para otimização de sites e redução do tamanho de arquivos sem perda significativa de qualidade.

## 🚀 Benefícios do WebP

- 📦 Tamanho de arquivo menor em comparação a PNG e JPEG  
- ⚡ Carregamento mais rápido em sites  
- 🧠 Compressão com e sem perdas  
- 🌐 Suporte amplo em navegadores modernos

## 📂 Estrutura do Projeto
Tem duas pastas ali dentro e o nome diz tudo:
- fotos_png
  - Aqui ficam suas fotos originais em .png
- fotos_webp
  -  Aqui é onde ficará as imagens depois de pronto


## 🐍 Requisitos

- Python 3.6 ou superior
- Biblioteca [Pillow](https://python-pillow.org/) instalada

Instale com:

```bash
pip install pillow
```

## 🧠 Modo de uso
- Coloque as fotos png na pasta
- Abra o cmd e entra na pasta do projeto
- Há dois scripts para ser usado:
  - script_with_alpha.py
    - Esse mantém a transparência da imagem, caso haja uma.
    - Um arquivo de 900KB, ficará em torno de uns 400KB
  - script_without_alpha.py
    - Esse não mantém a transparencia, é ideal para imagens que não possuam o fundo transparente
    - Um arquivo de 900KB ficará em torno de 20KB

 - Exemplo
```bash
python script_without_alpha.py
```
Após isso é só pegar suas imagens na pasta foto_webp



## 🤝 Contribuindo

Contribuições são bem-vindas!  
Se você tiver sugestões de melhoria, correções ou novas funcionalidades, sinta-se à vontade para abrir uma _issue_ ou um _pull request_.

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## 📬 Contato

Tem dúvidas ou sugestões? Me chama:

- 💼 [LinkedIn](https://linkedin.com/in/wagner-pinto-de-lima-b36009a8)
- 💻 [Meu Site](https://engenhariadocodigo.com.br/)
- 📧 wagnerdelima2@gmail.com

---

Feito com 🧠, 💻 e ☕ por **Wagner Pinto de Lima**.

