T = int(input())

for i in range(T):
    quiz = input()
    score = [0] * len(quiz)
    for j in range(0, len(quiz)):
        if quiz[j] == 'O':
            score[j] = score[j-1] + 1
    print(sum(score))
