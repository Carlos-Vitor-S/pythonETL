import psycopg2

#Lista para pegar dados das tabelas
listAlunos = []
listProfessores = []
listDisciplinas = []

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
#sk_alu,nome_alu,data_nasc,email,mgp,nk_alu
cursorAlunos = cursor.execute("SELECT mat_alu,nom_alu,dat_nasc,email,mgp FROM alunos",connectionDataSource)
getAlunos = cursor.fetchall()
for row in getAlunos:
    value = row[0],row[1],row[2],row[3],row[4]
    listAlunos.append(value)


#prints testes
print(f"Disciplinas: {listDisciplinas}")
print(f"Professores: {listProfessores}")
print(listAlunos)
print()
'''
cursorProfessor = cursor.execute("SELECT cod_prof, nom_prof, email FROM professores",connectionDataSource)
getDataProfessor = cursor.fetchall()

cursorAlunos = cursor.execute("SELECT mat_alu,dat_nasc, tot_cred, mgp, nom_alu, email FROM alunos" , connectionDataSource)
getDataAlunos = cursor.fetchall();

for row in getDataProfessor:
    #print(row[0])
    value = row[0],row[1],row[2]
    listProfessores.append(value)

for row in getDataAlunos:
    value = row[0], row[1] , row[2] , row[3] , row[4], row[5]
    listAlunos.append(value)

print(listAlunos)
print(listProfessores)'''



