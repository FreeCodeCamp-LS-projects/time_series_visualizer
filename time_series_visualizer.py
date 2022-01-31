import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data (we filtered the data as specified)
df = df[
        (df['value']>=df['value'].quantile(0.025)) &
        (df['value']<=df['value'].quantile(0.975))]

#df.index = pd.to_datetime(df.index)


def draw_line_plot():
    # Draw line plot in red
    fig,ax = plt.subplots()
    ax.plot(df.index, df['value'],'r')
    #titles for the graph
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    #organize the data creating new columns
    df['month'] = df.index.month
    df['year'] = df.index.year

    df_bar = df.groupby(['year','month'])['value'].mean()
    #sort the index levels
    df_bar = df_bar.unstack()

    fig=df_bar.plot.bar(legend=True, ylabel='Average Page Views', xlabel='Years').figure
    plt.legend(['January', 'February','March','April','May','June','July','August','September','October','November','December'])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box['num_month']=df_box['date'].dt.month
    df_box=df_box.sort_values('num_month')

    fig,ax = plt.subplots(1,2)
    ax[0]= sns.boxplot(x=df_box['year'], y=df_box['value'], ax=ax[0])
    ax[1]= sns.boxplot(x=df_box['month'], y=df_box['value'], ax=ax[1])

    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
