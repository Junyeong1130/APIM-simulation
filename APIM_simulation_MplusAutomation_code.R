install.packages("MplusAutomation")
install.packages("texreg")
library(MplusAutomation)
library(texreg)
getwd()
setwd("C:/Users/junye/APIM")

# you need to modify the paths for input file forms, and paths belonging to the below lines in a way you want.

################################################################################
# k parameter method data generation
createModels("C:/Users/junye/APIM/1.1.data_generation_KPARAM.txt")
runModels("C:/Users/junye/desktop/500replication/01.apimk/01.DATA_GENERATION", recursive=TRUE)

# input file generation for parameter k method
createModels("C:/Users/junye/APIM/1.2.KPARAM_input.txt")

# run all the input files at once
runModels("C:/Users/junye/desktop/500replication/01.apimk/01.DATA_GENERATION", recursive=TRUE)


################################################################################
# chi-square difference test data generation
createModels("C:/Users/junye/APIM/2.1.data_generation_CHIDIFF.txt")
runModels("C:/Users/junye/desktop/500replication/02.chidiff/01.DATA_GENERATION", recursive=TRUE)

# input file generation for chi-square difference test
createModels("C:/Users/junye/APIM/2.2.CHIDIFF_input_actor_only.txt")
createModels("C:/Users/junye/APIM/2.3.CHIDIFF_input_couple.txt")
createModels("C:/Users/junye/APIM/2.4.CHIDIFF_input_contrast.txt")

# run all the input files at once
runModels("C:/Users/junye/desktop/500replication/02.chidiff/02.1.ACTORONLY", recursive=TRUE)
runModels("C:/Users/junye/desktop/500replication/02.chidiff/02.2.COUPLE", recursive=TRUE)
runModels("C:/Users/junye/desktop/500replication/02.chidiff/02.3.CONTRAST", recursive=TRUE)


################################################################################
# model constraint data generation
createModels("C:/Users/junye/APIM/3.1.data_generation_MODELCONSTRAINT.txt")
runModels("C:/Users/junye/desktop/500replication/03.modelconstraint/01.DATA_GENERATION", recursive=TRUE)

# input file generation for new-variable method
createModels("C:/Users/junye/APIM/3.2.MODELCONSTRAINT_input_couple_contrast.txt")

# run all the input files at once
runModels("C:/Users/junye/desktop/500replication/03.modelconstraint/01.DATA_GENERATION0", recursive=TRUE)
