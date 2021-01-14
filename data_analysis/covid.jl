# -*- coding: utf-8 -*-

import Base.Filesystem
import Base.Threads
import Dates
import Random
import Random.MersenneTwister

import CSV
import DataFrames
import GLM
import Plots

const PATH = Filesystem.pwd()
const FILENAME = "covid.csv"
const FILE = Filesystem.joinpath(PATH, "data", FILENAME)
const THREADS = Threads.nthreads()


"""
    read_csv(file)

Read the .csv content in ``file`` into a ``DataFrame``.

### Arguments

* `file` : a string

"""
function read_csv(file)::DataFrames.DataFrame
    df = CSV.read(file, DataFrames.DataFrame)
    return df
end


"""
    create_dates(data)

Create a ``Dates.Date`` array from the ``data`` given.

### Arguments

* `data` : a DataFrames.SubDataFrame

"""
function create_dates(data)::Array{Dates.Date}
    dates = data[:, 1:3]
    n_dates = DataFrames.nrow(dates)
    # define an empty Date array with shape (n_dates,)
    dat = Array{Dates.Date}(undef, n_dates)
    for i in 1:DataFrames.nrow(dates)
        date = Dates.Date(
            Dates.Day(dates[i, 1][1]),
            Dates.Month(dates[i, 2][1]),
            Dates.Year(dates[i, 3][1]),
        )
        dat[i] = date
    end
    # reverse the order since it is given "wrong" in the csv
    dat = dat[end:-1:1]
    return dat
end


"""
    compute_input(x, degree)

Compute the input matrix to a Linear Regression model up to ``degree``.

### Arguments

* `x` : an ``Array``
* `degree` : an Int

"""
function compute_input(x, degree)::Array{Float64}
    n_samples = size(x)[1]
    input = ones(Float64, (n_samples, degree + 1))
    for i in 1:1:degree
        input[:, i + 1] = x.^i
    end    
    return input
end



function analyze_country!(data, country)
    # get only the data for country
    data = data[data["Location.Country"] .== country, :]
    # get the abbreviation code
    code = data["Location.Code"][1, :][1]
    # create the dates array
    dates = create_dates(data)
    # get the cases and reverse the order
    cases = data["Data.Cases"][end:-1:1]
    println(DataFrames.describe(data))
    plot = Plots.plot()
    display(Plots.plot!(dates, cases; 
            title=string("Daily Covid19 Cases in ", country),
            label=code,
            xlabel="dates",
            ylabel="cases", 
            lw=2.5,
            legend=:topleft,
            size=(1000, 1000),
            )
    )
    return data
end


df = read_csv(FILE)
println(DataFrames.head(analyze_country!(df, "Germany")))
# group the data by continent
grouped_continents = DataFrames.groupby(df, "Location.Continent")
# get the continents as keys
continents = DataFrames.keys(grouped_continents)
# get the number of continents
n_continents = size(continents)[1]

# create an empty plot
plot = Plots.plot()
for i in 1:n_continents
    # get the individual continent as DataFrame
    continent = grouped_continents[continents[i]]
    continent_name = continents[i]["Location.Continent"]
    # group the continent DataFrame by countries
    grouped_countries = DataFrames.groupby(continent, "Location.Country")
    # get the countries as keys
    countries = DataFrames.keys(grouped_countries)
    # get the number of countries
    n_countries = length(countries)
    for j in 1:n_countries
        # get the individual country as DataFrame
        country = grouped_countries[countries[j]]
        country_name = countries[j]["Location.Country"]
        # get the cases per country and its number
        cases = country[:, "Data.Cases"][end:-1:1]
        n_cases = length(cases)
        # get the dates as Date object
        dates = create_dates(country)

        # create a linear regression model
        x = 1:1:n_cases
        # define the polynomial degree
        degree = 4
        input = compute_input(x, degree)
        lin_model = GLM.fit(GLM.LinearModel, input, cases)
        linear_fit = GLM.predict(lin_model)

        # display(Plots.plot!(dates, cases; 
        #     title=string("Daily Covid19 Cases in ", continent_name),
        #     label=country_name, 
        #     xlabel="dates",
        #     ylabel="cases", 
        #     lw=2.5,
        #     legend=:topleft,
        #     size=(1000, 1000),
        #     )
        # )
        # display(Plots.plot!(dates, linear_fit;
        #     lw=2.5,
        #     label=string(country_name, " trend")
        #     )
        # )
        if j == 2
            break
        end
    end
    break
end

