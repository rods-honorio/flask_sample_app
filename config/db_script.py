import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='M4n43lf0v41!', host='127.0.0.1', port=3306)

conn.cursor().execute("DROP DATABASE `sample`;")
conn.commit()
conn.cursor().close()

cursor = conn.cursor()

set_names = '''SET NAMES UTF8MB4;'''

conn.cursor().execute(set_names)
conn.commit()
conn.cursor().close()

criar_esquema = '''
    CREATE DATABASE `sample` /*!40100 DEFAULT CHARACTER SET UTF8MB4 COLLATE utf8mb4_bin */;
'''

conn.cursor().execute(criar_esquema)
conn.commit()
conn.cursor().close()

use_database = '''USE `sample`;'''

conn.cursor().execute(use_database)
conn.commit()
conn.cursor().close()

criar_tabela = '''
    CREATE TABLE `sample_a` (
      `id_field_a` int(11) NOT NULL AUTO_INCREMENT,
      `text_field_a` varchar(50) COLLATE utf8_bin NOT NULL,
      `numeric_field_a` int(11) COLLATE utf8_bin NOT NULL,
      `date_field_a` date NOT NULL,
      PRIMARY KEY (`id_field_a`)
    ) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=utf8mb4_bin;
    '''

conn.cursor().execute(criar_tabela)
conn.commit()
conn.cursor().close()

criar_tabela = '''
    CREATE TABLE `sample_b` (
      `id_field_b` int(11) NOT NULL AUTO_INCREMENT,
      `id_field_a` int(11) COLLATE utf8_bin NOT NULL,
      `text_field_b` varchar(50) NOT NULL,
      PRIMARY KEY (`id_field_b`),
      CONSTRAINT `fk_id_field_a` FOREIGN KEY (`id_field_a`) 
      REFERENCES `sample_a` (`id_field_a`)
    ) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=utf8mb4_bin;
'''

conn.cursor().execute(criar_tabela)
conn.commit()
conn.cursor().close()

criar_tabela = '''
    CREATE TABLE `users` (
      `username` varchar(8) COLLATE utf8_bin NOT NULL,
      `name` varchar(20) COLLATE utf8_bin NOT NULL,
      `password` varchar(8) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`username`)
    ) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=utf8mb4_bin;
'''

conn.cursor().execute(criar_tabela)
conn.commit()
conn.cursor().close()

# inserting users
cursor.executemany(
      'INSERT INTO sample.users (username, name, password) VALUES (%s, %s, %s)',
      [
            ('rods', 'The Raccoon', 'flask'),
            ('noob', 'Nubinha', 'senha'),
      ])
conn.commit()
conn.cursor().close()

cursor.execute('select * from sample.users')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserting sample a
cursor.executemany(
      'INSERT INTO sample.sample_a (text_field_a, numeric_field_a, date_field_a) VALUES (%s, %s, %s)',
      [
            ('Sample Value A 1', '1', '2001-01-01'),
            ('Sample Value A 2', '2', '2002-02-02'),
            ('Sample Value A 3', '3', '2003-03-03'),
            ('Sample Value A 4', '4', '2004-04-04'),
      ])
conn.commit()
conn.cursor().close()

cursor.execute('select * from sample.sample_a')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])
conn.cursor().close()

# inserting sample b
cursor.executemany(
      'INSERT INTO sample.sample_b (id_field_a, text_field_b) VALUES (%s, %s)',
      [
            ('1', 'Sample Value B 1'),
            ('1', 'Sample Value B 2'),
            ('2', 'Sample Value B 3'),
            ('2', 'Sample Value B 4'),
      ])
conn.commit()
conn.cursor().close()

cursor.execute('select * from sample.sample_a')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# commiting
conn.commit()
conn.cursor().close()