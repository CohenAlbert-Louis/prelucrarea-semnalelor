import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tools.sm_exceptions import ConvergenceWarning
import warnings

warnings.simplefilter('ignore', ConvergenceWarning)

def trend_component(x):
    return (x*x-250*x+125*125)/1000

def seasonal_component(x):
    return x * np.sin(2 * np.pi * x / 12)/30

def residual_component(size):
    return np.random.normal(0, 2, size)

def exp_med(data,alpha):
    result = np.zeros_like(data)
    result[0] = data[0]
    for t in range(1, len(data)):
        for k in range(1,t):
            result[t]+=(1-alpha)**(t-k)*data[k]
        result[t]*=alpha
        result[t]+=(1-alpha)**t*data[0]
    return result

np.random.seed(0)
time = np.arange(0, 360)
trend = trend_component(time)
seasonal = seasonal_component(time)
residual = residual_component(len(time))
data = trend + seasonal + residual

fig,axs = plt.subplots(4)

axs[0].plot(time,data, label='Observed Data')
axs[1].plot(time,trend, label='Trend Component')
axs[2].plot(time,seasonal, label='Seasonal Component')
axs[3].plot(time,residual, label='Residual Component')

fig2,axs2 =  plt.subplots(4)

axs2[0].plot(time,data,label='Original')
axs2[1].plot(time,exp_med(data,0.1),label='ME alpha=0.1')
axs2[2].plot(time,exp_med(data,0.3),label='ME alpha=0.3')
axs2[3].plot(time,exp_med(data,0.5),label='ME alpha=0.5')

exp_med_array = [exp_med(data,i/100) for i in range(1,100)]
mean_errors = [sum((data-exp_med_array[i])**2) for i in range(len(exp_med_array))]

optimal_alpha_pos = np.argmin(mean_errors)

fig3,axs3=plt.subplots(1)

fig3.suptitle(f'Optimal alpha: {(optimal_alpha_pos+1)/100:.2f} with MSE: {mean_errors[optimal_alpha_pos]/len(data):.2f}')
axs3.plot(time,exp_med_array[optimal_alpha_pos])

eps_sum=[]

for horiz in range(5,15):
    model = ARIMA(data,order=(0,0,horiz),enforce_stationarity=False,enforce_invertibility=False)
    results = model.fit()

    eps_sum.append(sum(results.resid**2))

optimal_theta_pos = np.argmin(eps_sum)
print(f"Optimal MA horizon: {optimal_theta_pos+1}, MSE: {eps_sum[optimal_theta_pos]/len(data):.2f}")

optimal_AIC = float('inf')
optimal_args = (0,0)

for p in range(20):
    for q in range(20):
        model = ARIMA(data,order=(p,0,q),enforce_stationarity=False,enforce_invertibility=False)
        results = model.fit(method_kwargs={"maxiter":20}) # for faster exec
        if results.aic< optimal_AIC: # AIC = Akaike Information Criterion (2k-2ln(L) - k = nr est params, L = MLE)
            optimal_AIC=results.aic
            optimal_args=(p,q)
    print(".",end="") # progress bar
        
fig4,axs4=plt.subplots(1)

fig4.suptitle(f'Optimal ARIMA: {optimal_args}')
model = ARIMA(data,order=(optimal_args[0],0,optimal_args[1]),enforce_stationarity=False,enforce_invertibility=False)
results = model.fit()
axs4.plot(time,results.fittedvalues)

plt.show()