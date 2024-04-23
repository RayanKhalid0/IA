import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("TestModelling.csv")

X = df.iloc[:, :-1]
columns = []

for column in X.columns:
    columns.append(column)

Y = df.iloc[:, -1]
target_col = df.columns[-1]


def scatter_plot():
    for feature_column in X.columns:
        plt.figure(figsize=(8, 6))
        plt.scatter(X[feature_column], Y, alpha=0.5)
        plt.title(f"{feature_column} vs. Target")
        plt.xlabel(feature_column)
        plt.ylabel("Target")
        plt.grid(True)
        plt.show()


def line_plot():
    for feature_column in X.columns:
        plt.figure(figsize=(8, 6))
        plt.plot(X[feature_column], Y, marker='o', linestyle='-')
        plt.title(f"{feature_column} vs. Target")
        plt.xlabel(feature_column)
        plt.ylabel("Target")
        plt.grid(True)
        plt.show()


def bar_plot():
    for feature_column in X.columns:
        plt.figure(figsize=(8, 6))
        plt.bar(X[feature_column], Y)
        plt.title(f"{feature_column} vs. Target")
        plt.xlabel(feature_column)
        plt.ylabel("Target")
        plt.grid(True)
        plt.show()


def pie_chart_plot():
    target_counts = df[target_col].value_counts()

    plt.figure(figsize=(8, 6))
    plt.pie(target_counts, labels=target_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title("Distribution of Target Variable")
    plt.axis('equal')
    plt.show()


def box_plot():
    for feature_column in X.columns:
        plt.figure(figsize=(8, 6))
        plt.boxplot([X[feature_column][Y == value] for value in Y.unique()], labels=Y.unique())
        plt.title(f"{feature_column} Box Plot by Target")
        plt.xlabel("Target")
        plt.ylabel(feature_column)
        plt.grid(True)
        plt.show()


def violin_plot():
    for feature in X.columns:
        plot_data = pd.concat([X, Y], axis=1)

        plot_data_melted = pd.melt(plot_data, id_vars=target_col, var_name=feature)

        plt.figure(figsize=(10, 6))
        sns.violinplot(x=feature, y="value", hue=target_col, data=plot_data_melted, split=True, inner="quart")
        plt.title("Violin Plot of Features vs. Target")
        plt.xlabel("Feature")
        plt.ylabel("Value")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


violin_plot()

