#!/usr/bin/env sh
# Run in the Termux home folder: sh mobile-termux.sh
# Only writes a fresh test folder. No network calls or device permissions.
set -eu
umask 077
root=./REYRUN-test
if [ -L "$root" ]; then
  echo 'REYRUN-test must be a real directory, not a symbolic link.' >&2
  exit 2
fi
mkdir -p "$root"
run=$(mktemp -d "$root/run-XXXXXXXX")
printf 'REYRUN\nRīga\n' > "$run/request.txt"
set -- $(sha256sum < "$run/request.txt")
digest=$1
bytes=$(wc -c < "$run/request.txt" | tr -d ' ')
lines=$(wc -l < "$run/request.txt" | tr -d ' ')
printf '{"schema":"reyrun.mobile.receipt/1","id":"phone-test-01","action":"inspect-text","bytes":%s,"lines":%s,"sha256":"%s"}\n' "$bytes" "$lines" "$digest" > "$run/receipt.json"
cat "$run/receipt.json"
printf '%s\n' "$run/receipt.json" >&2
