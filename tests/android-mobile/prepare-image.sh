#!/usr/bin/env bash
# The SDK manager's unverified streamed Google APIs image failed before emulator startup.
# Install Google's smaller stock Android 15 image, verified against the complete published archive.
set -euo pipefail
image_url='https://dl.google.com/android/repository/sys-img/android/x86_64-35_r02.zip'
expected_sha256='6dd7de33e63ef105cf2fabea6badda1dbe7665c96d8908e5f6e1407e63ff4556'
package_dir="${ANDROID_HOME:?Android SDK required}/system-images/android-35/default"
temp_dir="$(mktemp -d)"
trap 'rm -rf "$temp_dir"' EXIT
for attempt in 1 2 3; do
  if curl --fail --location --silent --show-error --retry 2 --max-time 300 \
       "$image_url?download=android-35-r2-$attempt" --output "$temp_dir/image.zip" &&
     printf '%s  %s\n' "$expected_sha256" "$temp_dir/image.zip" | sha256sum --check --status; then
    mkdir -p "$package_dir"
    unzip -qo "$temp_dir/image.zip" -d "$package_dir"
    test -s "$package_dir/x86_64/source.properties"
    test -s "$package_dir/x86_64/system.img"
    echo "Verified Android 15 API 35 OS archive SHA-256 $expected_sha256"
    exit 0
  fi
  echo "System image could not be verified on attempt $attempt" >&2
done
exit 1
