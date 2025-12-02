import scipy
import matplotlib.pyplot as plt
import numpy as np

def trend_component(x):
    return 0.00002*x**2-0.0001*x

def seasonal_component(x):
    return 10 * np.sin(np.pi*x/12)+8*np.sin(np.pi*x/15)

def noise_component(x):
    return np.random.normal(0, 2, size=len(x))

def generate_time_series(length):
    x = np.arange(length)
    trend = trend_component(x)
    seasonal = seasonal_component(x)
    noise = noise_component(x)
    return (trend+seasonal+noise,trend,seasonal,noise)

def autocorr(x):
    return np.correlate(x, x, mode='same')

def AR_prediction(x,p,predict_steps):
    from statsmodels.tsa.ar_model import AutoReg #auto AR fitting from statsmodels
    model = AutoReg(x, lags=p)
    model_fit = model.fit()
    return model_fit.predict(start=len(x), end=len(x)+predict_steps)

def avg_error(real,pred):
    return np.mean(np.abs(real-pred))


(ts_full,trend_full,seas_full,ns_full) = generate_time_series(2000) #for verifications with AR predictions later
(ts,trend,seas,ns) = (ts_full[:1000],trend_full[:1000],seas_full[:1000],ns_full[:1000])

fig,axs=plt.subplots(4)

axs[0].plot(ts)
axs[0].set_title('Original Time Series')

axs[1].plot(trend)
axs[1].set_title('Trend Component')

axs[2].plot(seas)
axs[2].set_title('Seasonal Component')

axs[3].plot(ns)
axs[3].set_title('Noise Component')

fig2,axs2=plt.subplots(1)

axs2.plot(autocorr(ts))

fig3,axs3 = plt.subplots(2)

axs3[0].plot(AR_prediction(ts, p=200,predict_steps=100))
axs3[0].set_title('AR 200')

axs3[1].plot(ts_full[1000:1101])
axs3[1].set_title('Original Time Series (continuation)')

min_err = float('inf')

for p in range(1,100):
    for m in range(1,10):
        curr_err = avg_error(ts_full[1000:1001+m],AR_prediction(ts,p=p,predict_steps=m))
        if curr_err<min_err:
            min_err = curr_err
            best_p = p
            best_m = m

print(f'Best p: {best_p}, Best m: {best_m}, with error: {min_err}')

plt.show()