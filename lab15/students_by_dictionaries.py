# Task: find the name of hier score student:
# student:
# 	name, surname, age, score


def change_age(student, new_age):
	student['age'] = new_age

pesho = {
	'name': 'Petar',
	'surname': 'Petrov',
	'age':23,
	'score': 5
}


maria = {}
maria['name'] = 'Maria'
maria['surnam'] = 'Marieva'
maria['age'] = 32
maria['score'] = 6


change_age(pesho,40)
print(pesho)


# students = [ pesho, maria ]
# hier_score_student = sorted(students,key=lambda d:d['score'],reverse=True)[0]

# print(hier_score_student['name'])









