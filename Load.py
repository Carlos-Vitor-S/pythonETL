import psycopg2
from Extract import listProfessores

def load():
    connectionDataBase = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="$1790",
    database="escolaETL",

    )
    print("conectou")
    cursor = connectionDataBase.cursor()
    #contadores de commits

    contadorAlunos = 0
    contadorProfessores = 0

    try:
        #carga para dimensão professores
        sql = "INSERT into dm_professores (sk_prof,nom_prof,email) values (%s, %s, %s)"
        cursor.executemany(sql, listProfessores)
        contadorProfessores = cursor.rowcount
        connectionDataBase.commit()
        # carga para dimensão alunos

    except:
        connectionDataBase.rollback()

    connectionDataBase.commit()
    print(f"Dados do Professores Inseridos: {contadorProfessores}")
    connectionDataBase.close()




