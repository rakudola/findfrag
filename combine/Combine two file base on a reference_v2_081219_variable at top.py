import csv

FirstInPutPath="G:\BYU OneDrive_G\OneDrive - BYU Office 365\BYU\===Price lab===\Data\Folding Project\LL3045_Diflunisal_I300mM\peaks output\LL3045_Diflunisal_A_0uM_LABEL FREE_14_more peptide"
FirstInName="LL3045_A_proteins Name"
SecondInPath="G:\BYU OneDrive_G\OneDrive - BYU Office 365\BYU\===Price lab===\Data\Folding Project\LL3050_Sina'sData\LL3050_Sina_bio1tech1A_QUANT"
SecondInName="LL3050_proteinsName"
OutPutPath="G:\BYU OneDrive_G\OneDrive - BYU Office 365\BYU\===Price lab===\Data\Folding Project\LL3050_Sina'sData\LL3050_Sina_bio1tech1A_QUANT"
OutName="LL3050+LL3045_proteinName+peptide"


#do Not Chnage anything Below#

#INPUT FIRST FILE
Ainfile=open(FirstInPutPath+"\\"+FirstInName+".csv","r")#"r"=reading mode
Areader=csv.reader(Ainfile)#create reader object
headerA=next(Areader)#ignore the first row in csv file
dataA=list(Areader)
Ainfile.close()

    

#INPUT SECOND FILE
Binfile=open(SecondInPath+"\\"+SecondInName+".csv","r")#"r"=reading mode
Breader=csv.reader(Binfile)#create reader object
headerB=next(Breader)
dataB=list(Breader)
Binfile.close()



#USE THE KEY AND COMBINE TWO LIST-WAY2
combineData=[]
for i in range(len(dataA)):
     for j in range(len(dataB)):
         if dataB[j][0]==dataA[i][0]:
             #print (dataA[i][0],dataA[i][1],dataB[j][1])
             dataA[i].extend(dataB[j])#this is a trick to deal with list of list, the i is the pointer



#output the data file        
outfile=open(OutPutPath+"\\"+OutName+".csv","w",newline="")
writer=csv.writer(outfile)#create write object
headerA.extend(headerB)
newheader=headerA
writer.writerow(newheader)
for addvariable in dataA:
    writer.writerow(addvariable)
outfile.close()
