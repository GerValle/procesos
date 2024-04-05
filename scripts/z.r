pdf("xh.pdf") # set graphical output file
hist(rnorm(1000)) # generate 100 N(0,1) variates and plot their histogram
dev.off() # close the graphical output file