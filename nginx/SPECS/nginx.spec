Name:       nginx
Version:    1.17.6
Release:    1%{?dist}
Summary:    nginx package

Group:      Applications/Archiving
License:    GPLv2
URL:        https://github.com/xinzhanguo/rpmbuild/nginx/
Packager:   xinzhanguo <e@xinzhanguo.cn>
Vendor:     xinzhanguo

Source0:    nginx-%{version}.tar.gz
Source1:    nginx.conf
Source2:    nginx.service

BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:  gcc
Requires:   openssl,openssl-devel,pcre-devel,pcre

%description
  Custom nginx package.

%prep
rm -rf $RPM_BUILD_DIR/nginx-%{version}
tar fx $RPM_SOURCE_DIR/nginx-%{version}.tar.gz

%build
cd nginx-%{version}
./configure \
--with-pcre-jit \
--with-http_realip_module \
--with-http_stub_status_module \
--with-http_ssl_module \
--with-debug \
--with-http_gzip_static_module \
--prefix=/usr/local/nginx
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
cd nginx-%{version}
make install DESTDIR=%{buildroot}
%{__install} -p -D %{SOURCE1} %{buildroot}/usr/local/nginx/conf/nginx.conf
%{__install} -p -D %{SOURCE2} %{buildroot}/lib/systemd/system/nginx.service

%files
%defattr(-,root,root,-)
/usr/local/nginx
%config(noreplace) /usr/local/nginx/conf/nginx.conf
%config(noreplace) /lib/systemd/system/nginx.service

%changelog
* Mon Apr 29 2021 xinzhanguo (euclid)
- init nginx

