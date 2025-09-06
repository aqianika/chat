[app]
# عنوان برنامه
title = SecureChat Pro

# نام پکیج
package.name = securechatpro

# دامنه پکیج
package.domain = com.securechat

# مسیر سورس
source.dir = .

# پسوندهای فایل‌های شامل
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf

# پترن فایل‌های شامل
source.include_patterns = assets/*,images/*,*.kv,fonts/*

# نسخه برنامه
version = 1.0

# نسخه کد
version.code = 1

# نویسنده
author = SecureChat Team

# کتابخانه‌های مورد نیاز
requirements = 
    python3,
    kivy==2.2.0,
    plyer==2.1.0,
    requests==2.31.0,
    android,
    openssl

# مجوزهای اندروید
android.permissions = 
    INTERNET,
    ACCESS_FINE_LOCATION,
    ACCESS_COARSE_LOCATION,
    READ_EXTERNAL_STORAGE,
    WRITE_EXTERNAL_STORAGE,
    READ_CONTACTS,
    ACCESS_NETWORK_STATE,
    WAKE_LOCK

# ویژگی‌های اندروید
android.features = 
    android.hardware.location,
    android.hardware.location.gps,
    android.hardware.location.network

# API اندروید
android.api = 28

# حداقل API
android.minapi = 21

# نسخه SDK هدف
android.sdk = 28

# نسخه NDK
android.ndk = 23b

# معماری‌های پشتیبانی شده
android.arch = armeabi-v7a, arm64-v8a

# دستور راه‌اندازی
android.entrypoint = org.kivy.android.PythonActivity

# آیکون برنامه
# icon.filename = assets/icon.png

# لوگو برنامه
# logo.filename = assets/logo.png

# جهت صفحه
orientation = portrait

# حالت نمایش
fullscreen = 0

# جلوگیری از خوابیدن صفحه
wake_lock = 1

# نگه داشتن برنامه در پس‌زمینه
keep_screen_on = 1

# لاگ‌گیری
log_level = 2

# حذف فایل‌های موقت
android.clean_build_before_distribute = 1

# بهینه‌سازی بیلد
android.build_tools_override = 30.0.3

# قوانین صرافی
android.allow_backup = true
android.allow_revert = false

# متادیتاهای اضافی
android.meta_data = 
    com.google.android.gms.version=@integer/google_play_services_version

# سرویس‌های گوگل پلی
android.gradle_dependencies = 
    com.google.android.gms:play-services-location:21.0.1

# قوانین intent فیلتر
android.intent_filters = 
    <intent-filter>
    <action android:name="android.intent.action.MAIN" />
    <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>

# تنظیمات بوسترپ
presplash.filename = assets/presplash.png
presplash.color = #2962FF

# بکند Kivy
graphics = opengl

# شتاب‌دهی گرافیکی
graphics.accelerated = 1

# خطوط چندضلعی
graphics.polygon_offset = 1

# عمق بافر
graphics.depth_size = 16

# الگوی رنگی
graphics.rgba_size = 32

# نمونه‌گیری
graphics.multisamples = 2

# تنظیمات پایتون
python.version = 3.9
python.optimize = 1
python.ndk = 3.9
python.android_version = 3.9

# بسته‌های اضافی
p4a.branch = master
p4a.local_recipes = recipes

# حذف کتابخانه‌های اضافی
android.strip = false
android.no_strip = false

# امضای دیجیتال
android.release_artifact = .apk
android.debug_artifact = .apk

# کلید انحصاری
# android.keystore = release.keystore
# android.keystore_password = password
# android.keyalias = keyalias
# android.keyalias_password = password