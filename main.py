from database_management import *

p1 = Player("Rodrigo", '23', 'lvl-1')
p2 = Player("Jogardor#2", '33', 'lvl-1')
p3 = Player("Jogardor#3", '38', 'lvl-2')
p4 = Player("Jogardor#4", '21', 'lvl-5')
p5 = Player("Jogardor#5", '55', 'lvl-3')
q1 = Court("Gustavo Kuerten Court", "clay")
q2 = Court("Djokovick Court", "grass")
mt = Match()
db = DBManagement()

p1.cadastrar_jogador()
p2.cadastrar_jogador()
p3.cadastrar_jogador()
p4.cadastrar_jogador()
p5.cadastrar_jogador()

q1.cadastrar_quadra()
q2.cadastrar_quadra()

mt.agendar_partida([p1, p2], q1, "2024-05-28", "11:00")
mt.agendar_partida([p2, p1], q2, "2024-05-07", "19:00")
mt.agendar_partida([p2], q2, "2024-05-07", "19:00")
mt.agendar_partida([p1, p2, p3], q2, "2024-05-07", "19:00")
mt.agendar_partida([p1, p2, p3, p4], q1, "2024-05-04", "10:00")
mt.agendar_partida([p1, p2, p3, p4, p5], q1, "2024-05-04", "10:00")


db.select_all_data_from_table('players')
db.select_all_data_from_table('courts')
db.select_all_data_from_table('matches')

