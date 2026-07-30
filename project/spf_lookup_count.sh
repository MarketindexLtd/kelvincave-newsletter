#!/bin/bash
# Count the DNS-lookup terms in a domain's SPF record and print the include tree.
#
# SPF allows a maximum of 10 DNS lookups (RFC 7208 s4.6.4). Exceeding it makes the record
# invalid - which does not just break the new sender, it breaks SPF for ALL of the domain's
# mail. Run this BEFORE adding an include to someone's SPF record, and again after.
#
# Usage: ./spf_lookup_count.sh kelvincave.com
#
# kelvincave.com was at 7/10 on 2026-07-30; adding include:spf.brevo.com (a flat ip4 list,
# no nested includes) takes it to 8/10. See BREVO-SETUP.md section 3a.

[ -z "$1" ] && { echo "usage: $0 <domain>"; exit 1; }

count=0

walk() {
  local dom="$1" depth="$2" rec term
  rec=$(dig +short TXT "$dom" | tr -d '"' | grep -m1 '^v=spf1')
  if [ -z "$rec" ]; then
    printf "%*s%s -> NO SPF RECORD\n" $((depth * 2)) "" "$dom"
    return
  fi
  printf "%*s%s\n" $((depth * 2)) "" "$dom"
  for term in $rec; do
    case "$term" in
      include:*)  count=$((count + 1)); walk "${term#include:}" $((depth + 1)) ;;
      redirect=*) count=$((count + 1)); walk "${term#redirect=}" $((depth + 1)) ;;
      # a, mx, ptr and exists each cost one lookup but do not nest further.
      a|mx|ptr|a:*|mx:*|exists:*)
        count=$((count + 1))
        printf "%*s%s (1 lookup)\n" $(((depth + 1) * 2)) "" "$term" ;;
    esac
  done
}

walk "$1" 0
echo "---- total DNS-lookup terms: $count (limit 10) ----"
[ "$count" -gt 10 ] && echo "!! OVER THE LIMIT - this record is invalid and breaks all mail for the domain"
exit 0
