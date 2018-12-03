Name:           etcd-grpc
Version:        1.0.0
Release:        1%{?dist}
Summary:        etcd gRPC C++ API
License:        BSD
Url:            https://github.com/DSSL-MSK3/%{name}
Source:		https://github.com/DSSL-MSK3/%{name}/archive/v%{version}.tar.gz

BuildRequires:  cmake >= 3.1.1
BuildRequires:	gcc-c++ >= 4.8.5
BuildRequires:	protobuf-devel >= 3.6.1
BuildRequires:	grpc-devel >= 1.15.1

Requires:	grpc >= 1.15.1

%description
etcd-grpc is a C++ auto-generated gRPC API for etcd version 3.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:	protobuf-devel >= 3.6.1
Requires:	grpc-devel >= 1.15.1

%description devel
Development files (headers) for %{name}.

%prep
%setup -q

%build
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr -DCMAKE_C_COMPILER=/usr/bin/gcc
make

%install
cd build
make install

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%define _libdir /usr/lib

%files
%{_libdir}/libetcd-grpc.so

%files devel
%{_includedir}/etcd/

%changelog
* Mon Nov 26 2018 Sergey Pronin <s.pronin@trassir.com> - 1.0.0-1
- RPM for DSSL Cloud
- Provide auto-generated C++ gRPC API as a library
