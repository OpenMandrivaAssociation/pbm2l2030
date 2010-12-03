Summary:	Driver for the Lexmark 2030 printer
Name:		pbm2l2030
Version:	1.4
Release:	%mkrel 10
Group:		System/Printing
License:	GPL
URL:		http://home.fhtw-berlin.de/~s0226426/projects/pbm2l2030_faq.html
Source0:	http://home.fhtw-berlin.de/~s0226426/projects/pbm2l2030-1.4.tar.bz2
Patch0:		pbm2l2030-1.4-LDFLAGS.diff
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Lexmark 2030 Color Jetprinter printer driver.

%prep

%setup -c -q
%patch0 -p0

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}

install -m 0755 %{name} %{buildroot}%{_bindir}/

%clean
rm -rf %{_builddir}/%{name}-%{version}
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README* LICENSE 
%attr(0755,root,root) %{_bindir}/*
