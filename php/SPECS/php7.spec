Name: php7
Version: 7.4.16

Release:    1%{?dist}
Summary:    php and php-fpm

Group:      Applications/Archiving
License:    GPLv2
URL:        https://github.com/xinzhanguo/rpmbuild/php
Packager:   xinzhanguo <e@xinzhanguo.cn>
Vendor:     xinzhanguo

Source0: php-%{version}.tar.gz
Source1: php.ini
Source2: php-fpm.conf
Source3: www.conf
Source4: redis.so
Source5: php-fpm.service

BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:  gcc
Requires:   openssl,openssl-devel,pcre-devel,pcre

Requires: sqlite-devel,zlib-devel,libxml2-devel,gd-devel,libcurl-devel,curl-devel,mcrypt,mhash,libmcrypt-devel,oniguruma-devel,libxslt-devel

%description
 php7.4 yuntu purge package.

%prep
rm -rf $RPM_BUILD_DIR/php-%{version}
tar fx $RPM_SOURCE_DIR/php-%{version}.tar.gz

%build
cd php-%{version}
./configure \
--prefix=/usr/local/php7 \
--enable-xml \
--enable-safe-mode \
--with-curl \
--enable-mbregex \
--enable-fpm \
--enable-mbstring \
--with-mcrypt \
--with-gd \
--with-openssl \
--with-mhash \
--enable-pcntl \
--enable-sockets \
--with-xmlrpc \
--enable-zip \
--enable-short-tags \
--enable-zend-multibyte \
--enable-static \
--with-xsl \
--with-fpm-user=nginx \
--with-fpm-group=nginx
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
cd php-%{version}
INSTALL_ROOT=%{buildroot} make install
%{__install} -p -D %{SOURCE1} %{buildroot}/usr/local/php7/lib/php.ini
%{__install} -p -D %{SOURCE2} %{buildroot}/usr/local/php7/etc/php-fpm.conf
%{__install} -p -D %{SOURCE3} %{buildroot}/usr/local/php7/etc/php-fpm.d/www.conf
%{__install} -p -D %{SOURCE4} %{buildroot}/usr/local/php7/lib/php/extensions/no-debug-non-zts-20190902/redis.so
%{__install} -p -D %{SOURCE5} %{buildroot}/lib/systemd/system/php-fpm.service

%files
%defattr(-,root,root,-)
/usr/local/php7/*
%config(noreplace) /usr/local/php7/etc/php-fpm.conf
%config(noreplace) /usr/local/php7/etc/php-fpm.d/www.conf
%config(noreplace) /lib/systemd/system/php-fpm.service

%changelog
* Mon Apr 28 2021 xinzhanguo (euclid)
- init php7 rpmbuild