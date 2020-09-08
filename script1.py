from pandas_datareader import data
import datetime
from bokeh.plotting import figure
from bokeh.io import show, output_file
from bokeh.models.annotations import Title
from bokeh.embed import components


start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2019, 12, 31)
df = data.DataReader(name= 'GOOG', data_source='yahoo', start= start, end= end)

def inc_dec(c, o):
    if c > o:
        return "Increase"
    elif c < o:
        return "Decrease"
    else:
        return "Equal"

df['Status'] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
df['Middle'] = (df.Open + df.Close)/2
df['Height'] = abs(df.Open - df.Close)

p = figure(x_axis_type= 'datetime', width= 1000, height= 500)
p.title = Title(text= 'CandleStick Chart')
hours_12 = 12 * 60 * 60 * 1000

p.segment(df.index, df.High, df.index, df.Low, color= 'Black')

p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"], hours_12, df.Height[df.Status == "Increase"], fill_color= 'green')
p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"], hours_12, df.Height[df.Status == "Decrease"], fill_color= 'red')

components(p)

#output_file('Graph.html') 
show(p)