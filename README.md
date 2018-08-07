Reward adhoc participants with monetary incentive.

Takes in a csv file of submissions and for each participant submission, calculates the reward.

Uses a cumulative model to reward those who send more reports with more cash.

Baseline charge for minimum number of reports is 5000 UGX.\ 
Extra reports sent in the range [20 - 60] cost 150 UGX each.<br/>
Extra reports sent in the range [60 - 100] cost (150 + 25 = 175/-) UGX each.
And so on and so forth.

Base charges for Yo Payment transfer charges.\
MTN - 650\
Airtel - 550\
Others - None

DEPENDENCIES:
python3 and the csv module

Run: python3 optimized_payment.py path_to_local_file path_to_remote_file

where
- path_to_local_file is a csv consisting of participants details
- path_to_remote_file is a csv generated from exporting submissions using ODK Aggregate

