[app]
title = MHB Inspection
package.name = mhbinspection
package.domain = org.mhb
source.dir = .
source.include_exts = py,kv,html,css,js,json,png,jpg,jpeg,gif,ttf,otf,db
version = 1.0.0

requirements = python3,kivy,kivymd,flask,reportlab,python-docx,jdatetime,arabic-reshaper,requests,python-bidi

orientation = portrait
fullscreen = 0

[buildozer]
android.api = 30
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
p4a.branch = master
log_level = 2
