"""
SCRIPT DE LIMPEZA E ANÁLISE DE DADOS DE VENDAS
==============================================

FUNCIONALIDADES:
1. Criação de dataset sintético de vendas
2. Limpeza de dados (missing, duplicatas, outliers)
3. Análise de vendas por produto
4. Exportação de resultados
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random


class VendasCriacao:
    """Classe para pipeline de ETL de dados de vendas"""

    def __init__(self, seed=42):
        """Inicializar com seed para reprodutibilidade"""
        np.random.seed(seed)
        random.seed(seed)

        # Configurações de produtos e categorias
        self.produtos = [
            'Notebook Dell Inspiron', 'Mouse Logitech', 'Teclado Mecânico', 'Monitor Samsung 24"',
            'Smartphone Samsung Galaxy', 'iPhone 14', 'Tablet iPad', 'Fones Bluetooth',
            'Carregador USB-C', 'HD Externo 1TB', 'SSD 512GB', 'Cabo HDMI',
            'Caixa de Som JBL', 'Webcam Full HD', 'Impressora HP', 'Roteador Wi-Fi',
            'Pen Drive 64GB', 'Mousepad Gamer', 'Cadeira Gamer', 'Mesa de Escritório'
        ]

        self.categorias = {
            'Notebook Dell Inspiron': 'Computadores',
            'Mouse Logitech': 'Periféricos',
            'Teclado Mecânico': 'Periféricos',
            'Monitor Samsung 24"': 'Monitores',
            'Smartphone Samsung Galaxy': 'Celulares',
            'iPhone 14': 'Celulares',
            'Tablet iPad': 'Tablets',
            'Fones Bluetooth': 'Áudio',
            'Carregador USB-C': 'Acessórios',
            'HD Externo 1TB': 'Armazenamento',
            'SSD 512GB': 'Armazenamento',
            'Cabo HDMI': 'Acessórios',
            'Caixa de Som JBL': 'Áudio',
            'Webcam Full HD': 'Periféricos',
            'Impressora HP': 'Impressoras',
            'Roteador Wi-Fi': 'Rede',
            'Pen Drive 64GB': 'Armazenamento',
            'Mousepad Gamer': 'Periféricos',
            'Cadeira Gamer': 'Móveis',
            'Mesa de Escritório': 'Móveis'
        }

        self.precos_base = {
            'Notebook Dell Inspiron': (2500, 4500),
            'Mouse Logitech': (80, 250),
            'Teclado Mecânico': (200, 800),
            'Monitor Samsung 24"': (800, 1500),
            'Smartphone Samsung Galaxy': (1200, 3000),
            'iPhone 14': (4000, 6000),
            'Tablet iPad': (2000, 4000),
            'Fones Bluetooth': (100, 500),
            'Carregador USB-C': (30, 80),
            'HD Externo 1TB': (300, 600),
            'SSD 512GB': (400, 800),
            'Cabo HDMI': (15, 50),
            'Caixa de Som JBL': (200, 800),
            'Webcam Full HD': (150, 400),
            'Impressora HP': (400, 1200),
            'Roteador Wi-Fi': (150, 500),
            'Pen Drive 64GB': (25, 80),
            'Mousepad Gamer': (50, 200),
            'Cadeira Gamer': (800, 2500),
            'Mesa de Escritório': (600, 1800)
        }

    def gerar_dataset_sintetico(self, n_registros=300):
        """
        Gera dataset sintético de vendas

        Args:
            n_registros (int): Número de registros a gerar

        Returns:
            pandas.DataFrame: Dataset de vendas
        """
        print(f"Gerando dataset sintético com {n_registros} registros...")

        dados = []
        data_inicio = datetime(2023, 1, 1)
        data_fim = datetime(2023, 12, 31)
        dias_total = (data_fim - data_inicio).days + 1

        # Pesos para distribuição realista de produtos
        pesos = [3, 5, 4, 2, 6, 4, 3, 5, 7, 2, 2, 8, 3, 4, 1, 2, 6, 4, 1, 1]

        for i in range(n_registros):
            # Data aleatória
            dias_aleatorio = random.randint(0, dias_total - 1)
            data_venda = data_inicio + timedelta(days=dias_aleatorio)

            # Produto com distribuição ponderada
            produto = random.choices(self.produtos, weights=pesos)[0]
            categoria = self.categorias[produto]

            # Quantidade com distribuição realista
            if random.random() < 0.8:
                quantidade = random.randint(1, 3)
            elif random.random() < 0.95:
                quantidade = random.randint(4, 5)
            else:
                quantidade = random.randint(6, 10)

            # Preço com variação
            preco_min, preco_max = self.precos_base[produto]
            preco = round(random.uniform(preco_min, preco_max), 2)

            dados.append({
                'ID': i + 1,
                'Data': data_venda.strftime('%Y-%m-%d'),
                'Produto': produto,
                'Categoria': categoria,
                'Quantidade': quantidade,
                'Preço': preco
            })

        return pd.DataFrame(dados)

    def introduzir_problemas_qualidade(self, df):
        """
        Introduz problemas de qualidade para emular cenário real e realizar limpeza

        Args:
            df (pandas.DataFrame): Dataset limpo

        Returns:
            pandas.DataFrame: Dataset com problemas introduzidos
        """
        print("Introduzindo problemas de qualidade para demonstração...")

        df_sujo = df.copy()

        # 1. Valores faltantes (~5%)
        n_missing = int(len(df_sujo) * 0.05)
        missing_indices = random.sample(range(len(df_sujo)), n_missing)

        for i in missing_indices[:len(missing_indices)//3]:
            df_sujo.loc[i, 'Quantidade'] = np.nan
        for i in missing_indices[len(missing_indices)//3:2*len(missing_indices)//3]:
            df_sujo.loc[i, 'Preço'] = np.nan
        for i in missing_indices[2*len(missing_indices)//3:]:
            df_sujo.loc[i, 'Categoria'] = np.nan

        # 2. Duplicatas (~3%)
        n_duplicatas = int(len(df_sujo) * 0.03)
        indices_duplicar = random.sample(range(len(df_sujo)), n_duplicatas)

        # pega todas as linhas para duplicar de uma vez
        duplicatas = df_sujo.loc[indices_duplicar].copy()

        # atribui novos IDs sequenciais
        start_id = len(df_sujo) + 1
        duplicatas['ID'] = range(start_id, start_id + len(duplicatas))

        # concatena os duplicados
        df_sujo = pd.concat([df_sujo, duplicatas], ignore_index=True)

        # 3. Outliers de preço
        outlier_indices = random.sample(range(len(df_sujo)), 5)
        for idx in outlier_indices:
            if pd.notna(df_sujo.loc[idx, 'Preço']):
                df_sujo.loc[idx, 'Preço'] *= random.uniform(5, 10)

        return df_sujo


    def executar_pipeline_completo(self, n_registros=300):
        """
        Executa pipeline completo de criação de dataset e emulação de dados contaminados

        Args:
            n_registros (int): Número de registros a gerar
        """
        print("=== PIPELINE CRIAÇÂO DE DADOS DE VENDAS ===\n")

        # 1. Gerar dataset sintético
        df_original = self.gerar_dataset_sintetico(n_registros)

        # 2. Introduzir problemas para demonstração
        df_sujo = self.introduzir_problemas_qualidade(df_original)
        df_sujo.to_csv('data_raw.csv', index=False)
        print(f"Dataset raw salvo: data_raw.csv")

        return df_sujo


if __name__ == "__main__":
    criador = VendasCriacao(seed=42)
    resultados = criador.executar_pipeline_completo(300)
