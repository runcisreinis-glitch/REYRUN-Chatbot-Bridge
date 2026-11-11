#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
suite=tests/android-mobile
build="$(mktemp -d)"
trap 'rm -rf "$build"' EXIT
sdk="${ANDROID_HOME:?Android SDK required}"
platform="$sdk/platforms/android-35/android.jar"
tools="$sdk/build-tools/35.0.0"
mkdir -p "$build/assets" "$build/classes" "$build/dex"
cp web/start/index.html "$build/assets/index.html"
"$tools/aapt2" link -I "$platform" --manifest "$suite/AndroidManifest.xml" -A "$build/assets" -o "$build/probe.apk"
javac --release 11 -cp "$platform" -d "$build/classes" "$suite/ProbeActivity.java"
jar cf "$build/probe.jar" -C "$build/classes" .
"$tools/d8" --min-api 30 --lib "$platform" --output "$build/dex" "$build/probe.jar"
(cd "$build/dex" && zip -q "$build/probe.apk" classes.dex)
"$tools/zipalign" -f 4 "$build/probe.apk" "$build/aligned.apk"
keytool -genkeypair -alias smoke -keyalg RSA -keystore "$build/test.p12" -storepass android -keypass android -validity 1 -dname 'CN=Ephemeral Android smoke'
"$tools/apksigner" sign --ks "$build/test.p12" --ks-pass pass:android --out "$build/signed.apk" "$build/aligned.apk"
adb install -r "$build/signed.apk"
adb logcat -c
adb shell input keyevent KEYCODE_WAKEUP
adb shell wm dismiss-keyguard
adb shell am start -W -n org.reyrun.mobiletest/.ProbeActivity
python3 "$suite/verify.py" web/start/index.html
