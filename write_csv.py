import csv
headers = ["scores"]
scores = list(map(lambda x:[x],scores)) # scores ndarray(7200,)
with open('test.csv','w', newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(scores)
