Summary:	Driver for the Lexmark 2030 printer
Name:		pbm2l2030
Version:	1.4
Release:	24
Group:		System/Printing
License:	GPLv2
Url:		http://home.fhtw-berlin.de/~s0226426/projects/pbm2l2030_faq.html
Source0:	http://home.fhtw-berlin.de/~s0226426/projects/pbm2l2030-1.4.tar.bz2
Patch0:	pbm2l2030-1.4-LDFLAGS.diff

%description
Lexmark 2030 Color Jetprinter printer driver.

%prep
%setup -c -q
%patch0 -p0

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
install -d %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}/

%files
%doc README* LICENSE 
%{_bindir}/*

