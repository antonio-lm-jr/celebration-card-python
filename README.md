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

## Importante conhecer

-   [Pypi](https://pypi.org/)
-   [Github actions](https://github.com/marketplace/actions)
-   [Make](https://makefiletutorial.com/)
