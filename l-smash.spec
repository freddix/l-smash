Summary:	Yet another opensource mp4 handler
Name:		l-smash
Version:	1.13.27
Release:	2
Epoch:		1
License:	BSD-like
Group:		Libraries
Source0:	https://github.com/l-smash/l-smash/archive/v%{version}.tar.gz
# Source0-md5:	cdcd065bfe97adbfe2f41cb3620bc294
URL:		http://code.google.com/p/l-smash/
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Loyal to Spec of Mpeg4 and Ad-hoc Simple Hackwork.

%package libs
Summary:	L-SMASH library
Group:		Libraries

%description libs

%package devel
Summary:	Header files for L-SMASH library
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
This is the package containing the header files for L-SMASH library.

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix}		\
	--libdir=%{_libdir}		\
	--disable-static		\
	--enable-shared			\
	--extra-cflags="%{rpmcflags}"	\
	--extra-ldflags="%{rpmldflags}"
%{__make} \
	STRIP=/usr/bin/true

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\
	STRIP=/usr/bin/true

chmod +x $RPM_BUILD_ROOT%{_libdir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/boxdumper
%attr(755,root,root) %{_bindir}/muxer
%attr(755,root,root) %{_bindir}/remuxer
%attr(755,root,root) %{_bindir}/timelineeditor

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblsmash.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblsmash.so
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

