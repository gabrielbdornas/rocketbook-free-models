# Rocketbook Modelos Gratuitos

Este repositório contém um script Python para agrupar [modelos gratuitos](https://getrocketbook.com/pages/rocketbook-for-free) de páginas Rocketbook.
utiliza a ferramenta **pdfjam** para manipulação destes arquivos PDF. O principal objetivo é facilitar a criação de documentos com várias páginas em uma única folha, ideal para impressão em formato caderno, aproveitando melhor o espaço.

## Funcionalidade

O script utiliza a ferramenta **pdfjam** para:

- Combinar várias páginas de um PDF em uma única página.
- Ajustar o layout para impressão frente e verso ou lado a lado.
- Escalar o conteúdo do PDF para caber adequadamente na página.

## Exemplo de uso

O script pode ser usado para combinar um único PDF em várias páginas por folha. O comando básico em Python executa:

```python
poetry run task prints
```

O comando acima junta quatro páginas do PDF de entrada em uma única página no formato **A4**, no modo **paisagem**.

## Dependências

- Python 3.12.3.
- pdfjam (instalado em seu sistema).
- [Poetry](https://python-poetry.org/docs/).

## Instalação do pdfjam

Se você não tiver o **pdfjam** instalado, siga as instruções para o seu sistema operacional:

### No Linux:
```bash
sudo apt-get install pdfjam
```

### No macOS:
```bash
brew install pdfjam
```

### No Windows:
Baixe e instale o [pdfjam](http://www.ctan.org/pkg/pdfjam) conforme as instruções para Windows.

## Como usar o script

1. Clone este repositório em sua máquina local.
2. Instale as dependências necessárias (por exemplo, `pdfjam`).
3. Rode o comando `poetry run task prints` se não houver arquivos na pasta `prints` (pasta com arquivos unificados prontos para impressão).
4. Imprima o modelo desejado na pasta `prints` (sugestão de impressão frente e verso).

## Contribuições

Se você quiser contribuir com melhorias para este projeto, fique à vontade para fazer um **fork** e enviar um **pull request**!
