import matplotlib.pyplot as plt
import pandas as pd


class Plot:
    data_frame = pd.read_json('https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json')

    def draw_plots(self):
        df = pd.DataFrame(self.data_frame, columns=['name', 'gt_corners', 'rb_corners', 'mean', 'max', 'min',
                                                    'floor_mean', 'floor_max', 'floor_min', 'ceiling_mean',
                                                    'ceiling_max', 'ceiling_min'])

        df.plot(x='max', y='min', kind='scatter', figsize=(10, 10), title='Max-min')
        plt.savefig('plots/Max-min.png', dpi=100)                                       # columns: Max-min

        df.plot(x='floor_max', y='ceiling_max', kind='scatter', figsize=(10, 10), title='FloorMax-CeilingMax')
        plt.savefig('plots/FloorMax-CeilingMax.png', dpi=100)               # columns: FloorMax-CeilingMax

        df.plot(x='mean', y='floor_mean', kind='scatter', figsize=(10, 10), title='Mean-Floor_mean')
        plt.savefig('plots/Mean-Floor_mean.png', dpi=100)                       # columns: Mean-Floor_mean

        df.plot(x='mean', y='ceiling_mean', kind='scatter', figsize=(10, 10), title='Mean-Ceiling_mean')
        plt.savefig('plots/Mean-Ceiling_mean.png', dpi=100)                   # columns: Mean-Ceiling_mean

        df.plot(x='floor_mean', y='ceiling_mean', kind='scatter', figsize=(10, 10), title='FloorMean-CeilingMean')
        plt.savefig('plots/FloorMean-CeilingMean.png', dpi=100)           # columns: FloorMean-CeilingMean

        df.plot(x='floor_max', y='ceiling_min', kind='scatter', figsize=(10, 10), title='FloorMax-CeilingMin')
        plt.savefig('plots/FloorMax-CeilingMin.png', dpi=100)               # columns: FloorMax-CeilingMin

        df.plot(x='floor_min', y='ceiling_max', kind='scatter', figsize=(10, 10), title='FloorMin-CeilingMax')
        plt.savefig('plots/FloorMin-CeilingMax.png', dpi=100)               # columns: FloorMin-CeilingMax


call_plots = Plot()
call_plots.draw_plots()
