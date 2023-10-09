import pandas as pd
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

df = pd.DataFrame(data)

total_mujeres = df[df['is_male'] == False].shape[0]
total_hombres = df[df['is_male'] == True].shape[0]

fumadores_mujeres = df[(df['is_male'] == False) & (df['is_smoker'] == True)].shape[0]
fumadores_hombres = df[(df['is_male'] == True) & (df['is_smoker'] == True)].shape[0]

print(f"Total de mujeres: {total_mujeres}, Fumadoras: {fumadores_mujeres}")
print(f"Total de hombres: {total_hombres}, Fumadores: {fumadores_hombres}")
