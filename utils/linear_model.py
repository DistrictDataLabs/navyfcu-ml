#!/usr/bin/env python3

import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import make_regression
from matplotlib.patches import Rectangle

sns.set_context('notebook')
sns.set_style('whitegrid')
sns.set_palette('deep')


FIGURES = os.path.join(os.path.dirname(__file__), "..", "figures")


def make_2d_regression(n=10, noise=35.0, random_state=None):
    x, y, coef = make_regression(
        n_samples=n, n_features=1, noise=noise, coef=True, random_state=random_state
    )

    return x.ravel(), y, coef


def draw_ols(name=None, ax=None, **kwargs):
    if ax is  None:
        _, ax = plt.subplots(figsize=(9,6))

    x, y, coef = make_2d_regression(**kwargs)

    # compute the limit, regression line, and y predictions
    lims = (x.min()-0.5, x.max()+0.5)
    xl = np.linspace(*lims)
    yl = np.dot(xl,coef)
    yp = np.dot(x,coef)

    # plot the regression line and scatter plot
    ax.plot(xl, yl, ls='--')
    ax.scatter(x, y, marker='x')

    # draw the error rectangles
    for xi, yi, yhi in zip(x, y, yp):
        err = yhi - yi
        rect = Rectangle((xi,yi), err/100, err, alpha=0.3, ls='solid', fill=True, ec='r', fc='r')
        ax.add_patch(rect)

    # format the axes for display
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_xlim(*lims)

    if name:
        path = os.path.join(FIGURES, name)
        plt.savefig(path)
    else:
        plt.show()


def draw_explained_variance(name=None, ax=None, **kwargs):
    if ax is  None:
        _, ax = plt.subplots(figsize=(9,6))

    x, y, coef = make_2d_regression(**kwargs)

    # compute the limit, regression line, and y predictions
    lims = (x.min()-0.5, x.max()+0.5)
    xl = np.linspace(*lims)
    yl = np.dot(xl,coef)
    yp = np.dot(x,coef)

    # plot the regression line and scatter plot
    ax.plot(xl, yl, ls='-')
    ax.scatter(x, y, marker='x')

    # annotate ybar
    ax.axhline(y.mean(), ls='--', label=r"$\bar{y}$", c='g')

    # add explained variance
    for idx, (xi, yi, yp) in enumerate(zip(x,y,yp)):
        if yi > yp and  yp > y.mean():
            ax.plot([xi, xi], [yp, y.mean()], ls=":", c='c', lw=2, label="explained variance (from model)" if idx==0 else None)
            ax.plot([xi, xi], [yi, yp], ls=":", c='r', lw=2, label="unexplained variance (noise)" if idx==0 else None)
        elif yi < yp and yp < y.mean():
            ax.plot([xi, xi], [yp, y.mean()], ls=":", c='c', lw=2, label="explained variance (from model)" if idx==0 else None)
            ax.plot([xi, xi], [yi, yp], ls=":", c='r', lw=2, label="unexplained variance (noise)" if idx==0 else None)

    # format the axes for display
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_xlim(*lims)
    ax.legend(loc='upper left', frameon=True)

    if name:
        path = os.path.join(FIGURES, name)
        plt.savefig(path)
    else:
        plt.show()


if __name__ == '__main__':
    # draw_ols(name="ordinary_least_squares.png", random_state=32)
    draw_explained_variance(name="explained_variance.png", random_state=32)
