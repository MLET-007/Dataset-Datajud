# Endpoints

Para testar os endpoints citados abaixo, clique em [Swagger](http://localhost:8000/docs) para ser redirecionado para a documentação automatica feita pelo FastAPI

## **Listagem de Endpoints**

- Extração e gravação dos dados
- Predição do modelo

### **Extração e gravação dos dados**

`POST` - **`/import/csv`** 

Importa os dados pelo arquivo .csv
Exemplo de resposta:

```
    "Data imported successfully"
```

Códigos da Resposta

| Código | Descrição                            |
|--------|--------------------------------------|
|200     | Data imported successfully |
|500     | Error during data import |

---

`POST` - **`/import/api`** 

Importa os dados pela API do Datajud
Exemplo de resposta:

```
    "Data imported successfully"
```

Códigos da Resposta

| Código | Descrição                            |
|--------|--------------------------------------|
|200     | Data imported successfully |
|500     | Error during data import |

---

### **Predição do modelo**

`POST` - **`/predict`**

Endpoint de predição do modelo de acordo com os dados enviados
Exemplo de resposta:

```
    "Entre 181 a 365 dias"
```

Códigos da Resposta

| Código | Descrição                            |
|--------|--------------------------------------|
|200     | Resposta de predição |
|500     | An error occurred during prediction |