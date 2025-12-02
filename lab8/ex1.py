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

def AR_prediction_exo(x,m,p,predict_steps):
    from statsmodels.tsa.ar_model import AutoReg
    model = AutoReg(x, lags=p, exog=m)
    model_fit = model.fit()
    return model_fit.predict(start=len(x), end=len(x)+predict_steps,exog_oos=m[-predict_steps-1:])

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

fig4,axs4 = plt.subplots(3)

axs4[0].plot(AR_prediction_exo(ts, m=trend, p=200, predict_steps=100))
axs4[0].set_title('AR 200 Trend Exo (m param)')
axs4[1].plot(AR_prediction_exo(ts, m=seas, p=200, predict_steps=100))
axs4[1].set_title('AR 200 Seasonal Exo (m param)')
axs4[2].plot(ts_full[1000:1101])
axs4[2].set_title('Original Time Series (continuation)')

plt.show()