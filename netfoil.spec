%global debug_package %{nil}

Name:           netfoil
Version:        1.0
Release:        1%{?dist}
Summary:        Netfoil dns proxy

License:        Apache 2.0
URL:            https://github.com/tinfoil-factory/netfoil
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  golang
Requires:       systemd

%global _unitdir /usr/lib/systemd/system

%description
Netfoil is a dns proxy allowing for whitelisting of dns queries

%prep
%autosetup

%build
# NOTE: This requires an internet enabled build
GOOS=linux \
GOARCH=amd64 \
GO111MODULE=on \
GOPROXY=https://goproxy.io,direct \
CGO_ENABLED=0 \
go build -trimpath -o netfoil cmd/netfoil/main.go

%install
install -d %{buildroot}%{_sysconfdir}/netfoil
install -m0644 packaging/config/* %{buildroot}%{_sysconfdir}/netfoil/

install -D -m0644 packaging/systemd/netfoil.service %{buildroot}%{_unitdir}/netfoil.service
install -D -m0644 packaging/systemd/netfoil.socket %{buildroot}%{_unitdir}/netfoil.socket
install -D -m0644 packaging/systemd/netfoil.slice %{buildroot}%{_unitdir}/netfoil.slice

install -D -m0755 netfoil %{buildroot}%{_sbindir}/netfoil

%post
%systemd_post netfoil.socket
%systemd_post netfoil.service

%preun
%systemd_preun netfoil.service
%systemd_preun netfoil.socket

%postun
%systemd_postun netfoil.service
%systemd_postun netfoil.socket

%files
%{_sbindir}/netfoil
%{_unitdir}/netfoil.service
%{_unitdir}/netfoil.socket
%{_unitdir}/netfoil.slice
%dir %{_sysconfdir}/netfoil
%config(noreplace) %{_sysconfdir}/netfoil/*

%license LICENSE
%doc README.md

%changelog
* Sat Jun 14 2025 Simen Munch <simenmunch@gmail.com> - 1.0-1
- Initial release

