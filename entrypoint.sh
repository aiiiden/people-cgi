#!/bin/sh

echo "🔹 락 파일 제거 중..."
rm -rf /var/www/html/ppllock  # 락 파일 제거

echo "🔹 Apache 실행..."
exec apache2ctl -D FOREGROUND  # Apache 실행
