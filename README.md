## Projeto

Criar uma API que possibilite criar cartão de datas comemorativas.

## Objetivo

Criar uma pequena API em python com fastapi para exercitar alguns aprendizados da linguagem.

## Configurando ambiente

1. Instale as ferramentas

-   [pyenv](https://github.com/pyenv/pyenv)
-   [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
-   [make](https://www.google.com/search?q=install+make)

2. Garanta que você têm alguns módulos instalados para que o python funcione, alguns deles...

```bash
> sudo apt update
> sudo apt install libssl-dev, openssl-dev, gcc, make, build-essential
```

## Executando local

1. Verifique a versão do python no arquivo python-version e instale se necessário `pyenv install`

2. Crie um virtualenv para o projeto.

```bash
> pyenv virtualenv <python-version> celebration-card-venv
```

3. Ative o virtualenv.

```bash
> pyenv activate celebration-card-venv
```

4. Instale as dependencias.

```
> make dev-dependencies
```

5. Execute o comando

```
> make run
```

## Ambientes

| Ambiente | Url                    |
| -------- | ---------------------- |
| dev      | http://localhost:3000/ |
| homolog  |                        |
| prod     |                        |

## Recursos

### Cadastro de card

Faça uma socitiação `POST /celebration` com os dados abaixo

```json
{
    "of": "João",
    "to": "Maria",
    "description": "Obrigado pelo feedback sobre a reunião"
}
```

### Busca detalhes do card

Faça uma socitiação `GET /celebration/{celebration_id}`

### Deleta um card

Faça uma socitiação `DELETE /celebration/{celebration_id}`

## Importante conhecer

-   [Pypi](https://pypi.org/)
-   [Github actions](https://github.com/marketplace/actions)
-   [Make](https://makefiletutorial.com/)
