%define		rev	823
%define		hash	55a4589

Summary:	Yet another opensource mp4 handler™
Name:		l-smash
Version:	%{rev}.%{hash}
Release:	1
License:	BSD-like
Group:		Libraries
# git clone https://code.google.com/p/l-smash/
# git archive --format=tar --prefix=l-smash-rev.hash/ HEAD | xz -c > l-smash-rev.hash.tar.xz
# rev -> git rev-list HEAD | wc -l
# hash -> git describe --always
Source0:	%{name}-%{version}.tar.xz
# Source0-md5:	b58c065215107b1e8f61072ca0866d52
URL:		http://code.google.com/p/l-smash/
Requires:	%{name}-libs = %{version}-%{release}
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
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for L-SMASH library.

%prep
%setup -q

%{__sed} -i -e "s|^REV.*|REV=%{rev}|" \
	-i -e "s|^HASH.*|HASH=%{hash}|" \
	configure

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
%attr(755,root,root) %{_libdir}/liblsmash.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

