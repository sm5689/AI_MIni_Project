import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans

data = pd.read_csv('food.csv')

def bmicheck(bmi):
    print("Your body mass index is: ", bmi)
    if ( bmi < 18.5):
        clbmi=0
    elif ( bmi >= 18.5 and bmi < 24.9):
        clbmi = 1
    elif ( bmi >= 25 and bmi < 29.9):
        clbmi=2
    elif ( bmi >= 30 and bmi < 39.9):
        clbmi=3
    return clbmi

# def Weight_Loss(age, veg, weight, height):
def Weight_Loss(bmi):
    # bmi = weight / ((height / 100) ** 2)
    clbmi = bmicheck(bmi)
    x = data[['Calories', 'Sugars']]
    kmeans = KMeans(4)
    kmeans.fit(x)
    identified_clusters = kmeans.fit_predict(x)
    # identified_clusters
    d_w_c = data.copy()
    d_w_c['Clusters'] = identified_clusters
    # plt.scatter(d_w_c['Calories'], d_w_c['Sugars'], c = d_w_c['Clusters'], cmap='rainbow')
    output_df = data
    output_df['cluster'] = identified_clusters
    i = 0
    min = 1000000
    smin = 10000
    for i in range(0, 4):
        res = output_df.loc[output_df['cluster'] == i]
        m = res[['Calories']].mean().item()
        # print(f"Mean = {res[['Calories']].mean().item()}")
        # print(m.value())
        if m < min:
            min = i
        elif m > min and m < smin:
            smin = i
    if clbmi == 0 or clbmi == 1:
        res = output_df.loc[output_df['cluster'] == smin]
    else:
        res = output_df.loc[output_df['cluster'] == min]
    res = res.sort_values(by=['Calories'])
    res_list = res['Food_items'].tolist()
    res_list = res_list[0:10]
    print(res_list)
    return res_list
    # print(res_list)
    # print(res)
    # if veg == 0:
    #     res = output_df.loc[output_df['veg'] == 0]
    # else:
    #     res = output_df.loc[output_df['veg'] == 1]
    # 0 => cal 500, sugar = 50s, 60 (purple)
    # 1 => cal = 150, sugar = 10 (cyan)
    # 2 => cal = <100, sugar = low (yellow)
    # 3 => cal = 300, sugar = 50s (red)
# def Healthy(age, veg, weight, height):
def Weight_Gain(bmi):
    clbmi = bmicheck(bmi)
    z = data[['Sugars', 'Fats', 'Proteins']]
    kmeans = KMeans(4)
    kmeans.fit(z)
    print("finished kmeans")
    identified_clusters = kmeans.fit_predict(z)
    # identified_clusters
    d_w_c = data.copy()
    d_w_c['Clusters'] = identified_clusters
    print(identified_clusters)
    # plt.scatter(d_w_c['Sugars'], d_w_c['Fats'], d_w_c['Proteins'], c=d_w_c['Clusters'], cmap='rainbow')
    output_df = data
    output_df['cluster'] = identified_clusters
    # output_df[['Food_items', 'Sugars', 'Fats', 'Proteins', 'cluster']]
    ans_df = output_df[['Food_items', 'Sugars', 'Fats', 'Proteins', 'cluster']]
    # ans_df.loc[ans_df['cluster'] == 0]
    i = 0
    if clbmi == 0:
        i = 2
    elif clbmi == 1:
        i = 2
    else:
        i = 3
    # res = ans_df.loc[ans_df['cluster'] == i]
    res = output_df.loc[output_df['cluster'] == i]
    if clbmi == 3:
        res = res.sort_values(by=['Calories'])
    else:
        res = res.sort_values(by=['Calories'], ascending = False)
    res_list = res['Food_items'].tolist()
    res_list = res_list[0:10]
    print(res_list)
    return res_list
    # print(res)
def Healthy(bmi):
    clbmi = bmicheck(bmi)
    y = data[['Calories', 'Proteins']]
    kmeans = KMeans(4)
    kmeans.fit(y)
    print('finished kmeans')
    identified_clusters = kmeans.fit_predict(y)
    d_w_c = data.copy()
    d_w_c['Clusters'] = identified_clusters
    output_df = data
    output_df['cluster'] = identified_clusters
    i = 0
    if clbmi == 0:
        i = 3
    else:
        i = 0


    res = output_df.loc[output_df['cluster'] == i]
    res = res.sort_values(by=['Calories'])
    res_list = res['Food_items'].tolist()
    res_list = res_list[0:10]
    print(res_list)
    return res_list


# Weight_Loss(26)
# Weight_Loss(14)
# Weight_Loss(31)
# Weight_Loss(20)
Healthy(26)
Healthy(14)
Healthy(31)
Healthy(20)
# Weight_Gain(26)
# Weight_Gain(14)
# Weight_Gain(31)
# Weight_Gain(20)