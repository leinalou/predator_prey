#! /usr/bin/env python3
import math
from datetime import datetime
datetime.now().replace(microsecond=0).isoformat()
import matplotlib.pyplot as plt
def main():
    print('##', datetime.now().replace(microsecond=0).isoformat())
    dt = 0.01
    N0B = 20
    N0W = 2
    #Prey_Growth_Rate = 5
    #Prey_Side_Interaction_Rate = 0.015
    Predator_Side_Interaction_Rate = 0.5
    Predator_Death_Rate = 0.5
    NGen = 4500
    NB_Previous = N0B
    NW_Previous = N0W
    Prey_Growth_Range = 19
    Prey_Death_Range = 19
    print('#from variables:', 'dt=', dt, 'NOB=', N0B, 'NOW=', N0W, 'Prey Death Rate=', Predator_Side_Interaction_Rate, 'Predator Death Rate=',  Predator_Death_Rate, 'NGen =', NGen, 'Prey Growth Rate Range=', Prey_Growth_Range, 'Prey Death Rate=', Prey_Death_Range)

    x1_data_list = []
    y1_data_list = []
    x2_data_list = []
    y2_data_list = []
    x3_data_list = []
    y3_data_list = []
    divergex_list = []
    divergey_list = []
   # color_list = []
    for i in range(Prey_Growth_Range):
        test_list = []
        peak_list = []
       # divergex_list = []
       # divergey_list = []
        Prey_Growth_Rate = ((i+1)/3)
        for n in range(Prey_Death_Range):
            test_list = []
            peak_list = []

            #3divergex_list = []
            #3ivergey_list = []
            Prey_Side_Interaction_Rate = ((n+1)/3)
            for z in range(NGen):
                dNB =(Prey_Growth_Rate * NB_Previous * dt) - (Prey_Side_Interaction_Rate * NB_Previous * NW_Previous * dt)
                NB_New = NB_Previous + dNB
                dNW = (Predator_Side_Interaction_Rate * NB_Previous * NW_Previous* dt) - (Predator_Death_Rate * NW_Previous * dt)
                NW_New = NW_Previous + dNW
                test_list.append(NW_New)
                
                if NB_Previous <= 0:
                    NB_New = 0
                    x1_data_list.append((Prey_Growth_Rate))
                    y1_data_list.append((Prey_Side_Interaction_Rate))
                    break
                else:
                    NB_Previous = NB_New
                if NW_Previous <= 0:
                    NW_New = 0
                    x2_data_list.append((Prey_Growth_Rate))
                    y2_data_list.append((Prey_Side_Interaction_Rate))
                    #color_list.append('2')
                    break
                else:
                    NW_Previous = NW_New
                    
                if len(test_list) == 3:
                    if test_list[1] > test_list[0] and test_list[1] > test_list[2]:
                        peak_list.append(test_list[1])
                    del test_list[0]
                if len(peak_list) >= 3:
                    if peak_list[1] > peak_list[0] and peak_list[2] > peak_list[1]:
                        divergex_list.append((Prey_Growth_Rate))
                        divergey_list.append((Prey_Side_Interaction_Rate))
          
                if z+1 == NGen:
                    x3_data_list.append((Prey_Growth_Rate))
                    y3_data_list.append((Prey_Side_Interaction_Rate))
                    break
            NB_Previous = N0B
            NW_Previous = N0W
            #########################print(divergex_list)
    plt.scatter(x1_data_list, y1_data_list, color = 'red')
    plt.scatter(x2_data_list, y2_data_list, color = 'black')
    plt.scatter(x3_data_list, y3_data_list, color = 'green')
    plt.scatter(divergex_list, divergey_list, color = 'yellow')
   # plt.title('#from variables: dt=' dt 'NOB=' N0B 'NOW=' N0W 'Prey Death Rate=' Prey_Side_Interaction_Rate 'Predator Death Rate=' Predator_Death_Rate' NGen =' NGen 'Prey Growth Rate Range=' Prey_Var_Range 'Predator Growth Rate=' Predator_Var_Range)
 #   for suffix in ('png', 'pdf', 'svg'):
    plot_fname = 'AB1.png'
    #+suffix
    plt.savefig(plot_fname)
    plt.show()
main()

