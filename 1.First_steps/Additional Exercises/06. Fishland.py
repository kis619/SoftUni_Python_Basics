price_skumruia = float(input())
price_caca = float(input())
palamud = float(input())
safrid = float(input())
mussles = int(input())

price_palamud = 1.6 * price_skumruia
price_safrid = 1.8 * price_caca
price_mussles = 7.5

money_needed = palamud * price_palamud + safrid * price_safrid + mussles * 7.5
print(f"{money_needed:.2f}")