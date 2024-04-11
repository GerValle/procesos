# Ejemplo de script en R
library(ggplot2)

x = rnorm(1000)
y = rnorm(1000)
plot(x, y)

library(ggplot2)

# Create a data frame with two variables
df <- data.frame(x = rnorm(100), y = rnorm(100))

# Create a scatter plot using ggplot2
ggplot(df, aes(x = x, y = y)) +
  geom_point()


  library(ggplot2)

# Create a data frame with one variable
df <- data.frame(x = rnorm(100))

# Create a histogram using ggplot2
ggplot(df, aes(x = x)) + geom_histogram()