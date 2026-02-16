[app]
title = SARA
package.name = sara_project
package.domain = org.anif
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0.0
requirements = python3,kivy,requests
orientation = portrait
fullscreen = 1
android.permissions = INTERNET

[android]
api = 35
minapi = 21
ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
