#!/usr/bin/python2
# -*- coding: utf-8 -*-
import pandas
import numpy as np
import matplotlib.pyplot as plt
import xlrd
from scipy.interpolate import InterpolatedUnivariateSpline
from matplotlib.backends.backend_pdf import PdfPages
from sys import argv


def draw_and_save(save_file, name):
    plt.suptitle(name)
    plt.xlabel("Time (h)")
    plt.ylabel("Expression Profile")
    save_file.savefig(dpi=1)


def interpolate(data, smoothness):
    x = np.linspace(0, 24, 30)
    spl = InterpolatedUnivariateSpline(x, data)
    plt.plot(x, data, 'ro', ms=0)
    xs = np.linspace(0, 24, smoothness)
    plt.plot(xs, spl(xs), lw=0.5, alpha=1)


def counting(class_file, research_file):
    pdf_file = PdfPages('Data after interpolation.pdf')

    # Loading the file with the classes.
    classes = pandas.read_excel(class_file, header=0, sheetname=range(1, 12))

    # Loading the file with the research and later deleting the unnecessary 2nd column.
    research = pandas.read_excel(research_file, sheetname=0, header=1, index_col=0)
    research.pop('KP name')

    xls = xlrd.open_workbook(class_file, on_demand=True)
    titles = list(xls.sheet_names())

    # Loop that passes through each of the 11 sheets from class_file.
    for n in xrange(1, 12):

        mean = np.zeros(30)

        # Loop that passes through each gene in a given class.
        for name in classes[n]["FID"]:

            gene_score = np.array(research.loc[name].values.tolist())

            # Take only data from first research (if more then one).
            if gene_score.shape != (30,):
                gene_score = gene_score[0]

            mean += gene_score

            interpolate(gene_score, 200)

        draw_and_save(pdf_file, titles[n])
        plt.clf()

        mean /= len(list(classes[n]["FID"]))
        interpolate(mean, 200)
        draw_and_save(pdf_file, str(titles[n]) + " average")
        plt.clf()

        print "Completed  ", (100 * n / 11), "%."

    pdf_file.close()


def main():
    try:
        script_name, input_class, input_research = argv
    except:
        print "\nYou have submitted the files incorrectly. " \
              "\nCheck if you have entered two files. " \
              "\nExample: " \
              "\npython interpolate_script.py input_class_file.xls input_research_file.xls"
        exit(1)

    print "\nPLEASE WAIT FOR THE COMMUNICATION AT THE END OF ACTION! \n"

    try:
        counting(input_class, input_research)
    except:
        print "\nThe specified files are incorrect. " \
              "\nCheck if they are correct or if you entered them correctly. " \
              "\nExample: " \
              "\npython interpolate_script.py input_class_file.xls input_research_file.xls"
        exit(1)

    print "\nThe program has ended. \n"


if __name__ == '__main__':
    main()
