import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import sklearn.metrics as r2_score



data = {
    'age':[1,1,1,1,1,1,
         2,2,2,2,2,2,
         3,3,3,3,3,3,
         4,4,4,4,4,4,
         5,5,5,5,5,5,
         6,6,6,6,6,6],
    'price':[18000,18000,18000,18000,18000,18000,   # avg : 17950   # differnce one ye old : 2000
            17500,17500,17500,17500,17500,17500,
            17000,17000,17000,17000,17000,17000,
            16500,16500,16500,16500,16500,16500,
            16000,16000,16000,16000,16000,16000,
            15500,15500,15500,15500,15500,15500]
}
# 30 data - 20 data - 
# 10 test data. 
# actual result 
#  prediction
#  actual vs predicted - r2 score   : 1 (100%), near to 1, towards 0 : worst model
plt.figure(figsize=(10,6))
plt.scatter(data['age'], data['price'], color='blue')
plt.title('Car Price vs Age')
plt.xlabel('Age (years)')
plt.ylabel('Price ($)')
plt.grid()
plt.show()


#  line  = mx + b
# m = slope
# -2000(x)+20000
# y = -2000x + 20000
# y = -2000 * age + 20000
# y = -2000 * 4 + 20000
# y = -8000 + 20000
# y = 12000

# if age is 8
# y = -2000 * 8 + 20000
# y = -16000 + 20000
# y = 4000

model = LinearRegression()
df = pd.DataFrame(data)
model.fit(df[['age']], df[['price']])

slope = model.coef_[0][0]
intercept = model.intercept_[0]
print(f"Slope: {slope}, Intercept: {intercept}")

price_pred = model.predict(df[['age']])

r2 = r2_score.r2_score(df[['price']], price_pred)
print(f"R² Score: {r2}")
