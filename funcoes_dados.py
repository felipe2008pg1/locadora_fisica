# ==========================================
# 1. BASE DE DADOS (Lista de Filmes)
# ==========================================
filmes_locadora = [
    # --- AÇÃO ---
    {"titulo": "Vingadores: Ultimato", "ano": 2019, "segmento": "Ação"},
    {"titulo": "Spider-Man: No Way Home", "ano": 2021, "segmento": "Ação"},
    {"titulo": "Vingadores: Guerra Infinita", "ano": 2018, "segmento": "Ação"},
    {"titulo": "The Avengers: Os Vingadores", "ano": 2012, "segmento": "Ação"},
    {"titulo": "Furious 7", "ano": 2015, "segmento": "Ação"},
    {"titulo": "Top Gun: Maverick", "ano": 2022, "segmento": "Ação"},
    {"titulo": "Deadpool & Wolverine", "ano": 2024, "segmento": "Ação"},
    {"titulo": "Black Panther", "ano": 2018, "segmento": "Ação"},
    {"titulo": "Vingadores: Era de Ultron", "ano": 2015, "segmento": "Ação"},
    {"titulo": "Capitão América: Guerra Civil", "ano": 2016, "segmento": "Ação"},
    {"titulo": "Aquaman", "ano": 2018, "segmento": "Ação"},
    {"titulo": "Iron Man 3", "ano": 2013, "segmento": "Ação"},
    {"titulo": "The Dark Knight Rises", "ano": 2012, "segmento": "Ação"},
    {"titulo": "The Dark Knight", "ano": 2008, "segmento": "Ação"},
    {"titulo": "Piratas do Caribe: O Baú da Morte", "ano": 2006, "segmento": "Ação"},
    
    # --- FICÇÃO CIENTÍFICA ---
    {"titulo": "Avatar", "ano": 2009, "segmento": "Ficção Científica"},
    {"titulo": "Avatar: O Caminho da Água", "ano": 2022, "segmento": "Ficção Científica"},
    {"titulo": "Star Wars: O Despertar da Força", "ano": 2015, "segmento": "Ficção Científica"},
    {"titulo": "Jurassic World", "ano": 2015, "segmento": "Ficção Científica"},
    {"titulo": "Star Wars: Os Últimos Jedi", "ano": 2017, "segmento": "Ficção Científica"},
    {"titulo": "Jurassic World: Reino Ameaçado", "ano": 2018, "segmento": "Ficção Científica"},
    {"titulo": "Transformers: O Lado Oculto da Lua", "ano": 2011, "segmento": "Ficção Científica"},
    {"titulo": "Transformers: A Era da Extinção", "ano": 2014, "segmento": "Ficção Científica"},
    {"titulo": "Rogue One: Uma História Star Wars", "ano": 2016, "segmento": "Ficção Científica"},
    {"titulo": "Interestelar", "ano": 2014, "segmento": "Ficção Científica"},

    # --- ANIMAÇÃO ---
    {"titulo": "Divertida Mente 2", "ano": 2024, "segmento": "Animação"},
    {"titulo": "Frozen II", "ano": 2019, "segmento": "Animação"},
    {"titulo": "Super Mario Bros. O Filme", "ano": 2023, "segmento": "Animação"},
    {"titulo": "Frozen: Uma Aventura Congelante", "ano": 2013, "segmento": "Animação"},
    {"titulo": "Incríveis 2", "ano": 2018, "segmento": "Animação"},
    {"titulo": "Minions", "ano": 2015, "segmento": "Animação"},
    {"titulo": "Toy Story 4", "ano": 2019, "segmento": "Animação"},
    {"titulo": "Toy Story 3", "ano": 2010, "segmento": "Animação"},
    {"titulo": "Moana 2", "ano": 2024, "segmento": "Animação"},
    {"titulo": "Procurando Dory", "ano": 2016, "segmento": "Animação"},

    # --- FANTASIA ---
    {"titulo": "O Rei Leão (Live-Action)", "ano": 2019, "segmento": "Fantasia"},
    {"titulo": "Harry Potter e as Relíquias da Morte - Parte 2", "ano": 2011, "segmento": "Fantasia"},
    {"titulo": "A Bela e a Fera (Live-Action)", "ano": 2017, "segmento": "Fantasia"},
    {"titulo": "O Senhor dos Anéis: O Retorno do Rei", "ano": 2003, "segmento": "Fantasia"},
    {"titulo": "Aladdin (Live-Action)", "ano": 2019, "segmento": "Fantasia"},
    {"titulo": "Harry Potter e a Pedra Filosofal", "ano": 2001, "segmento": "Fantasia"},
    {"titulo": "Alice no País das Maravilhas", "ano": 2010, "segmento": "Fantasia"},
    {"titulo": "O Senhor dos Anéis: As Duas Torres", "ano": 2002, "segmento": "Fantasia"},
    {"titulo": "Harry Potter e a Ordem da Fênix", "ano": 2007, "segmento": "Fantasia"},
    {"titulo": "O Senhor dos Anéis: A Sociedade do Anel", "ano": 2001, "segmento": "Fantasia"},

    # --- COMÉDIA / DRAMA / SUSPENSE ---
    {"titulo": "Barbie", "ano": 2023, "segmento": "Comédia/Drama"},
    {"titulo": "Joker (Coringa)", "ano": 2019, "segmento": "Drama/Suspense"},
    {"titulo": "Bohemian Rhapsody", "ano": 2018, "segmento": "Comédia/Drama"},
    {"titulo": "A Origem (Inception)", "ano": 2010, "segmento": "Ficção Científica"},
    {"titulo": "O Lobo de Wall Street", "ano": 2013, "segmento": "Comédia/Drama"}
]


# ==========================================
# 2. FUNÇÃO DE PROCESSAMENTO E EXIBIÇÃO
# ==========================================
def separar_e_exibir(catalogo):
    # Dicionário para agrupar os filmes por segmento
    agrupado = {}
    
    for filme in catalogo:
        segmento = filme["segmento"]
        titulo_ano = f"{filme['titulo']} ({filme['ano']})"
        
        # Se o segmento ainda não existe no dicionário, criamos uma lista nova
        if segmento not in agrupado:
            agrupado[segmento] = []
            
        # Adicionamos o filme dentro da lista do seu respectivo segmento
        agrupado[segmento].append(titulo_ano)
        
    # Exibindo formatado no terminal
    print("=== CATÁLOGO DA LOCADORA SEPARADO POR SEGMENTO ===\n")
    for segmento, filmes in agrupado.items():
        print(f"[{segmento.upper()}] - Total: {len(filmes)} filmes")
        for f in filmes:
            print(f"  • {f}")
        print("-" * 40)


# ==========================================
# 3. CHAMADA DA FUNÇÃO (Execução)
# ==========================================
if __name__ == "__main__":
    separar_e_exibir(filmes_locadora)