import pandas as pd

input = pd.read_csv("user_input.txt", delimiter="|")
output = pd.read_csv("commands.txt", delimiter="|")

final = pd.concat([input, output])

print(input)
