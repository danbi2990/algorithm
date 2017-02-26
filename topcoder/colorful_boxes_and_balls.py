numRed, numBlue, onlyRed, onlyBlue, bothColors = map(int,input().split())
a = numRed * onlyRed + numBlue * onlyBlue
b = min(numRed, numBlue)*2*bothColors + (numRed-numBlue)*(onlyRed if numRed > numBlue else -1*onlyBlue)
print(max(a, b))
