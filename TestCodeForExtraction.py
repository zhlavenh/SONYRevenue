import PyPDF2 as pypdf, re, os

# GeoRevenueFiles = os.listdir("GeoRevenue")
GeoRevenueFiles = []
for a in os.listdir("GeoRevenue"):
    GeoRevenueFiles.append(os.path.join("GeoRevenue", a))

startingPoints = 0
startingStrings = ["year ended", "Year ended", "Year Ended"]

for fileName in GeoRevenueFiles:
    with open(fileName, 'rb') as pdfFile:
        reader = pypdf.PdfReader(pdfFile)
        test = reader.pages[0]
        textFromPDf = test.extract_text()
    # print(textFromPDf)
    check = any(item in textFromPDf for item in startingStrings)
    if check == True:
        print("Starting point found")
    else:
        print(f"Starting point not found in file: {fileName}")
    # if "Year ended" in textFromPDf:
    #     print("String Exist as Year ended")
    #     startingPoints += 1
    # elif "Year Ended" in textFromPDf:
    #     print("String Exist as Year Ended")
    #     startingPoints += 1
    # else:
    #     print(f"String not found in file: {fileName}")
    
# print(f"The expected refrences was: {count(GeoRevenueFiles)}. The actual count of refreneces is: {startingPoints} ")