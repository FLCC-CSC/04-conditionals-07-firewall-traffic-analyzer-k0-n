# FILE NAME - firewall_traffic_analyzer.py

# NAME: Josh Fielding       
# DATE: 10/5/25
# BRIEF DESCRIPTION: Consider two pieces of data to make a risk analysis


# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print("=== Network Traffic Security Analyzer ===\n")

# prompt user for inputs
port = int(input("Enter the port number (e.g., 80, 22, 443, 3389): "))
transfer_size = int(input("Enter the data transfer size in megabytes (MB): "))

# determine risk assessment
if (port == 22 or port == 3389) and transfer_size >= 100:
    risk_assessment = "HIGH RISK: Potential unauthorized remote access detected!"
elif port == 80 and transfer_size > 100:
    risk_assessment = "MEDIUM RISK: Large unencrypted data transfer detected."
elif port == 443:
    risk_assessment = "LOW RISK: Secure encrypted transfer detected."
else:
    risk_assessment = "UNKNOWN: Unrecognized traffic pattern."

# output firewall log
print("\nFIREWALL LOG:")
print(f"Port: {port}, Transfer Size: {transfer_size} MB")
print(f"Risk Assessment: {risk_assessment}")
print("------------------------")

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 80
Enter the data transfer size in megabytes (MB): 120

FIREWALL LOG:
Port: 80, Transfer Size: 120 MB
Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 22
Enter the data transfer size in megabytes (MB): 12

FIREWALL LOG:
Port: 22, Transfer Size: 12 MB
Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 443
Enter the data transfer size in megabytes (MB): 1024

FIREWALL LOG:
Port: 443, Transfer Size: 1024 MB
Risk Assessment: LOW RISK: Secure encrypted transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 1725
Enter the data transfer size in megabytes (MB): 234567

FIREWALL LOG:
Port: 1725, Transfer Size: 234567 MB
Risk Assessment: UNKNOWN: Unrecognized traffic pattern.
------------------------
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Did you get tripped up using the `or` or `and` operators? If so, how?

Yes, I used 'and' between two port numbers, which didnt work because a port cant be both 22 and 3389.
'or' is meant to be used for ports and the 'and' operator is meant for the file sizes.





'''
