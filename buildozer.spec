[app]

# (str) Title of your application
title = Currency Converter Pro

# (str) Package name
package.name = currencyconverterpro

# (str) Package domain (needed for android packaging)
package.domain = org.abdoudesigner

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,mp3,json

# (str) Application version
version = 1.0

# (list) Application requirements
# Added: requests, kivmob, and openssl for HTTPS support
requirements = python3, kivy==2.3.0, requests, urllib3, charset-normalizer, idna, certifi, kivmob, openssl

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE, AD_ID

# (int) Target Android API
android.api = 33

# (int) Minimum API
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# (list) Gradle dependencies for AdMob
android.gradle_dependencies = 'com.google.android.gms:play-services-ads:22.6.0'

# (list) Packaging options to prevent requests library conflicts
android.packaging_options = "META-INF/INDEX.LIST", "META-INF/LICENSE", "META-INF/NOTICE"

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) AdMob Application ID (Essential for KivMob)
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-3896006690470878~2043942153

# (bool) Use the custom logcat filter
android.copy_libs = 1

[buildozer]

# (int) Log level (2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1

