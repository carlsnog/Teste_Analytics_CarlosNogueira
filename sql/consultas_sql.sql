SELECT 
    Produto,
    Categoria,
    valor AS total_vendas
FROM vendas
GROUP BY Produto, Categoria
ORDER BY total_vendas DESC;

-- Esta consulta SQL recupera o total de vendas por produto e categoria, ordenando os resultados do maior para o menor valor de vendas.

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

-- Esta consulta SQL recupera a quantidade vendida, o valor total de vendas e o número de transações para cada produto e categoria no mês de junho de 2023, ordenando os resultados do menor para o maior valor de vendas.

