import sqlite3
from modelo import Pessoa, Marca, Veiculo

banco = sqlite3.connect('database.db')
banco.execute("PRAGMA foreign_keys=on")
cursor = banco.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Pessoa(
                cpf INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                nascimento DATE NOT NULL,
                oculos BOOLEAN NOT NULL
                );''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Marca(
                id INTEGER NOT NULL,
                nome TEXT NOT NULL,
                sigla CHARACTER(2) NOT NULL,
                PRIMARY KEY(id)           
);''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Veiculo(
                placa CHARACTER(7) NOT NULL,
                ano INTEGER NOT NULL,
                cor TEXT NOT NULL,
                proprietario INTEGER NOT NULL,
                marca INTEGER NOT NULL,
                PRIMARY KEY(placa),
                FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                FOREIGN KEY(marca) REFERENCES Marca(id));''')
#cursor.execute('''ALTER TABLE Veiculo ADD motor REAL;''')
#pessoa=Pessoa(22993083898998, 'pedro', '2000-01-31', True)
#comando = '''insert into Pessoa(cpf, nome, nascimento, oculos) values'''
#cursor.execute(comando,(pessoa.cpf,pessoa.nome,pessoa.nascimento,pessoa.usa_oculos))
pessoas= [Pessoa(122342356745, 'joao', ' 2000-01-31', True  ), Pessoa(102938302089, 'cynthia', '1995-03-10',False)]
comando= '''INSERT INTO Pessoa(cpf, nome, nascimento, oculos) values (?,?,?,?); '''
#cursor.executemany(comando,[(i.cpf, i.nome,i.nascimento,i.usa_oculos) for i in pessoas])
#adicionando marca
comando= '''insert into Marca (nome, sigla) values (:nome, :sigla)'''
marcaA= Marca('Marca A', 'MA')
cursor.execute(comando, vars(marcaA))
marcaA.id = cursor.lastrowid
marcaB= Marca("Marca B", "MB")
cursor.execute(comando, vars(marcaB))
marcaB.id= cursor.lastrowid
#adicionar veiculo
comando1= '''insert into Veiculo(placa, ano, cor, motor, proprietario, marca) values (:placa, :ano, :cor, :motor, :proprietario, :marca);'''
veiculo1= Veiculo("AAABBB01", '2001', 'prata', 1.0, 122342356745, marcaA.id )
cursor.execute(comando1, vars(veiculo1))
banco.commit()
cursor.close()
banco.close