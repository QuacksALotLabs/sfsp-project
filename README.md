<a id="top"></a>

<div align=center>

![Banner](docs/utils/banner.jpg)

[![Python](https://img.shields.io/badge/_-3.13.5-ff9863?style=flat-square&logo=python&logoColor=white&labelColor=e6805a "python version")](#) [![Django](https://img.shields.io/badge/_-5.2.5-ff9863?style=flat-square&logo=django&logoColor=white&labelColor=e6805a "django version")](#) [![DOCKER](https://img.shields.io/badge/containerized-white?style=flat-square&logo=docker&logoColor=white&labelColor=e6805a&color=ff9863 "build with docker")](#) [![CodeFactor](https://img.shields.io/codefactor/grade/github/SirQuacksAlot/py.django.playground?style=flat-square&logo=devbox&label=%C2%A0&labelColor=e6805a&color=ff9863 "codefactor rating (clickable)")](https://www.codefactor.io/repository/github/sirquacksalot/py.django.playground) [![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/SirQuacksAlot/py.django.playground/.github/workflows/build.yml?style=flat-square&logo=github&label=build&labelColor=e6805a&color=ff9863 "github actions workflow status")](#)


## Python Django Playground

*just a simple playground to get into the django framework*

<br>

[Getting started]() · [Journey]() · [Dokumentation]() · [Lernfortschritt]()

</div>

# 

<br>

This will be my take on the `python` framework `django`. Where I try out things to get in to the guts of it and have a basic under standing of the framework.

This project makes use of [`conventional commits`](https://www.conventionalcommits.org/en/v1.0.0/) like the angular project uses them and describes them in their [`commit message guidlines`](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines).

<br>

## 🛫 Getting started

Docker container setup

```
docker run -it -e DJANGO_ALLOWED_HOSTS=playground.home.arpa -p "3000:3000" django-playground
```

Docker compose setup

```
```

<div align=right>

[back to top ↑](#user-content-top)

</div>

## 🧳 Journey

> *List of stuff I did when working on this logged here to get back later*

- created virtual environemnt `python -m venv env` and activated it `.\env\Scripts\activate`
- created requirements file with `pip freeze > requirements.txt`
- added testing domain to hostfile `127.0.0.1 playground.home.arpa`
- build local image with `docker build -t django-playground .` 

<div align=right>

[back to top ↑](#user-content-top)

</div>

<br>

> Banner image source [www.freepik.com](https://www.freepik.com/free-ai-image/anime-style-portrait-young-student-attending-school_133553028.htm#fromView=keyword&page=1&position=1&uuid=a88d1953-aee4-487f-b4ee-246a311873e8&query=Anime+playground)