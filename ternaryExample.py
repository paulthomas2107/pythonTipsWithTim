age = 25
smoke = True

# in line if else rather than if...else...if...else...
health = "Poor" if age > 60 or smoke else 'Good' if age < 30 else 'Fair'

print("Health:", health)
