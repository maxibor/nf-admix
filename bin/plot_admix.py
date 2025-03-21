#!/usr/bin/env python

import argparse
from pathlib import Path
import pandas as pd
import re
from plotnine import *

def parse_args():
    parser = argparse.ArgumentParser("Plot ADMIXTURE results")
    parser.add_argument("--dir", "-d", type=Path, default=".", help="Path to directory with cv log files")
    parser.add_argument("-b", type=int, default=1, dest="best", help="Plot best b admixture")
    parser.add_argument("output", type=str, help="Output file basename")

    return parser.parse_args()


def get_cv_error(d="."):
    min_err = 1
    best_k = 0
    cvs = Path(d).glob("*.log")
    k_regex = re.compile("^.*\(K\=(\d+)\).*$")
    cv_regex = re.compile("^.*\:\s{1}(\d+\.?\d+)$")
    k_list = []
    err_list = []
    for cv in cvs:
        with open(cv, "r") as f:
            for line in f: #CV error (K=3): 0.57090
                if "CV error" in line:
                    k = int(k_regex.match(line).group(1))
                    cv_err = float(cv_regex.match(line).group(1))
                    k_list.append(k)
                    err_list.append(cv_err)
                    print(f"Looking at {k} fold admixture")
                    if cv_err < min_err:
                        min_err = cv_err
                        best_k = k
                        print(f"New best K: {best_k}, CV error: {min_err}")

    return best_k, min_err, k_list, err_list

def plot_cv_errors(k_list, err_list, output):
    df = pd.DataFrame({"K": k_list, "CV error": err_list})
    df = df.sort_values("K")
    g = (
        ggplot(df, aes(x='K', y='CV error')) 
        + geom_point() 
        + geom_line() 
        + labs(y='CV error', x='K') 
        + theme_classic() 
    )
    g.save(f"{output}_cv_error.png", dpi=300)
    g.save(f"{output}_cv_error.svg")
    return df

def plot_best(k, output, d = "."):
    best_mix = list(Path(d).glob(f"*.{k}.Q"))[0].as_posix()
    df = pd.read_table(best_mix, sep=" ", header=None)
    df = df.reset_index().melt(id_vars="index", var_name='pop', value_name='prop')
    g = (
        ggplot(df, aes(x='index', y='prop', fill='pop')) 
        + geom_col(show_legend=False) 
        + labs(y='Admixture', x="") 
        + theme_classic() 
        + theme(
            axis_text_x=element_blank(),
            axis_line_x=element_blank(),
            axis_ticks_major_x=element_blank(),
            ) 
    )
    g.save(f"{output}_{k}_admixture.png", dpi=300)
    g.save(f"{output}_{k}_admixture.svg")
    return g

if __name__ == "__main__":
    args = parse_args()
    best_k, min_err, all_k, all_err = get_cv_error(args.dir)
    print(f"Best K: {best_k}, CV error: {min_err}")
    df_err = plot_cv_errors(all_k, all_err, args.output)
    print(df_err)
    for k in df_err['K'][:args.best]:
        print(k)
        plot_best(k, args.output, args.dir)
    # plot_best(best_k, args.output, args.dir)
    
                    

