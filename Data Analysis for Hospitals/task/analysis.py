import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 8)

general = pd.read_csv('./test/general.csv')
prenatal = pd.read_csv('./test/prenatal.csv')
sports = pd.read_csv('./test/sports.csv')

prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

un = pd.concat([general, prenatal, sports], ignore_index=True)
un.drop(columns='Unnamed: 0', inplace=True)
un = un[un.isna().sum(axis=1) < 14]
un.loc[(un['gender'] == 'male') | (un['gender'] == 'man'), 'gender'] = 'm'
un.loc[(un['gender'] == 'female') | (un['gender'] == 'woman'), 'gender'] = 'f'
un.loc[(un['hospital'] == 'prenatal') & (un['gender'].isna()), 'gender'] = 'f'
un[['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']]=un[['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']].fillna(value=0)

#print(un.hospital.value_counts().idxmax())
#print(((un[un.hospital == 'general'].diagnosis.value_counts().loc['stomach'])/(un[un.hospital == 'general'].diagnosis.count())).round(3))
#print(((un[un.hospital == 'sports'].diagnosis.value_counts().loc['dislocation'])/(un[un.hospital == 'sports'].diagnosis.count())).round(3))
#print(un[un.hospital == 'general'].age.median()-un[un.hospital == 'sports'].age.median())
#print(un[un.blood_test == 't'].groupby(['hospital']).blood_test.count().idxmax(), un[un.blood_test == 't'].groupby(['hospital']).blood_test.count().loc[un[un.blood_test == 't'].groupby(['hospital']).blood_test.count().idxmax()], sep=",")

un.plot(y=['age'],kind='hist', bins=[0, 15, 35, 55, 70, 80])
print('The answer to the 1st question:','15-35')
plt.show()
plt.pie(un['diagnosis'].value_counts())
print('The answer to the 2nd question:','pregnancy')
plt.show()
plt.violinplot([un[un['hospital']=='general'].height,un[un['hospital']=='prenatal'].height,un[un['hospital']=='sports'].height], showextrema=True, showmeans=True, showmedians=True)
print('The answer to the 13rd question:','It is because sport hospital does not uses metric system.')
plt.show()


