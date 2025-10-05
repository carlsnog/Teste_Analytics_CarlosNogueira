# Consultas SQL - Análise de Vendas

## Consulta 1: Produtos por Valor Total de Vendas

### SQL Query:
```sql
SELECT 
    Produto,
    Categoria,
    valor AS total_vendas
FROM vendas
GROUP BY Produto, Categoria
ORDER BY total_vendas DESC;
```

### Explicação:
Esta consulta lista todos os produtos com seus respectivos valores totais de vendas, ordenados do maior para o menor valor.

### Principais Resultados:
- **iPhone 14** (Celulares): R$ 170.895,92
- **Smartphone Samsung Galaxy** (Celulares): R$ 149.106,72  
- **Tablet iPad** (Tablets): R$ 105.616,38
- **Notebook Dell Inspiron** (Computadores): R$ 26.484,38
- **Monitor Samsung 24"** (Monitores): R$ 24.309,81

---

## Consulta 2: Produtos com Menor Vendas em Junho de 2023

### SQL Query:
```sql
SELECT 
    Produto,
    Categoria,
    SUM(Quantidade) AS quantidade_vendida,
    SUM(Valor) AS valor_total_junho,
    COUNT(*) AS num_transacoes
FROM vendas
WHERE Data LIKE '2023-06%'
GROUP BY Produto, Categoria
ORDER BY quantidade_vendida ASC, valor_total_junho ASC;
```

### Explicação:
Esta consulta identifica os produtos que tiveram as menores vendas especificamente no mês de junho de 2023, filtrando pela data e ordenando pela menor quantidade vendida.

### Produtos com Menor Volume de Vendas em Junho:
1. **Mousepad Gamer** (Periféricos): 1 unidade - R$ 180,48
2. **iPhone 14** (Celulares): 1 unidade - R$ 4.301,66

### Resumo Junho 2023:
- **Total de transações**: 26
- **Quantidade total vendida**: 65 unidades  
- **Valor total**: R$ 63.524,55
- **Produtos distintos**: 16

### Análise:
Embora o iPhone 14 seja o produto com maior receita geral, em junho de 2023 teve baixo volume de vendas (apenas 1 unidade), demonstrando variação sazonal nas vendas de produtos de alto valor.