csv_file = request.FILES["file"]
# if not csv_file.name.endswith('.csv'):
#     messages.error(request,'File is not CSV type')
    
# if csv_file.multiple_chunks():
#     messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
    
# read csv file
file_data = csv_file.read().decode("utf-8")
lines = file_data.split("\n")
columns = ['name', 'planvalidity', 'planvalidityunit', 'quotaid', 'price', 'priceunit', 'profilestatus', 'quotacarryforwarder', 'maxvalue', 'planunit', 'autorenewal', 'renewalperiod', 'frequency', 'qosid', 'plansubscriptiondate', 'planstartdate', 'planexpirydate', 'plantype']
# convert csv data into dict and append in list
result = []
for row in lines[1:]:
    row = row.split(",")
    row = dict(zip(columns, row))
    result.append(row)
    
for index in range(len(result)):
    if result[index]['name'] == "" or result[index]['planvalidity'] == "":
        del result[index]