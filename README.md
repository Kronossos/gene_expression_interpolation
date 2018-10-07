# Gene expression interpolation


Program allows constructing spline interpolation for gene expression data.


I used data from the publication: http://msb.embopress.org/content/3/1/72#DC2


The genes were divided into groups according to their expression profile during embryogenesis in input_class_file.xls file.
Their expression profiles are in the input_research_file.xls file.


Based on two files, the program performs the following analyzes:
1. Loads the names and gene profiles from .xls files,
2. Finds the average profile of each group and class,
3. Finds spline interpolations for a profile of each gene, group and class,
4. Creates diagrams containing spline for each group and class.
