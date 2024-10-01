# Endpoints

Para testar os endpoints citados abaixo, clique em [Swagger](http://localhost:8000/docs) para ser redirecionado para a documentação automatica feita pelo FastAPI

## **Listagem de Endpoints**

- Extração e gravação dos dados
- Predição do modelo

### **Extração e gravação dos dados**

`GET` - **`/import`** 

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

Exemplo de resposta:

```
    "Resposta de predição"
```

Códigos da Resposta

| Código | Descrição                            |
|--------|--------------------------------------|
|200     | Resposta de predição |
|500     | An error occurred during prediction |