import csv

def payout(reports,min_range,rate,prev_pay, network):
	if network == "MTN":
		final_payout = ((int(reports) - int(min_range)) * int(rate)) + int(prev_pay) + 640
	elif network == "AIRTEL":
		final_payout = ((int(reports) - int(min_range)) * int(rate)) + int(prev_pay) + 550
	else:
		final_payout = ((int(reports) - int(min_range)) * int(rate)) + int(prev_pay)
	return final_payout

local = csv.reader(open('finallocallist.csv'))
remote = csv.reader(open('adsurv_18_06_t0_24_06.csv'))
next(local)
# sub = csv.writer(open('Submissions.csv','a', newline=''))
mmoney = csv.writer(open('Payment.csv','a', newline=''))
mmoney.writerow(
	["Amount to credit", "Beneficiary account number", 
	"Beneficiary name", "Account type", "beneficiary email address", "Number of Reports"]
	)
local_arr = []
remote_arr = []

# count = 1
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
		elif remote_arr.count(l[1])>60 and remote_arr.count(l[1])<101:
			pay = payout(remote_arr.count(l[1]), 60, 175, 11000, l[6])
			mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
		elif remote_arr.count(l[1])>100 and remote_arr.count(l[1])<141:
			pay = payout(remote_arr.count(l[1]), 100, 200, 18000, l[6])
			mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
		elif remote_arr.count(l[1])>140 and remote_arr.count(l[1])<181:
			pay = payout(remote_arr.count(l[1]), 140, 225, 26000, l[6])
			mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
		elif remote_arr.count(l[1])>180 and remote_arr.count(l[1])<221:
			pay = payout(remote_arr.count(l[1]), 180, 250, 35000, l[6])
			mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
		elif remote_arr.count(l[1])>220 and remote_arr.count(l[1])<261:
			pay = payout(remote_arr.count(l[1]), 220, 275, 45000, l[6])
			mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
		elif remote_arr.count(l[1])>260 and remote_arr.count(l[1])<301:
			pay = payout(remote_arr.count(l[1]), 260, 300, 56000, l[6])
			mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
		elif remote_arr.count(l[1])>300 and remote_arr.count(l[1])<341:
			pay = payout(remote_arr.count(l[1]), 300, 325, 68000, l[6])
			mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
		elif remote_arr.count(l[1])>340 and remote_arr.count(l[1])<381:
			pay = payout(remote_arr.count(l[1]), 340, 350, 81000, l[6])
			mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
		elif remote_arr.count(l[1])>380 and remote_arr.count(l[1])<421:
			pay = payout(remote_arr.count(l[1]), 380, 375, 95000, l[6])
			mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
		elif remote_arr.count(l[1])>420 and remote_arr.count(l[1])<461:
			pay = payout(remote_arr.count(l[1]), 420, 400, 110000, l[6])
			mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
		elif remote_arr.count(l[1])>460 and remote_arr.count(l[1])<501:
			pay = payout(remote_arr.count(l[1]), 460, 425, 126000, l[6])
			mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
		elif remote_arr.count(l[1])>500 and remote_arr.count(l[1])<541:
			pay = payout(remote_arr.count(l[1]), 500, 450, 143000, l[6])
			mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
		elif remote_arr.count(l[1])>540 and remote_arr.count(l[1])<581:
			pay = payout(remote_arr.count(l[1]), 540, 475, 161000, l[6])
			mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
		elif remote_arr.count(l[1])>580 and remote_arr.count(l[1])<621:
			pay = payout(remote_arr.count(l[1]), 580, 500, 180000, l[6])
			mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
		elif remote_arr.count(l[1])>620 and remote_arr.count(l[1])<661:
			pay = payout(remote_arr.count(l[1]), 620, 525, 200000, l[6])
			mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
		elif remote_arr.count(l[1])>660 and remote_arr.count(l[1])<701:
			pay = payout(remote_arr.count(l[1]), 660, 550, 221000, l[6])
			mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
		elif remote_arr.count(l[1])>700 and remote_arr.count(l[1])<741:
			pay = payout(remote_arr.count(l[1]), 700, 575, 243000, l[6])
			mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
		elif remote_arr.count(l[1])>740 and remote_arr.count(l[1])<781:
			pay = payout(remote_arr.count(l[1]), 740, 600, 266000, l[6])
			mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
		elif remote_arr.count(l[1])>780 and remote_arr.count(l[1])<821:
			pay = payout(remote_arr.count(l[1]), 780, 625, 290000, l[6])
			mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
		elif remote_arr.count(l[1])>820 and remote_arr.count(l[1])<841:
			pay = payout(remote_arr.count(l[1]), 820, 650, 315000, l[6])
			mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
		elif remote_arr.count(l[1])>840 and remote_arr.count(l[1])<881:
			pay = payout(remote_arr.count(l[1]), 840, 675, 341000, l[6])
			mmoney.writerow([pay, l[5], l[3], "Mobile Money", "", remote_arr.count(l[1])])
		else:
			pass
	else:
		pass
	#sub.writerow([l[0], l[1], l[3], remote_arr.count(l[1])])

