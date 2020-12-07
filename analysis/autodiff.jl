using Pkg
Pkg.activate("../juliadev/")
# add the ForwardDiff package
Pkg.add("ForwardDiff")
# add the DataFrame package
Pkg.add("DataFrames")
# add the Distributions package
Pkg.add("Distributions")
# add the Plots package
Pkg.add("Plots")

using Base.Threads
using Random

using DataFrames
using Distributions
using ForwardDiff
using Plots

f(x::Vector) = sum(sin, x) + prod(tan, x) * sum(sqrt, x)
x = rand(5)
println(ForwardDiff.gradient(f, x))
println(Threads.nthreads())

x_i = Float32.(rand(Uniform(0.0, 1.0), 15))
y_o = Float32.(rand(Uniform(0.0, 1.0), 15))
print(typeof(x_i))
println(transpose(x_i) * y_o)
dfr = DataFrame(:input => x_i, :output => y_o)
println(dfr)
println(dfr.input)
plot(dfr.input, dfr.output, seriestype = :scatter, title = "Scatter")
