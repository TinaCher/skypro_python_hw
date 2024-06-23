def bank(X, Y):
    deposit = X  
    annual_interest_rate = 0.10  
    
    for _ in range(Y):
        deposit += deposit * annual_interest_rate  # 10% deposit increase
    
    return deposit

# Example
X = 1000  
Y = 5  

result = bank(X, Y)
print(f"Amount of money on the account after {Y} years: {result:.2f} dollars")
