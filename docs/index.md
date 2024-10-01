# Home

## **Introdução**

Construção de um modelo de Machine Learning para predição de tempo de julgamento de processos judiciais. O projeto utiliza dados reais disponibilizados pelo Conselho Nacional de Justiça - CNJ, por meio da Base Nacional do Poder Judiciário - DataJud. 

## **Objetivos**

- Construção de uma API em Python que realize o Webscrapping dos dados na API do Datajud
- Tratamento dos dados
- Treinamento e deploy de um modelo de Machine Learning
- Consumo desse modelo atraves de uma aplicação FastAPI

## **Tecnologias Utilizadas**

- Python
- FastAPI
- Uvicorn
- Alembic
- Psycopg2-binary
- SqlAlchemy
- Pandas
- Requests
- Scikit-learn
- Pydantic-settings

## **Tutorial de uso**

Pré-requisitos:

- Python, Poetry e Uvicorn 
- *Opcional: Docker*

### **Instalação e Configuração do Ambiente**

1 - Clone este repositório:

```
git clone https://github.com/MLET-007/Dataset-Datajud.git
cd nome-do-projeto
```

---

### **Inicializando o aplicativo**

2 - Execute o aplicativo pelas seguintes formas:

Executando normalmente:
```
uvicorn main:app --reload
```

---

Executando com o Poetry:
```
poetry install
poetry shell

poetry run uvicorn datajud.app:app --reload
```

---

Executando com Docker:
```
docker-compose up -d
```

---

### **Construindo as paginas da documentação**

Para que a documentação do projeto seja executada com sucesso, use o seguinte comando:

```
mkdocs build
```