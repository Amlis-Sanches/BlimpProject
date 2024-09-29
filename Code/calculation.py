from bouyant_force import *
from graphing_method import *
import numpy as np
import pandas

def main():
    volume:int = 30 #m3
    temp_range:list = [100,300]
    pressure_range:list = [1,100]
    n:int = igl1(P=pressure_range[0],V=volume,T=temp_range[0]) #number of moles is calculated at the starting T and P with the orgiginal volume. n doesn't change
    M:int = 28.96 #grams per mol for air
    pd:int = igl2(P=pressure_range[0],M=M,T=temp_range[0])

    #calculate the Fb with temperature and pressure but assuming volume is changing and density is the same.
    volume_change = pandas.DataFrame(columns=['Temperature', 'Pressure', 'Volume', 'Buoyancy Force'])
    for i in range(temp_range[0],temp_range[1],1):
        #calculate the fb with pressure
        for j in range(pressure_range[0], pressure_range[1],1):
            #calculate volume and bouyant force
            volume:int = igl1(P = j, n=n, T=i)
            Fb:int = buoyant_force(pd=pd,V=volume)

            # Create a dictionary of the current data
            row = {'Temperature': i, 'Pressure': j, 'Volume': volume, 'Buoyancy Force': Fb}

            # Append the row to the DataFrame
            volume_change = volume_change._append(row, ignore_index=True)

    #graph the data from the results
    vol_data = {
    'Volume': volume_change['Volume'].tolist(),
    'Buoyancy Force': volume_change['Buoyancy Force'].tolist()
    }

    plot_data_bokeh(
        data=vol_data,
        x_col='Volume',
        y_col='Buoyancy Force',
        plot_type='line',
        title='Volume vs Fb',
        xlabel='Volume',
        ylabel='Buoyancy Foce',
        output='file',         # Change to 'file'
        filename='plot.html'   # Specify the output file name
    )

    #calculate the Fb with temperature and pressure but assuming volume is the same and density changes.
    density_change = pandas.DataFrame(columns=['Temperature', 'Pressure', 'Volume', 'Buoyancy Force'])

if __name__ == '__main__':
    main()