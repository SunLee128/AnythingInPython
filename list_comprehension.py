answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
answer = []
for person in ["Elie", "Tim", "Matt"]:
    answer.append(person[0])
#answer = ["E", "T", "M"]

answer2 = [val for val in [1, 2, 3, 4, 5, 6] if val % 2 == 0]
answer2 = []
for num in [1, 2, 3, 4, 5, 6]:
    if num % 2 == 0:
        answer2.append(num)
# answer2 = [2,4,6]

answer = [val for val in [1, 2, 3, 4] if val in [3, 4, 5, 6]]
# the slice [::-1] is a quick way to reverse a string
answer = []
for x in [1, 2, 3, 4]:
    if x in [3, 4, 5, 6]:
        answer.append(x)
# answer = [3,4]


answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]
answer2 = []
for name in ["Elie", "Tim", "Matt"]:
    answer2.append(name[::-1].lower())
#answer2 = ['eile','mit','ttam']

# create a list of numbers divisiable by 12 between 1 to 100 inclusive
answer = [i for i in range(1, 101) if i % 12 == 0]

# create a list of consonants from a string
answer = [char for char in "amazing" if char not in "aeiou"]
# answer = ["m","z","n","g"]

answer = [[i for i in range(0, 3)] for num in range(0, 3)]
# answer = [[0,1,2],[0,1,2],[0,1,2]]
answer = [[i for i in range(0, 10)] for num in range(0, 10)]
