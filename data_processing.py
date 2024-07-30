import pandas as pd

filenames_to_process = ['hungarian','cleveland']

for filename in filenames_to_process:

    # Converting unprocessed file into a processed file with headers
    file1 = open(filename + '.data', 'r', encoding= 'unicode_escape')
    Lines = file1.readlines()

    data_array = []
    headers = "id ccf age sex painloc painexer relrest pncaden cp trestbps htn chol smoke cigs years fbs dm famhist restecg ekgmo ekgday ekgyr dig prop nitr pro diuretic proto thaldur thaltime met thalach thalrest tpeakbps tpeakbpd dummy trestbpd exang xhypo oldpeak slope rldv5 rldv5e ca restckm exerckm restef restwm exeref exerwm thal thalsev thalpul earlobe cmo cday cyr num lmt ladprox laddist diag cxmain ramus om1 om2 rcaprox rcadist lvx1 lvx2 lvx3 lvx4 lvf cathef junk name\n"
    data_array.append(headers)
    create_new_line = ""
    for line in Lines:   
        create_new_line = create_new_line + " " + line 
        if "name" in line:
            data_array.append(create_new_line.strip().replace('\n','') + "\n")
            create_new_line = ""
        else:
            continue


    file1 = open(filename+'_processed.data', 'w',encoding="utf8")
    file1.writelines(data_array)
    file1.close()

    # converting in csv
    dataframe1 = pd.read_csv(filename+"_processed.data")
    dataframe1.to_csv(filename+'_processed.csv',index = None)

    print("Conversion Completed for file name : "+filename)