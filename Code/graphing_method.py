from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource
import pandas as pd

def main():
    # Sample data dictionary
    data_dict = {
        'Time': [0, 1, 2, 3, 4, 5],
        'Velocity': [0, 10, 20, 15, 25, 30]
    }

    # Plotting the data
    plot_data_bokeh(
        data=data_dict,
        x_col='Time',
        y_col='Velocity',
        plot_type='line',
        title='Velocity vs. Time',
        xlabel='Time (s)',
        ylabel='Velocity (m/s)',
        output='file',         # Change to 'file'
        filename='plot.html'   # Specify the output file name
    )

def plot_data_bokeh(
    data, x_col, y_col, plot_type='line', title=None,
    xlabel=None, ylabel=None, output='file', filename='plot.html'
    ):
    # Validate and prepare the data
    if isinstance(data, dict):
        df = pd.DataFrame(data)
    elif isinstance(data, pd.DataFrame):
        df = data
    else:
        raise TypeError("Data must be a dictionary or a pandas DataFrame.")

    # Check if the specified columns exist
    if x_col not in df.columns:
        raise ValueError(f"Column '{x_col}' not found in data.")
    if y_col not in df.columns:
        raise ValueError(f"Column '{y_col}' not found in data.")

    # Prepare the data source
    source = ColumnDataSource(df)

    # Output options
    if output == 'file':
        output_file(filename)
    else:
        raise ValueError("For script execution, output must be 'file'.")

    # Create a new plot with a title and axis labels
    p = figure(title=title, x_axis_label=xlabel or x_col, y_axis_label=ylabel or y_col,
               tools="pan,wheel_zoom,box_zoom,reset,save", tooltips=f"@{x_col}, @{y_col}")

    # Add the appropriate glyph
    if plot_type == 'line':
        p.line(x=x_col, y=y_col, source=source, legend_label=y_col, line_width=2)
    elif plot_type == 'circle':
        p.circle(x=x_col, y=y_col, source=source, legend_label=y_col, size=8)
    elif plot_type == 'scatter':
        p.scatter(x=x_col, y=y_col, source=source, legend_label=y_col, marker='circle', size=8)
    elif plot_type == 'bar':
        p.vbar(x=x_col, top=y_col, source=source, width=0.9)
    else:
        raise ValueError(f"Plot type '{plot_type}' is not supported.")

    # Customize plot
    p.legend.location = "top_left"
    p.legend.click_policy = "hide"

    # Show the results
    show(p)

if __name__ == '__main__':
    main()
