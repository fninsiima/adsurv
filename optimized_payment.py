import csv
import os,sys,getopt

"""USE PYTHON 3"""

def payout(reports,min_range,rate,prev_pay, network):
	if network == "MTN":
		final_payout = ((int(reports) - int(min_range)) * int(rate)) + int(prev_pay) + 640
	elif network == "AIRTEL":
		final_payout = ((int(reports) - int(min_range)) * int(rate)) + int(prev_pay) + 550
	else:
		final_payout = ((int(reports) - int(min_range)) * int(rate)) + int(prev_pay)
	return final_payout

def calc(local_li, min_range, max_range, rate, prev_pay_factor_1, prev_pay_factor_2):

	l = local_li
	prev_pay = prev_pay_factor_1 + prev_pay_factor_2;
	prev_pay_factor_1 = prev_pay;
	prev_pay_factor_2 = prev_pay_factor_2 + 1000;

	if remote_arr.count(l[1])>min_range and remote_arr.count(l[1])<max_range:
		pay = payout(remote_arr.count(l[1]), min_range, rate, prev_pay, l[6]);
		mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])

	else:
		calc(l, min_range + 40, max_range + 40, rate + 25, prev_pay_factor_1, prev_pay_factor_2)

def main(local_file,remote_file):
	local = csv.reader(open(local_file))
	remote = csv.reader(open(remote_file))
	next(local)

	for r in remote:
		remote_arr.append(r[8])
	for l in local:
		if remote_arr.count(l[1])>0:
			if remote_arr.count(l[1])<21:
				if l[6] == "MTN":
					pay = 5000 + 640
				elif l[6] == "AIRTEL":
					pay = 5000 + 550
				else:
					pay = 5000
				mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
			elif remote_arr.count(l[1])>20 and remote_arr.count(l[1])<61:
				pay = payout(remote_arr.count(l[1]), 20, 150, 5000, l[6])
				mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
			else:
				min_range = 20
				max_range = 61
				rate = 150
				prev_pay_factor_1 = 5000
				prev_pay_factor_2 = 6000
				calc(l, min_range + 40, max_range + 40, rate + 25, prev_pay_factor_1, prev_pay_factor_2)
		else:
			pass
		#sub.writerow([l[0], l[1], l[3], remote_arr.count(l[1])])

if __name__=='__main__':
	if len(sys.argv) == 3:
		local_file = sys.argv[1]
		remote_file = sys.argv[2]
	else:
		local_file = 'finallocallist.csv'
		remote_file = 'adsurv_18_06_t0_24_06.csv'

	mmoney = csv.writer(open('Payment.csv','a', newline=''))
	mmoney.writerow(
		["Amount to credit", "Beneficiary account number", 
		"Beneficiary name", "Account type", "beneficiary email address", "Number of Reports"]
		)
	local_arr = []
	remote_arr = []

	main(local_file,remote_file)