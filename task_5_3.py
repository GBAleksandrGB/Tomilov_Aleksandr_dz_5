# возможно в задании ошибка: список tutors < списка klasses
# (tutor, None) не выведится

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

for el in tutors:
    if len(tutors) > len(klasses):
        klasses.append(None)

tutors_klasses = zip(tutors, klasses)
# next() присуща генераторам
print(type(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
