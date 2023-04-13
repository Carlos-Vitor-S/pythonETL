import psycopg2
from Transform import listDisciplinasTransformada,listProfessorTransformada,listAlunosTransformada

def load():
    connectionDataBase = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="$1790",
    database="controleAcademicoEscola",

    )
    #contadores de commits
    contadorAlunos = 0
    contadorProfessores = 0
    contadorDisciplinas = 0
    print("Banco de Destino conectado com sucesso")
    #cursos para banco de Destino
    cursorDB = connectionDataBase.cursor()
    cursorDB.execute("TRUNCATE  TABLE dm_disciplinas,dm_professores,dm_alunos RESTART IDENTITY CASCADE")

    try:
        #Carga para dimensão dm_disciplinas
        sql = "INSERT into dm_disciplinas (sk_disc,nom_disc,creditos,nk_disc) values (%s, %s, %s,%s)"
        cursorDB.executemany(sql,listDisciplinasTransformada)
        contadorDisciplinas = cursorDB.rowcount
        connectionDataBase.commit()
        #Carga para dimensão dm_professores
        sql = "INSERT into dm_professores (sk_prof,nom_professor,nk_prof) values (%s, %s, %s)"
        cursorDB.executemany(sql,listProfessorTransformada)
        contadorProfessores = cursorDB.rowcount
        connectionDataBase.commit()
        #Carga para dimensão dm_alunos
        sql = "INSERT into dm_alunos (sk_alu,nom_alu,data_nasc,email,mgp,nk_alu) values (%s, %s, %s, %s,%s, %s)"
        cursorDB.executemany(sql, listAlunosTransformada)
        contadorAlunos = cursorDB.rowcount
        connectionDataBase.commit()
    except:
        connectionDataBase.rollback()

    connectionDataBase.commit()
    print(f"Total de Inserções na Tabela dm_disciplinas: {contadorDisciplinas}")
    print(f"Total de Inserções na Tabela dm_professores: {contadorProfessores}")
    print(f"Total de Inserções na Tabela dm_alunos: {contadorAlunos}")
    connectionDataBase.close()




