<a id="top"></a>

<div align=center>

![Banner](.docs/assets/banner.jpg)

[![Python](https://img.shields.io/badge/_-3.13.5-ff9863?style=flat-square&logo=python&logoColor=white&labelColor=e6805a "python version")](#) [![Django](https://img.shields.io/badge/_-5.2.5-ff9863?style=flat-square&logo=django&logoColor=white&labelColor=e6805a "django version")](#) [![DOCKER](https://img.shields.io/badge/containerized-white?style=flat-square&logo=docker&logoColor=white&labelColor=e6805a&color=ff9863 "build with docker")](#) [![CodeFactor](https://img.shields.io/codefactor/grade/github/QuacksALotLabs/sfsp-project?style=flat-square&logo=devbox&label=%C2%A0&labelColor=e6805a&color=ff9863 "codefactor rating (clickable)")](https://www.codefactor.io/repository/github/QuacksALotLabs/sfsp-project) [![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/SirQuacksAlot/py.django.playground/.github/workflows/build.yml?style=flat-square&logo=github&label=build&labelColor=e6805a&color=ff9863 "github actions workflow status")](#)


## Simple file sharing project

*just a simple playground to get into the django framework*

<br>

[Getting started](#-getting-started) · [Get on developing](#️-get-on-developing) · [Dokumentation]()

</div>

# 

<br>

This will be my take on the `python` framework `django`. Where I try out things to get in to the guts of it and have a basic under standing of the framework.

This project makes use of [`conventional commits`](https://www.conventionalcommits.org/en/v1.0.0/) like the angular project uses them and describes them in their [`commit message guidlines`](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines).

The idea is to have a simple file sharing service which saves all uploads to a s3 bucket and tag uploads to make them unique. It will use hsmw session for authentication and be available as a docker container for arm and x86 plattforms.

<br>

## 🛫 Getting started

Docker run setup

```bash

```

Docker compose setup

```bash

```

## ⌨️ Get on developing

### dev container

- take a look on dev [containers information](.devcontainer/README.md)

### local development

1. install python 3.13 `winget install python.python313`
2. clone the repo `git clone git@github.com:QuacksALotLabs/sfsp-project.git`
3. created virtual environemnt `python -m venv .venv` and activated it `.\.venv\Scripts\activate`
4. updated package manager `python.exe -m pip install --upgrade pip`
5. install requirements `python -m pip install -r requirements.txt`
6. get on coding 👌

<div align=right>

[back to top ↑](#user-content-top)

</div>

## 🧳 Features

- [ ] 🧑‍🎓 hsmw session auth
  - [ ] 🔐 jwt sessions (optinal)
- [ ] 💾 s3 bucket upload
  - [ ] 🪧 upload tagging
- [ ] 📦 containerization
  - [ ] arm support
  - [ ] x86 support
  - [x] github action cicd automation

<br>

> Banner image source [www.freepik.com](https://www.freepik.com/free-ai-image/anime-style-portrait-young-student-attending-school_133553028.htm#fromView=keyword&page=1&position=1&uuid=a88d1953-aee4-487f-b4ee-246a311873e8&query=Anime+playground)