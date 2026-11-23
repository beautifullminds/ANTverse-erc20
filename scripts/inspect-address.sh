#!/usr/bin/env bash
set -euo pipefail
: "${ETH_RPC_URL:?Set ETH_RPC_URL}"
TARGET=0xf9FA938a18D73246298ef99C7d6D75DCA7Eb2A48
echo "Ethereum chain ID:"
cast chain-id --rpc-url "$ETH_RPC_URL"
echo "Code at requested Ethereum address:"
CODE=$(cast code "$TARGET" --rpc-url "$ETH_RPC_URL")
if [ "$CODE" != "0x" ]; then
  echo "ADDRESS OCCUPIED: $TARGET"
  exit 2
fi
echo "Address has no deployed code. This does NOT establish deterministic deployment feasibility."
