import familiar
from scipy.stats import ttest_1samp, ttest_ind, chi2_contingency

# Task 2: Get lifespans of Vein Pack subscribers
vein_pack_lifespans = familiar.lifespans(package='vein')

# Task 4: Perform 1-Sample T-Test
vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)

# Task 5 & 6: Check significance and print results
if vein_pack_test.pvalue < 0.05:
    print("The Vein Pack Is Proven To Make You Live Longer!")
else:
    print("The Vein Pack Is Probably Good For You Somehow!")

# Task 7: Get lifespans of Artery Pack subscribers
artery_pack_lifespans = familiar.lifespans(package='artery')

# Task 9: Perform 2-Sample T-Test
package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)

# Task 10: Check significance and print results
if package_comparison_results.pvalue < 0.05:
    print("The Artery Package guarantees even stronger results!")
else:
    print("The Artery Package is also a great product!")

# Task 12: Get iron counts data
iron_contingency_table = familiar.iron_counts_for_package()

# Task 14: Perform Chi-Squared Test
_, iron_pvalue, _, _ = chi2_contingency(iron_contingency_table)

# Task 15: Check significance and print results
if iron_pvalue < 0.05:
    print("The Artery Package Is Proven To Make You Healthier!")
else:
    print("While We Can't Say The Artery Package Will Help You, I Bet It's Nice!")
