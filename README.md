# Independent Academic Research: Black-Scholes model: 
https://github.com/i-api/Independant-Academic-Research

<br/>

## Topic
I will be doing independant academic research on the mathematical basis for Financial Derivatives. My research will focus on options contracts and derivative instruments, and how these baskets of assets are classified, calculated and priced in the market using data models. The Black-Scholes model will be used to expore these data models, and the Greeks Financial ratios (delta δ, gamma γ, rho ρ, theta θ) (alpha α and betaβ will NOT be included) will be used to calculate the sensitivity of the price of the option to changes in the underlying asset on a mathematical basis. I will also be using the Monte Carlo method to price options contracts. My research will consist of a literature review, and a report on my findings, as well as a computer data model that will consolidate my research.

## Goals:
- [x] My research will be concluded in a written dissertation, and additionally a computer data model that I will build from scratch with Python.
- [x] Summary Paper: 
    - Number of Pages: 8 
- [x] Faculty Selected Readings
- [x] Student Selected Readings



<br/><br/><br/><br/>



# Black–Scholes–Merton Model | Raw Notes
## History:
- Options had been traded for many years before the Black-Scholes model was developed.
- The Black-Scholes model was developed in 1973 by Fischer Black and Myron Scholes, and Robert C. Merton, and was published in 1973 in the Journal of Political Economy.
- The Black-Scholes model was developed to price options contracts
- It was revolutionary because it was the first time that options contracts were priced using mathematical models, and not just by the market.
- 
- 


## Black–Scholes equation:
The Black–Scholes equation is the partial differential equation that describes the price of an option over time:
$$V = S_0 N(d_1) - K e^{-rT} N(d_2)$$
Where:
V is the option price
S_0 is the current price of the underlying asset
N(d_1) is the cumulative standard normal distribution of d_1
K is the option's strike price
e^{-rT} is the discounted factor
N(d_2) is the cumulative standard normal distribution of d_2
r is the risk-free interest rate
T is the time to expiration


## Black–Scholes formula:
The Black–Scholes formula is the mathematical formula that describes the price of a European call options and put options:
$$C = S_0N(d_1) - Ke^{-rT}N(d_2)$$
Where:
$C$ is the option price
$S_0$ is the current price of the underlying asset
$N(d_1)$ and $N(d_2)$ are the cumulative standard normal distribution functions of $d_1$ and $d_2$, respectively
$K$ is the strike price of the option
$r$ is the risk-free interest rate
$T$ is the time to expiration of the option, in years

$d_1$ and $d_2$ are defined as follows:
$$d_1 = \frac{ln\left(\frac{S_0}{K}\right) + (r + \frac{\sigma^2}{2})T}{\sigma \sqrt{T}}$$
$$d_2 = d_1 - \sigma \sqrt{T}$$
Where $\sigma$ is the volatility of the underlying asset.



## Calculus:
- Deterministic 
- Stochastic

## Markov Processes:
- Think of Markov Processes as an amnesiac. They only remember current state, forget all past state.
- Examples: 
- Going Shopping for Groceries
- Copy and Paste Clipboard on Computer

## Tasks Jan 7, 2023: 
- Review Calculus:
- Taylor Series
- Derivatives
- Chain Rule
- Learn First Order Differential Equations (Seperable only), Second Order Differential Equations
- Introduction to Differential Equations  William E. Boyce,  Richard C. DiPrima 
- Chapter 2.1, 2.2 (seperable equations), 2.3