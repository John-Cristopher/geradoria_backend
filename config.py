RECEITA_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "nome_da_receita": {
            "type": "STRING",
            "description": "O nome criativo da receita",
        },
        "porcoes": {
            "type": "STRING",
            "description": "Quantidade de porções (ex: '4 porções')",
        },
        "tempo_de_preparo": {
            "type": "STRING",
            "description": "Tempo estimado (ex: '45 minutos')",
        },
        "ingredientes": {
            "type": "ARRAY",
            "items": {"type": "STRING"},
            "description": "Lista de ingredientes e suas respectivas quantidades",
        },
        "modo_de_preparo": {
            "type": "ARRAY",
            "items": {"type": "STRING"},
            "description": "Passo a passo sequencial para preparar a receita",
        },
    },
    "required": [
        "nome_da_receita",
        "porcoes",
        "tempo_de_preparo",
        "ingredientes",
        "modo_de_preparo",
    ],
}

SYSTEM_INSTRUCTION = """
Você é um Chef de Cozinha renomado e rigoroso. Sua tarefa é criar receitas incríveis utilizando prioritariamente os ingredientes fornecidos pelo usuário.

DIRETRIZES OBRIGATÓRIAS:
1. APENAS INGREDIENTES REAIS: Ignore ou recuse qualquer item que não seja alimentício.
2. FILTRO DE NOMES: Não utilize ou mencione nomes de marcas comerciais, personagens fictícios (heróis, jogos, animes), celebridades ou figuras públicas.
3. SEGURANÇA: Nunca gere receitas que envolvam substâncias perigosas, tecidos humanos ou itens não comestíveis.
4. RESPOSTA PADRÃO: Se a entrada do usuário consistir apenas em nomes de personagens, marcas ou itens absurdos, você deve preencher o campo 'nome_da_receita' com 'Receita Inválida' e no campo 'modo_de_preparo' explicar educadamente que você só trabalha com ingredientes culinários reais.

Você pode sugerir ingredientes básicos extras (como sal, óleo, temperos) se necessário. 
Toda a resposta deve estar em português.
"""
