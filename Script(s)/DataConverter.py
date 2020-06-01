import csv
import pandas as pd

Mississauga = "Mississauga"
Kenora = "Kenora"
ThunderBay = "Thunder Bay"
SaultSteMarie = "Sault Ste. Marie"
Sudbury = "Sudbury"
Timmins = "Timmins"
London = "London"
StThomas = "St.Thomas"
OwenSound = "Owen Sound"
Brantford = "Brantford"
Guelph = "Guelph"
Hamilton = "Hamilton"
Oakville = "Oakville"
Barrie = "Barrie"
Newmarket = "Newmarket"
Toronto = "Toronto"
NorthBay = "North Bay"
Thorold = "Thorold"
Whitby = "Whitby"
Peterborough = "Peterborough"
PortHope = "Port Hope"
Brockville = "Brockville"
Ottawa = "Ottawa"



def main():

    miss_cases = 0
    ken_cases = 0
    thun_cases = 0
    sault_cases = 0
    sud_cases = 0
    tim_cases = 0
    lon_cases = 0
    st_cases = 0
    owen_cases = 0
    brant_cases = 0
    gue_cases = 0
    ham_cases = 0
    oak_cases = 0
    barrie_cases = 0
    newm_cases = 0
    tor_cases = 0
    north_cases = 0
    thor_cases = 0
    whit_cases = 0
    peter_cases = 0
    port_cases = 0
    brock_cases = 0
    ottawa_cases = 0

    with open("conposcovidloc.csv", "r") as original:
        for row in original:
            if Mississauga in row:
                miss_cases += 1
            if Kenora in row:
                ken_cases += 1
            if ThunderBay in row:
                thun_cases += 1
            if SaultSteMarie in row:
                sault_cases += 1
            if Sudbury in row:
                sud_cases += 1
            if Timmins in row:
                tim_cases += 1
            if London in row:
                lon_cases += 1
            if StThomas in row:
                st_cases += 1
            if OwenSound in row:
                owen_cases += 1
            if Brantford in row:
                brant_cases += 1
            if Guelph in row:
                gue_cases += 1
            if Hamilton in row:
                ham_cases += 1
            if Oakville in row:
                oak_cases += 1
            if Barrie in row:
                barrie_cases += 1
            if Newmarket in row:
                newm_cases += 1
            if Toronto in row:
                tor_cases += 1
            if NorthBay in row:
                north_cases += 1
            if Thorold in row:
                thor_cases += 1
            if Whitby in row:
                whit_cases += 1
            if Peterborough in row:
                peter_cases += 1
            if PortHope in row:
                port_cases += 1
            if Brockville in row:
                brock_cases += 1
            if Ottawa in row:
                ottawa_cases += 1
            cases = ken_cases,thun_cases,sault_cases,sud_cases,tim_cases,lon_cases,st_cases,owen_cases,brant_cases,gue_cases,ham_cases,oak_cases,barrie_cases,miss_cases,newm_cases,tor_cases,north_cases,thor_cases,whit_cases,peter_cases,port_cases,brock_cases,ottawa_cases

        with open("Data.csv", "w") as Data:
            writer = csv.writer(Data)
            writer.writerow(cities)
            writer.writerow(cases)

        pd.read_csv('Data.csv', header = None).T.to_csv('FinalData.csv', header = False, index = False)
                
cities = ('Kenora','Thunder Bay','Sault Ste. Marie','Sudbury','Timmins','London','St.Thomas','Owen Sound','Brantford','Guelph','Hamilton','Oakville','Barrie','Mississauga','Newmarket','Toronto','North Bay','Thorold','Whitby','Peterborough','Port Hope','Brockville','Ottawa')        


if __name__ == "__main__":
    main()

