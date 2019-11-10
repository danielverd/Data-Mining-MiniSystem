import pandas as pd
from unidecode import unidecode

salaries = pd.read_csv('NBA Salaries 201819.csv')
stats = pd.read_csv('NBA Stats_201819.csv')
experience = pd.read_csv('NBA Experience 201819.csv')

repeats = stats.loc[stats['Tm'] == 'TOT']
for index, row in repeats.iterrows():
    stats.drop(stats[(stats['Player'] == row['Player']) & (stats['Tm'] != 'TOT')].index, inplace=True)
experience.drop_duplicates(subset='Player',keep='first',inplace=True)

experience['Player'] = experience['Player'].apply(unidecode)
stats['Player'] = stats['Player'].apply(unidecode)
salaries['Player'] = salaries['Player'].map(lambda x: x.strip())

experienceAndStats = pd.merge(experience,stats,on='Player')
experienceSalaryAndStats = pd.merge(experienceAndSalary,salaries,on='Player')

del experienceSalaryAndStats['Pos_y']
experienceSalaryAndStats.rename(columns={'Pos_x': 'Pos'}, inplace=True)
print(experienceSalaryAndStats.head())

experienceSalaryAndStats.to_csv('NBA Player Data 201819.csv')