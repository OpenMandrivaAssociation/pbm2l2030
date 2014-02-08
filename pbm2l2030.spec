Summary:	Driver for the Lexmark 2030 printer
Name:		pbm2l2030
Version:	1.4
Release:	14
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


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4-11mdv2011.0
+ Revision: 666996
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-10mdv2011.0
+ Revision: 607079
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-9mdv2010.1
+ Revision: 519051
- rebuild

* Tue Oct 06 2009 Thierry Vignaud <tv@mandriva.org> 1.4-8mdv2010.0
+ Revision: 454731
- do not package huge pbm image

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.4-7mdv2010.0
+ Revision: 426362
- rebuild

* Thu Dec 25 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4-6mdv2009.1
+ Revision: 318849
- use %%optflags and %%ldflags

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.4-5mdv2009.0
+ Revision: 223443
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4-4mdv2008.1
+ Revision: 179146
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4-3mdv2008.0
+ Revision: 75350
- fix deps (pixel)

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4-2mdv2008.0
+ Revision: 64169
- use the new System/Printing RPM GROUP

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4-1mdv2008.0
+ Revision: 64139
- Import pbm2l2030



* Thu Aug 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4-1mdv2008.0
- initial Mandriva package

* Tue May 04 2004 Wanderlei Antonio Cavassin <cavassin@conectiva.com.br>
+ 2004-05-04 09:58:12 (59161)
- Bumped Release.

* Mon Nov 10 2003 Ricardo Erbano <erbano@conectiva.com>
+ 2003-11-10 13:54:47 (39329)
- Fixed group description

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 18:36:10 (9011)
- Imported package from 8.0.
