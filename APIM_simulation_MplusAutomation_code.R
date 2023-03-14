install.packages("MplusAutomation")
install.packages("texreg")
library(MplusAutomation)
library(texreg)
getwd()
setwd("C:/Users/junye/APIM")

################################################################################
# k parameter method data generation
createModels("C:/Users/junye/APIM/1.1.data_generation_KPARAM.txt")
runModels("C:/Users/junye/desktop/500replication/01.apimk/01.DATA_GENERATION", recursive=TRUE)

# delete the data generation input file and run below two lines
createModels("C:/Users/junye/APIM/1.2.KPARAM_input.txt")
runModels("C:/Users/junye/desktop/500replication/01.apimk/01.DATA_GENERATION", recursive=TRUE)


################################################################################
# chi-square difference test data generation
createModels("C:/Users/junye/APIM/2.1.data_generation_CHIDIFF.txt")
runModels("C:/Users/junye/desktop/500replication/02.chidiff/01.DATA_GENERATION", recursive=TRUE)

createModels("C:/Users/junye/APIM/2.2.CHIDIFF_input_actor_only.txt")
createModels("C:/Users/junye/APIM/2.3.CHIDIFF_input_couple.txt")
createModels("C:/Users/junye/APIM/2.4.CHIDIFF_input_contrast.txt")

# copy and pastes the replications in the folders for each test
runModels("C:/Users/junye/desktop/500replication/02.chidiff/02.1.ACTORONLY", recursive=TRUE)
runModels("C:/Users/junye/desktop/500replication/02.chidiff/02.2.COUPLE", recursive=TRUE)
runModels("C:/Users/junye/desktop/500replication/02.chidiff/02.3.CONTRAST", recursive=TRUE)


################################################################################
# model constraint data generation
createModels("C:/Users/junye/APIM/3.1.data_generation_MODELCONSTRAINT.txt")
runModels("C:/Users/junye/desktop/500replication/03.modelconstraint/01.DATA_GENERATION", recursive=TRUE)

# delete the data generation input file and run below two lines
createModels("C:/Users/junye/APIM/3.2.MODELCONSTRAINT_input_couple_contrast.txt")
runModels("C:/Users/junye/desktop/500replication/03.modelconstraint/01.DATA_GENERATION0", recursive=TRUE)
