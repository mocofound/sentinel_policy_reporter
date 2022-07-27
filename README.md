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
