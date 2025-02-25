# 베이스 이미지 설정
FROM debian:latest

# 환경 설정
ENV DEBIAN_FRONTEND=noninteractive

# 필요한 패키지 설치
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        apache2 \
        libapache2-mod-perl2 \
        perl \
        bash \
        dos2unix \
        nano && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# CGI 실행을 위한 Apache 모듈 활성화
RUN a2enmod cgi
RUN a2enmod perl

# Apache 기본 설정 변경 (CGI 허용)
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \
    echo "ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/" >> /etc/apache2/sites-enabled/000-default.conf && \
    echo "<Directory \"/usr/lib/cgi-bin\">" >> /etc/apache2/sites-enabled/000-default.conf && \
    echo "    Options +ExecCGI" >> /etc/apache2/sites-enabled/000-default.conf && \
    echo "    AddHandler cgi-script .cgi .pl .py" >> /etc/apache2/sites-enabled/000-default.conf && \
    echo "    Require all granted" >> /etc/apache2/sites-enabled/000-default.conf && \
    echo "</Directory>" >> /etc/apache2/sites-enabled/000-default.conf

# 기본 인코딩을 EUC-KR로 설정
RUN echo "AddDefaultCharset EUC-KR" >> /etc/apache2/conf-available/charset.conf

# CGI 파일 및 데이터 디렉토리 복사
COPY src/*.cgi /usr/lib/cgi-bin/
COPY src/dat/ /var/www/html/dat/
COPY src/img/ /var/www/html/img/
COPY src/user/ /var/www/html/user/
COPY src/index.html /var/www/html/

# 실행 권한 설정
RUN chmod -R 755 /usr/lib/cgi-bin/*.cgi && \
    chmod -R 644 /var/www/html/index.html && \
    chmod -R 666 /var/www/html/dat/* && \
    chmod 777 /var/www/html/dat && \
    chmod -R 755 /var/www/html/user && \
    chmod -R 755 /var/www/html/img

# Windows 개행문자 문제 해결
RUN dos2unix /usr/lib/cgi-bin/*.cgi

# Apache 포트 개방
EXPOSE 80

# 컨테이너 실행 시 Apache 시작
CMD ["apachectl", "-D", "FOREGROUND"]

# 유저 데이터 폴더 생성 및 권한 설정
RUN mkdir -p /var/www/html/user && chmod 777 /var/www/html/user
