import pandas as pd

# Read in a data file
df = pd.read_csv('data/raw/shopping_behavior_updated.csv')

# calculate summary statistics on the Purchase Amount column
# TODO: Is there a way to encapsulate all this functionality
# TODO: in one function call?
# Let's use .agg function

purchase_amount_sum_stats = df.agg({'Purchase Amount (USD)' : ['mean', 'median', 'max', 'min', 'std']})

print(purchase_amount_sum_stats)

# calculate summary statistics on the Age column
# TODO: Is there a way to encapsulate all this functionality
# TODO: in one function call?

print("\n")

age_sum_stats = df.agg({'Age' : ['mean', 'median', 'max', 'min', 'std']})

print(age_sum_stats)

print("\n")

# summary statistics
# TODO: is there another function we can use to calculate metrics on groups?

season_grouped = df.groupby('Season')['Purchase Amount (USD)']

sum_stats_purchase_by_season = season_grouped.agg(['mean', 'median', 'max', 'min', 'std'])

print(sum_stats_purchase_by_season)

# # keep all columns except for "Customer", & "Discount Applied"
# # TODO: is there a more efficient way to exclude columns in your dataset?

df1 = df.drop(['Customer ID', 'Discount Applied'], axis=1)

# There is no column named "Customer", there is however "Customer ID" however that seems like an important row to keep

# figure out most popular payment method in NY
# TODO: is there anyway we could modularize this behavior to apply to all
# TODO: possible states? (OR possibly use a pandas function that does this
# TODO: for us already?)

# payment_methods = df['Payment Method'].unique()
# ny = df[df.Location == "New York"]

# most_frequent_method = {}

# for method in payment_methods:
#     most_frequent_method[method] = len(ny[ny['Payment Method'] == method])

# print(most_frequent_method)

# # Write this updated data out to csv file
# df.to_csv('data/processed/cleaned_data.csv', index=False)
