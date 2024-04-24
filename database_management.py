import sqlite3 as lite


class DBManagement:
    def __init__(self):
        self.conn = lite.connect('clube_tenis.db')
        self.c = self.conn.cursor()
        # self.c.execute('''DROP TABLE IF EXISTS players ''')
        # self.c.execute('''DROP TABLE IF EXISTS courts ''')
        # self.c.execute('''DROP TABLE IF EXISTS matches ''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS players
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, skill TEXT)''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS courts
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, type TEXT)''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS matches
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, player_1 TEXT, player_2 TEXT, player_3 TEXT, 
                          player_4 TEXT, quadra TEXT, schedule_date TEXT, schedule_time TEXT)''')
        self.conn.commit()

    def select_all_data_from_table(self, table):
        query = f''' select * from {table} '''
        self.c.execute(query)
        linhas = self.c.fetchall()
        if table == 'matches':
            print("AGENDAMENTOS: ")
        elif table == 'courts':
            print("QUADRAS: ")
        elif table == 'players':
            print("JOGADORES: ")
        for linha in linhas:
            print(linha)


class Player(DBManagement):
    def __init__(self, name, age, skill):
        super().__init__()
        self.name = name
        self.age = age
        self.skill = skill

    def cadastrar_jogador(self):
        self.c.execute("INSERT INTO players (name, age, skill) VALUES (?, ?, ?)",
                       (self.name, self.age, self.skill))
        self.conn.commit()
        player_id = self.c.lastrowid  # Obtém o ID do jogador inserido

        return player_id


class Court(DBManagement):
    def __init__(self, name, court_type):
        super().__init__()
        self.name = name
        self.type = court_type

    def cadastrar_quadra(self):
        self.c.execute("INSERT INTO courts (name, type) VALUES (?, ?)", (self.name, self.type))
        self.conn.commit()


class Match(DBManagement):
    def __init__(self):
        super().__init__()

    # def agendar_partida(self, players: list, court, schedule_date, schedule_time):
    def agendar_partida(self, players: list, court, schedule_date, schedule_time):
        if len(players) <= 1:
            print('Não pode agendar com um único jogador.')
        elif len(players) == 2:
            lista_valores = list()
            lista_valores.append(players[0].name)
            lista_valores.append(players[1].name)
            lista_valores.append(court.name)
            lista_valores.append(schedule_date)
            lista_valores.append(schedule_time)
            sql = "INSERT INTO matches (player_1, player_2, quadra, schedule_date, schedule_time) VALUES (?, ?, ?, ?, ?)"
            self.c.execute(sql, tuple(lista_valores))

        elif len(players) == 3:
            lista_valores = list()
            lista_valores.append(players[0].name)
            lista_valores.append(players[1].name)
            lista_valores.append(players[2].name)
            lista_valores.append(court.name)
            lista_valores.append(schedule_date)
            lista_valores.append(schedule_time)
            sql = "INSERT INTO matches (player_1, player_2, player_3, quadra, schedule_date, schedule_time) VALUES (?, ?, ?, ?, ?, ?)"
            self.c.execute(sql, tuple(lista_valores))


        elif len(players) == 4:
            lista_valores = list()
            lista_valores.append(players[0].name)
            lista_valores.append(players[1].name)
            lista_valores.append(players[2].name)
            lista_valores.append(players[3].name)
            lista_valores.append(court.name)
            lista_valores.append(schedule_date)
            lista_valores.append(schedule_time)
            sql = "INSERT INTO matches (player_1, player_2, player_3, player_4, quadra, schedule_date, schedule_time) VALUES (?, ?, ?, ?, ?, ?, ?)"
            self.c.execute(sql, tuple(lista_valores))

        elif len(players) > 4:
            print('Não é possível agendar com mais de 4 jogadores')

        self.conn.commit()
