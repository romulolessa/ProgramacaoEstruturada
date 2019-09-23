print("Construir um programa que leia a quantidade de alunos do sexo masculino, do sexo feminino e a quantidade de alunos aprovados de uma turma e calcule, armazene e imprima o total de alunos e a porcentagem de alunos do sexo masculino, do sexo feminino e a porcentagem de alunos aprovados.")
alunosm=int(input("Quantidades de alunos do sexo masculino da turma:"))
alunosf=int(input("Quantidades de alunas do sexo feminino da turma:"))
alunos_aprovados=int(input("Quantidade de alunos aprovados: "))

total_alunos= alunosm+alunosf
porcentom=(100*alunosm)/total_alunos
porcentof=(100*alunosf)/total_alunos
procentagem_aprovados=(100*alunos_aprovados)/total_alunos

print("Total de alunos: {:.1f}\nporcentagem de alunos do sexo masculino: {:.1f}\nporcentagem de alunos do sexo feminino: {:.1f}\nporcentagem de alunos aprovados: {:.1f}".format(total_alunos,porcentom, porcentof, procentagem_aprovados))
