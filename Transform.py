import datetime
from Extract import listAlunos,listProfessores,listDisciplinas
datetime.datetime
listAlunosTransformada = []
listProfessorTransformada = []
listDisciplinasTransformada = []


nk_alunos = 0
nk_disc = 0
nk_professores = 0

#Transformação da tabela de disciplinas
for index in listDisciplinas:
    nk_disc = index[0]
    values = index[0],index[1],index[2],nk_disc
    listDisciplinasTransformada.append(values)

#Transformação da tabela de professores
for index in listProfessores:
    nk_professores = index[0]
    values = index[0],index[1],nk_professores
    listProfessorTransformada.append(values)

#Transformação da tabela alunos
for index in listAlunos:
    nk_alunos = index[0]
    values = index[0],index[1],index[2],index[3],index[4], nk_alunos
    listAlunosTransformada.append(values)
print(f"lista alunos: {listAlunosTransformada}")
print(f"Disciplinas Transformadas: {listDisciplinasTransformada}")
print(f"Professores Transformados: {listProfessorTransformada}")



'''for index in listAlunos:
    generateNk = index[0]
    listaAlunosTransformada.append(index)
    listaAlunosTransformada.append(generateNk)'''




