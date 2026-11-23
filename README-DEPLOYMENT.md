# ANTVERSE Ethereum replica deployment (NOT YET VERIFIED)

BSC reference: `0xf9FA938a18D73246298ef99C7d6D75DCA7Eb2A48`

## Requirements
- Foundry (forge, cast), Python 3
- BSC and Ethereum RPC endpoints
- Etherscan V2 API key

## Workflow
1. Copy `.env.example` to `.env` and fill RPC/API settings. Never commit secrets.
2. `set -a; source .env; set +a`
3. `python3 scripts/fetch-bsc-source.py`
4. Extract all original source files and compiler settings from `reference/bsc-source-metadata.json`; audit external dependencies, proxies, mint permissions, initial supply and constructor arguments.
5. Rebuild with the **same compiler and optimizer settings**. Compare compiled deployed runtime bytecode against `cast code 0xf9FA938a18D73246298ef99C7d6D75DCA7Eb2A48 --rpc-url "$BSC_RPC_URL"`, accounting explicitly for immutables, metadata, and linked libraries.
6. `bash scripts/inspect-address.sh` checks if the desired Ethereum address is occupied.
7. Determine original deployment transaction, factory/deployer and nonce or CREATE2 salt and init code. For CREATE2, compute `keccak256(0xff ++ factory ++ salt ++ keccak256(init_code))[12:]`; it must equal the target address. If no valid deployment path exists, the same address cannot be promised.
8. Only after verified source, tests and address feasibility, add a contract-specific deployment script and run Sepolia tests. Do not mint a duplicate supply on Ethereum if cross-chain shared supply is intended.
9. Deploy on Ethereum only after explicit review and authorization, then verify with Etherscan using the exact source, compiler, optimizer, constructor arguments and libraries.

## Current blockers
Original verified source and deploy transaction not yet obtained. No Ethereum contract has been deployed. No tokens have been minted.
