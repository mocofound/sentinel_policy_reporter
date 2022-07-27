# sentinel_policy_reporter.py

## Description
Run this python script to output a report of Sentinel Policy Checks for Terraform Cloud
## Install
```
pip3 install terrasnek==0.1.10
```
## How to Use
```
export TFC_URL="https://app.terraform.io"
export TFC_TOKEN="your-tfc-org-token"
export TFC_ORGANIZATION="your-tfc-org"

python3 sentinel_policy_reporter.py
```
## Compatability
Compatable | Terraform Cloud

Compatable | Terraform Enterprise

## Example Output
```
python3 sentinel_policy_reporter.py

Workspace Name: learn-terraform-aws-control-tower-aft

        Workspace ID: ws-fn6TXZNHqccs4yiq

         Run ID: run-eqfAb5BJi4gvA57g    |    Created At: 2022-07-05T17:18:17.654Z
                 No Sentinel Policy Checks Performed

Workspace Name: hashicat-azure

        Workspace ID: ws-akAKfDQE5JP4kVWX

         Run ID: run-MNd86aKabNADaHMp    |    Created At: 2022-06-29T17:11:48.021Z
                polchk-kp5YHbjDjCPykt69
                        Passed Sentinel Policy Checks: True
         Run ID: run-vEBKFtBaXydFyaEz    |    Created At: 2022-06-29T15:54:32.522Z
                polchk-89prCHbSekSRLQfP
                        Passed Sentinel Policy Checks: True
         Run ID: run-ip9ACpSEbAUpD7qN    |    Created At: 2022-06-29T15:29:18.601Z
                polchk-q65HYVjJKJPLsAj3
                        Passed Sentinel Policy Checks: False
                        Total Policy Failures: 4
                                False >  Policy Name: azure-specific-governance/enforce-mandatory-tags
                                True >  Policy Name: azure-specific-governance/restrict-aks-clusters
                                True >  Policy Name: azure-specific-governance/restrict-app-service-to-https
                                False >  Policy Name: azure-specific-governance/restrict-inbound-source-address-prefixes
                                True >  Policy Name: azure-specific-governance/restrict-outbound-destination-address-prefixes
                                True >  Policy Name: azure-specific-governance/restrict-publishers-of-current-vms
                                False >  Policy Name: azure-specific-governance/restrict-vm-image-id
                                True >  Policy Name: azure-specific-governance/restrict-vm-publisher
                                False >  Policy Name: azure-specific-governance/restrict-vm-size
```
