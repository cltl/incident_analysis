import json
import glob
from collections import defaultdict, Counter
import pprint
from itertools import islice
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def barplot(plot_data, n_columns, ordered_l, output_folder, incident, textspan, fs, verbose):
    """create barplot"""
    width = 0.5
    plt.style.use('tableau-colorblind10')
    
    if fs != None:
        fig, ax = plt.subplots(figsize=fs,dpi=300)
    else:
        fig, ax = plt.subplots(dpi=300)

    #plt.style.use('tableau-colorblind10')
    plt.ylabel('proportion per TDC')
    plt.xlabel('TRD in TDCs')
    bottom = np.zeros(n_columns)

    for pos, percentages in plot_data.items():
        p = ax.bar(ordered_l, percentages, width, label=pos, bottom=bottom)
        bottom += percentages

    legend = ax.legend(bbox_to_anchor=(1, 1))
    pdf_path = f"{output_folder}/output/{incident}/figures/constructions/{textspan}_anchor.pdf"
    plt.savefig(pdf_path, bbox_inches='tight')
    if verbose:
        print(f"exported plot to {pdf_path}")
    return

def extract_construction_info(incident_d, ordered_tbs, textspan=None):
    """prepare participant POS data for plotting"""
    construction_types_l = ["clause",
                            "nominalization",
                            "regular noun",
                            "compound",
                            "named event",
                            "other"]
    tbs_l = []
    plot_data = defaultdict(list)

    for time_bucket, info in incident_d["anchor"].items():
        tbs_l.append(time_bucket)

    for time_bucket, info in incident_d["anchor"].items():
        total = []
        for tupl in info["joint"]:
            if textspan == None:
                total.append(tupl[4])
            else:
                if tupl[3] in textspan:
                    total.append(tupl[4])
        counter = Counter(total)
        for typ in construction_types_l:
            if typ in counter.keys():
                freq = counter[typ]
                perc = round((freq*100)/len(total))
                plot_data[typ].append(perc)
            else:
                plot_data[typ].append(0)

    if ordered_tbs != None:
        for typ, perc_l in plot_data.items():
            perc_newl = reorder_time_buckets(tbs_l, perc_l, ordered_tbs)
            plot_data[typ] = np.array(perc_newl)
    return tbs_l, plot_data

def reorder_time_buckets(unordered_tbs, unordered_perc, ordered_tbs):
    "reorder time buckets for plotting"
    tbs_perc = []

    for x, y in zip(unordered_tbs, unordered_perc):
        tbs_perc.append((x,y))

    ordered_perc = []

    for tdc in ordered_tbs:
        for tupl in tbs_perc:
            if tupl[0] == tdc:
                ordered_perc.append(tupl[1])
    return ordered_perc
