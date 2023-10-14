import os
import re
import pandas as pd

dir_path = os.path.dirname(os.path.realpath(__file__))

input = []
output = []
for file_name in os.listdir(dir_path):
    if ".txt" not in file_name:
        continue
    print(file_name)
    with open(os.path.join(dir_path, file_name)) as file:
        for line in file.readlines():
            if len(line.strip()) > 0:
                m = re.search("[0-9]*[.].", line)
                print(line, m)
                print(line[m.end(0) - 1 :].split(" -> "))
                command, description = line[m.end(0) - 1 :].split(" -> ")
                input.append(description.strip())
                output.append(command.strip())


pd.DataFrame(input).to_csv(
    os.path.join(dir_path, "input.csv"), index=False, header=False
)
pd.DataFrame(output).to_csv(
    os.path.join(dir_path, "output.csv"), index=False, header=False
)
