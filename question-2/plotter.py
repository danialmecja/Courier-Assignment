from plotly.offline import plot
data_or_figure = [{"x": [1, 2, 3], "y": [3, 1, 6]}]
plot_, plotdivid, width, height = plot(
    data_or_figure, False, "", True, filename='file.html')
print(plot_)