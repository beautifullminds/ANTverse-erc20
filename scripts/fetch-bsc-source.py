#!/usr/bin/env python3
"""Fetch verified BSC source metadata using Etherscan API V2 (chainid 56).
Do not interpret successful retrieval as bytecode equivalence.
"""
import json, os, urllib.parse, urllib.request
address="0xf9FA938a18D73246298ef99C7d6D75DCA7Eb2A48"
key=os.environ["ETHERSCAN_API_KEY"]
url="https://api.etherscan.io/v2/api?"+urllib.parse.urlencode({
"chainid":"56","module":"contract","action":"getsourcecode","address":address,"apikey":key})
with urllib.request.urlopen(url, timeout=30) as response:
    result=json.load(response)
if result.get("status")!="1" or not result.get("result"):
    raise SystemExit("Source lookup failed: "+str(result))
metadata=result["result"][0]
if not metadata.get("SourceCode"):
    raise SystemExit("No verified source available from API")
os.makedirs("reference",exist_ok=True)
with open("reference/bsc-source-metadata.json","w") as f:
    json.dump(metadata,f,indent=2)
print("Saved reference/bsc-source-metadata.json")
print("Compiler:",metadata.get("CompilerVersion"))
print("Contract:",metadata.get("ContractName"))
print("Proxy:",metadata.get("Proxy"))
print("Implementation:",metadata.get("Implementation"))
print("NEXT: extract source, review imports and constructor args, compile and compare deployed runtime bytecode.")
