import psycopg2

#Lista para pegar dados das tabelas
listAlunos = []
listProfessores = []
listDisciplinas = []
listTurmas = []
listCursos = []
listHistoricoTempo = []
listHistoricoEscolar = []

#criando conexão com o postgres
connectionDataSource = psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "$1790",
    database="dataSource",

)
#criação do cursor para interações com o banco de origem

cursor = connectionDataSource.cursor()

#Extraindo dados da tabela disciplinas

cursorDisciplinas = cursor.execute("SELECT cod_disc,nom_disc,qtd_cred FROM disciplinas", connectionDataSource)
getDisciplinas = cursor.fetchall()
for row in getDisciplinas:
    value = row[0],row[1],row[2]
    listDisciplinas.append(value)

#Extraindo dados da tabela professores

cursorProfessores = cursor.execute("SELECT cod_prof,nom_prof FROM professores", connectionDataSource)
getProfessores = cursor.fetchall()
for row in getProfessores:
    value = row[0],row[1]
    listProfessores.append(value)

# Extraindo dados da tabela alunos

cursorAlunos = cursor.execute("SELECT mat_alu,nom_alu,dat_nasc,email,mgp FROM alunos",connectionDataSource)
getAlunos = cursor.fetchall()
for row in getAlunos:
    value = row[0],row[1],row[2],row[3],row[4]
    listAlunos.append(value)

# Extraindo dados da tabela turmas

cursorTurmas = cursor.execute("SELECT vag_ocup,tot_vagas FROM turmas ",connectionDataSource)
getTurmas = cursor.fetchall()
for row in getTurmas:
    value = row[0],row[1]
    listTurmas.append(value)

#Extraindo dados da tabela cursos
cursorCursos = cursor.execute("SELECT cod_curso,nom_curso,tot_cred FROM cursos",connectionDataSource)
getCursos = cursor.fetchall()
for row in getCursos:
    value = row[0],row[1],row[2]
    listCursos.append(value)

#Extraindo dados da tabela historico para lançar em tempo
cursosHistoricoTempo = cursor.execute("SELECT semestre,ano FROM historicos_escolares GROUP BY 1,2", connectionDataSource)
getHistoricoTempo =  cursor.fetchall()
for row in getHistoricoTempo:
    value = row[0],row[1]
    listHistoricoTempo.append(value)

#Extraindo dados da tabela historico para lançar em fatos
cursosHistoricoEscolar = cursor.execute("SELECT situacao,faltas,media FROM historicos_escolares", connectionDataSource)
getHistoricoEscolar =  cursor.fetchall()
for row in getHistoricoEscolar:
    value = row[0],row[1],row[2]
    listHistoricoEscolar.append(value)
print(listHistoricoEscolar)

#prints testes
print(f"Disciplinas: {listDisciplinas}")
print(f"Professores: {listProfessores}")
print(listAlunos)
print(f"Lista turmas: {listTurmas}")
print(listCursos)
print()



