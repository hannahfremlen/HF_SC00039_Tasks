import csv

# Open, read and store the data of the csv file as a list.
with open('brca_cnvs_tcga-1-2.csv','r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Add seq_length to the header
data[0].append('seq_length')

# Loop over the rows to extract the data from loc.start and loc.end (skipping the header), turning them into integers to enable subtraction to calculate the seq length and append to the data set.
    
for row in data[1:]:
    start = int(row[2])
    end = int(row[3])
    row.append(end - start)

# Create a new output file with 5 columns
with open('brca_cnvs_tcga-1-2_out.csv','w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)
