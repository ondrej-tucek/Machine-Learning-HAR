# -*- coding: utf-8 -*-
"""
@author: ondrej-tucek
@date: 2016-02-14
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pylab as plot


def plot_variable_importance(feature_importance, names_cols, save_name, save):
    """Show Variable importance graph."""    

    # scale by max importance first 20 variables in column names
    feature_importance = feature_importance / feature_importance.max()
    sorted_idx = np.argsort(feature_importance)[::-1][:20]
    barPos = np.arange(sorted_idx.shape[0]) + .8
    barPos = barPos[::-1]
    
    #plot.figure(num=None, facecolor='w', edgecolor='r') 
    plot.figure(num=None, facecolor='w') 
    plot.barh(barPos, feature_importance[sorted_idx]*100, align='center')
    plot.yticks(barPos, names_cols[sorted_idx])
    plot.xticks(np.arange(0, 120, 20), \
      ['0 %', '20 %', '40 %', '60 %', '80 %', '100 %'])    
    plot.margins(0.02)
    plot.subplots_adjust(bottom=0.15)
    
    plot.title('Variable Importance')
    
    if save:
	plot.savefig(save_name, bbox_inches='tight', dpi = 300)
	plot.close("all")
    else:
	plot.show()    
    

def plot_confusion_matrix(conf_mat, classes, save_name, save):
    """Show correctly color of cell in Confusion matrix."""    

    N, cbar_label, fake_mat = get_data_to_plot(conf_mat)
    cmap = discrete_cmap(N, 'Blues')

    fig, ax = plt.subplots(num=None, facecolor='w')
    ax.imshow(fake_mat, interpolation='nearest', cmap=cmap, vmin=0, vmax=N)
    for i in range(conf_mat.shape[0]):
	for j in range(conf_mat.shape[1]):
	    ax.text(x=j, y=i, s=conf_mat[i, j], va='center', ha='center')

    ax.set_xticks(range(len(classes)))
    #tick_marks = np.arange(len(conf_mat.columns))
    #ax.set_xticks(tick_marks, conf_mat.columns, rotation=45)
    ax.set_xticklabels(classes)
    ax.xaxis.set_ticks_position("bottom")
    ax.set_yticks(range(len(classes)))
    ax.set_yticklabels(classes)    

    mappable = cm.ScalarMappable(cmap=cmap)
    mappable.set_array([])
    mappable.set_clim(-0.5, N+0.5)

    str_label = map(str, cbar_label)
    str_label[-1] = r"$\leq$" + str_label[-1]

    colorbar = plt.colorbar(mappable)
    colorbar.set_ticks(np.linspace(0, N, N)) 
    colorbar.ax.set_yticklabels(str_label) 
    colorbar.set_ticklabels(str_label) 

    plt.xlabel('Predicted class')
    plt.ylabel('Actual Class')
    plt.title("Confusion matrix")    
    
    if save:
      plt.savefig(save_name, bbox_inches='tight', dpi = 300)
      plt.close("all")
    else:
      plt.show()


def discrete_cmap(N, base_cmap=None):
    """Create an N-bin discrete colormap from the specified input map."""

    # Note that if base_cmap is a string or None, you can simply do
    #    return plt.cm.get_cmap(base_cmap, N)
    # The following works for string, None, or a colormap instance.

    base = plt.cm.get_cmap(base_cmap)
    color_list = base(np.linspace(0, 1, N))
    cmap_name = base.name + str(N)
    
    return base.from_list(cmap_name, color_list, N)


def get_data_to_plot(conf_mat):
    """
    Return a triple (number N, label vector, fake_mat matrix),
    that will be used to (discretization a color, labelling 
    colorbar, properly show color of cell in matrix).
    """
    
    min_diag = np.diag(conf_mat).min()
    dg = np.diag(np.diag(conf_mat))
    mat_zero_diag = conf_mat - dg
    uniq_el = pd.unique(mat_zero_diag.flatten())
    N = 1 + len(uniq_el)

    tmp = np.append(uniq_el, min_diag)
    tmp_sort = np.argsort(tmp)
    label = tmp[tmp_sort]

    uniq_el_sort = np.argsort(uniq_el) 
    uniq_el = uniq_el[uniq_el_sort]
    idx_diff = np.where(range(N-1) != uniq_el)[0]
    #conf_mat[conf_mat == 6] = 100
    fake_mat = conf_mat.copy()
    for el in idx_diff:
	fake_mat[fake_mat == uniq_el[el]] = el

    fake_mat.flat[::len(conf_mat)+1] = N-1
    #print conf_mat
    #print ""
    #print fake_mat
    
    return (N, label, fake_mat)
