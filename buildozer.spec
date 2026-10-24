[app]

# (str) Title of your application
title = Smart Steward

# (str) Package name
package.name = smartsteward

# (str) Package domain (needed for android packaging)
package.domain = org.example

# === 關鍵：請確保這裡有設定版本 ===
version = 0.1

# (str) Source files where the let's go (relative to directory of spec)
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3==3.11,kivy

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# -----------------------------------------------------------------------
# 關鍵修正：鎖定穩定的 Android SDK、API 與 NDK 版本（解決編譯崩潰問題）
# -----------------------------------------------------------------------

# Target android API, should be as high as possible.
android.api = 33

# Minimum API your APK will support.
android.minapi = 21

# Android NDK version to use
android.ndk = 25b

# Android arch to build for, 
android.archs = arm64-v8a

# (bool) Automatically accept SDK license
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1