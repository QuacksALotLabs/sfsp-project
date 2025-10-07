# Dev Container Environment

This is a dev container environment for the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension for vscode.

## 🧳 Prequisits

1. add `container name` to hosts file pointing to `127.0.0.1`
2. (optional) add `<django projektname>.docker.home.arpa` to hosts file pointing to `127.0.0.1`
3. (optional) create a ssh key for git and add to the python container with:
    ```yml
    volumes:
      - path/to/ssh/keys/:/home/appuser/.ssh/
    ```

## 🛫 Getting started

1. start the dev container (`Crtl+P` -> `> Dev Containers: Rebuild Container`)
2. (first start) run `python manage.py makemigration`, `python manage.py migrate`, `python manage.py collectstatic`
3. run `python manage.py runserver 0.0.0.0:8000` to start testing server instance
4. open [http://api.docker.home.arpa:8000/](http://api.docker.home.arpa:8000/) and [http://api.docker.home.arpa:8000/admin/](http://api.docker.home.arpa:8000/admin/) to test your app.