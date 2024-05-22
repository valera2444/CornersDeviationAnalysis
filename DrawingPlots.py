import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class DrawPlots:
    def __save_figure(self, dest):
        plt.savefig(dest)
        plt.clf()

    def __draw_hists_corners(self, data):

        plt.hist(data[data.rb_corners == 4]['mean'],
                 color='red', label='4 corners', bins=75)
        plt.hist(data[data.rb_corners == 6]['mean'],
                 color='green', label='6 corners', bins=75)
        plt.hist(data[data.rb_corners == 8]['mean'],
                 color='blue', label='8 corners', bins=75)
        plt.hist(data[data.rb_corners == 10]['mean'],
                 color='yellow', label='10 corners', bins=75)
        plt.legend()
        self.__save_figure('plots/hist_means.png')
        return ['plots/hist_means.png']

    def __draw_hists_floor_ceil(self, data):
        plt.hist(data.ceiling_mean, color='green', label='ceiling mean', alpha=0.5, bins=50)
        plt.hist(data.floor_mean,color='red', label='floor_mean', alpha = 0.5, bins=50)
        plt.legend()
        self.__save_figure('plots/hist_floor_ceil_mean.png')

        plt.hist(data.ceiling_max, color='green', label='ceiling max', alpha=0.5, bins=50)
        plt.hist(data.floor_max, color='red', label='floor_max', alpha=0.5, bins=50)
        plt.legend()
        self.__save_figure('plots/hist_floor_ceil_max.png')

        plt.hist(data.ceiling_min, color='green', label='ceiling min', alpha=0.5, bins=50)
        plt.hist(data.floor_min, color='red', label='floor_min', alpha=0.5, bins=50)
        plt.legend()
        self.__save_figure('plots/hist_floor_ceil_min.png')
        return ['plots/hist_floor_ceil_mean.png','plots/hist_floor_ceil_max.png','plots/hist_floor_ceil_min.png']

    def __draw_heatmap(self, data):
        fig, ax = plt.subplots(figsize=(10, 10))
        sns.heatmap(data.iloc[:, 1:].reset_index(drop=True).corr(), annot=True,ax=ax)
        fig.savefig('plots/sns_heatmap.png')
        plt.clf()
        return ['plots/sns_heatmap.png']

    def __draw_boxplot(self, data):
        fig, ax = plt.subplots(1,4)
        ax[0].boxplot(data[data.gt_corners==4].floor_max)
        ax[1].boxplot(data[data.gt_corners==6].floor_max)
        ax[2].boxplot(data[data.gt_corners == 8].floor_max)
        ax[3].boxplot(data[data.gt_corners==10].floor_max)
        self.__save_figure('plots/box_plot_floor_max.png')
        fig, ax = plt.subplots(1, 4)
        ax[0].boxplot(data[data.gt_corners == 4].floor_min)
        ax[1].boxplot(data[data.gt_corners == 6].floor_min)
        ax[2].boxplot(data[data.gt_corners == 8].floor_min)
        ax[3].boxplot(data[data.gt_corners == 10].floor_min)
        self.__save_figure('plots/box_plot_floor_min.png')
        return ['plots/box_plot_floor_max.png', 'plots/box_plot_floor_min.png']

    def __draw_boxplot_means_corners(self, data):
        fig, ax = plt.subplots(1,3)
        ax[0].boxplot(data[data.gt_corners==4]['mean'])
        ax[0].set_title('4 corners')
        ax[1].boxplot(data[data.gt_corners == 6]['mean'])
        ax[1].set_title('6 corners')
        ax[2].boxplot(data['mean'])
        ax[2].set_title('all rooms')
        self.__save_figure('plots/box_plot_corners_mean.png')
        return ['plots/box_plot_corners_mean.png']

    def __draw_pie(self, data):

        fig, ax = plt.subplots()
        vc = data['gt_corners'].value_counts()
        ax.pie(vc.values, labels=['4 corners','6 corners','8 corners','10 corners'], autopct='%1.0f%%')
        self.__save_figure('plots/class_pie.png')
        return ['plots/class_pie.png']

    def __min_max_plot(self, data):
        fig, ax = plt.subplots(1,3, figsize=(20,10))
        ax[0].scatter(data['min'], data['max'])
        ax[0].set_xlabel('data.min')
        ax[0].set_ylabel('data.max')
        ax[1].scatter(data['floor_min'], data['floor_max'])
        ax[1].set_xlabel('data.floor_min')
        ax[1].set_ylabel('data.floor_max')
        ax[2].scatter(data['ceiling_min'], data['ceiling_max'])
        ax[2].set_xlabel('data.ceiling_min')
        ax[2].set_ylabel('data.ceiling_max')
        self.__save_figure('plots/min_max_all.png')
        return ['plots/min_max_all.png']

    def draw_plots(self, file):

        data = pd.read_json(file)

        to_ret = []
        to_ret += self.__draw_hists_floor_ceil(data)
        to_ret += self.__draw_hists_corners(data)
        to_ret += self.__draw_boxplot_means_corners(data)
        to_ret += self.__draw_pie(data)
        to_ret += self.__draw_heatmap(data)
        to_ret += self.__min_max_plot(data)
        return to_ret


