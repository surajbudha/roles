# Allow a token to read secrets
path "kv/*" {
    capabilities = ["read", "list"]
}