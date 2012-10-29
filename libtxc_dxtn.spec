Summary:	S3TC/DXTN texture compression/decompression library
Name:		libtxc_dxtn
Version:	1.0.0
Release:	2
License:	MIT
Group:		Libraries
Source0:	http://cgit.freedesktop.org/~mareko/libtxc_dxtn/snapshot/%{name}-%{version}.tar.bz2
# Source0-md5:	ebee75ed669f6011e3998ba0c358d778
Patch0:		%{name}-make.patch
URL:		http://people.freedesktop.org/~cbrill/libtxc_dxtn/
BuildRequires:	OpenGL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
S3TC/DXTN texture compression/decompression library. It can be
dlopened by Mesa to perform online compression or software
decompression of textures.

%prep
%setup -q
%patch0 -p1

%build
export LDFLAGS="%{rpmldflags}"
export CC="%{__cc}"
%{__make} \
	OPT_CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtxc_dxtn.so

