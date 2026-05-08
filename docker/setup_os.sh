#!/bin/bash

set -euo pipefail

haf_admin_unix_account="haf_admin"

while [ $# -gt 0 ]; do
  case "$1" in
    --haf-admin-account=*)
      haf_admin_unix_account="${1#*=}"
      ;;
    --help)
      exit 0
      ;;
    *)
      ;;
  esac
  shift
 done

if id "$haf_admin_unix_account" >/dev/null 2>&1; then
  exit 0
fi

useradd -ms /bin/bash -c "HAF admin account" "$haf_admin_unix_account"
