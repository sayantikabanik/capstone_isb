
#Exploratory factor analysis in R Dr Paul Christiansen

################packages to install- only needs to be done once.


install.packages("psych")  ######PCA/EFA amongst many other things!
install.packages("REdaS")  ######produces KMO and Bartletts test
install.packages("readxl") ######reads excel

###############pull packages out of the library


library(psych)
library(readxl)
library(REdaS)


##############read in the data set

#ATGC <- read_excel("C:/Users/prc/Desktop/Covid-19/BOOK/FA_in_R/ATGC_expFA.xlsx")
#View(ATGC)        
##attach(ATGC)
x <- read.csv("combinedReviews.csv",header=TRUE)
x_new<-data.frame(x$workLifeBalance
,x$skillDevelopment,x$salaryBenefits,x$workSatisfaction,x$careerGrowth,x$companyCulture)
x_new
dz=na.omit(x_new)
head(dz)
#############

bart_spher(ATGC) ###### produces Bartletts test of spherecity (you want this to be significant)
KMO(ATGC)       ###### Kaiser-Meyer-Olkin measure, you want to be above .7


#############FA, if you are doing a PCA switch fa to say principal

##########using Kaisers rule, Eigenvalues>1 represent valid factors

###set nfactors to n items, in this case there is 12 items so we state nfactors=12
#####oblimin is selected as the rotation although this is default for factor analysis (variamx is default for pca)
##orthagonal roatations availible ="none", "varimax", "quartimax", "bentlerT", "equamax", "varimin", "geominT" "bifactor" 
##oblique roatations availible "Promax", "promax", "oblimin", "simplimax", "bentlerQ, "geominQ" "biquartimin" "cluster" 

#fa(dz, nfactors = 2, rotate =  "oblimin" )  


###################you can produce a figure 

M1<-fa(dz, nfactors = 3, rotate = "varimax" ) ##save the analysis as the object m1
fa.diagram(M1,main="data")                      ## produce a figure with the title "" note fa.diagram still works for PCA























