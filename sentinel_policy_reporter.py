#!/usr/bin/python
import os
from terrasnek.api import TFC

import logging
import hashlib
import base64
import unittest
import binascii
import time
import terrasnek.exceptions

TFC_TOKEN = os.getenv("TFC_TOKEN", None)
TFC_URL = os.getenv("TFC_URL", None) 
TFC_ORGANIZATION = os.getenv("TFC_ORGANIZATION", None) 
api = TFC(TFC_TOKEN, url=TFC_URL)

api.set_org(TFC_ORGANIZATION)
all_workspaces = api.workspaces.list_all()
#print(all_workspaces["data"][0]["id"])
for workspace in all_workspaces["data"]:
    #print(workspace)
    print("\nWorkspace Name: " + workspace["attributes"]["name"]+ "\n")
    print("\tWorkspace ID: " + workspace["id"]+ "\n")
    all_workspace_runs = api.runs.list_all(workspace["id"])
    for run in all_workspace_runs["data"]:
        print("\t Run ID: " + run["id"] + "    |    Created At: " +run["attributes"]["created-at"])
        #print(str(run))
        all_run_policy_checks = api.policy_checks.list(run["id"])["data"]
        if all_run_policy_checks:
            for policy_check in all_run_policy_checks:
                print("\t\t" + policy_check["id"])
                shown_pol_check = api.policy_checks.show(policy_check["id"])["data"]
                try:
                    policy_check_result = shown_pol_check["attributes"]["result"]["result"]
                    print("\t\t\tPassed Sentinel Policy Checks: " + str(policy_check_result))
                    if policy_check_result == False:
                        print("\t\t\tTotal Policy Failures: " + str(shown_pol_check["attributes"]["result"]["total-failed"]))
                        if shown_pol_check["attributes"]["result"]["total-failed"] > 0:
                            #print("\t\t\t Policy Failure: " + str(((shown_pol_check["attributes"]["result"]["sentinel"])["data"]["azure-specific-governance"]["policies"][0]["policy"])))
                            for policy_set in (shown_pol_check["attributes"]["result"]["sentinel"])["data"]:
                                #print(str((shown_pol_check["attributes"]["result"]["sentinel"])["data"][policy_set]["policies"]))
                                for policy in ((shown_pol_check["attributes"]["result"]["sentinel"])["data"][policy_set]["policies"]):
                                    print("\t\t\t\t" + str(policy["result"]) + " >  Policy Name: " + str(policy["policy"]))
                                    #print("\t\t\t\t\t Policy Result: " + str(policy["result"]))
                                    #print("\t\t\t\t\t Policy Description: " + str(policy["trace"]["description"]))
                except Exception as e: print("Exception: " + str(e))
        else:
            print("\t\t No Sentinel Policy Checks Performed")
