Summary:	WLAN based location library
Summary(pl.UTF-8):	Biblioteka do lokalizacji w oparciu o WLAN
Name:		libwlocate
Version:	1.36
Release:	1
License:	GPL v3 with exception
Group:		Libraries
# https://sourceforge.net/p/libwlocate/code/ci/v1.36/tarball
Source0:	https://sourceforge.net/code-snapshots/git/l/li/libwlocate/code.git/libwlocate-code-965e1fcd6950a458fcb06f71b9fe484af23e2268.zip
# Source0-md5:	190ebbc60ae096308a00774ac2c6c301
Patch0:		%{name}-make.patch
URL:		https://sourceforge.net/projects/libwlocate/
BuildRequires:	libiw-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libwlocate is a library that can be used to evaluate a geographical
position out of the WLAN networks that are available near to a user.

%description -l pl.UTF-8
libwlocate to biblioteka służąca do wyznaczania położenia
geograficznego na podstawie sieci WLAN dostępnych w pobliżu
użytkownika.

%package devel
Summary:	Header files for libwlocate library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libwlocate
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libwlocate library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libwlocate.

%prep
%setup -q -n libwlocate-code-965e1fcd6950a458fcb06f71b9fe484af23e2268
%patch0 -p1

%build
cd master

%{__make} -j1 \
	TARGET=ENV_LINUX \
	CC="%{__cc}" \
	STRIP=: \
	LDFLAGS="%{rpmldflags} -L. -lwlocate -lm" \
	VERBOUSFLAGS="%{rpmcflags} %{rpmcppflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

%{__make} -C master install \
	CHECK_LIBWLOCATE:=1 \
	CHECK_LWTRACE:= \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc master/{COPYING,CREDITS,README.md}
%attr(755,root,root) %{_bindir}/lwtrace
%attr(755,root,root) %{_libdir}/libwlocate.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/libwlocate.h
